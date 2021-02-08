from PIL import Image

message_to_hide = 'It is a period of civil war. Rebel spaceships, striking from a hidden base, have won \
their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret \
plans to the Empire\'s ultimate weapon, the DEATH STAR, an armored space station with enough power to \
destroy an entire planet. Pursued by the Empire\'s sinister agents, Princess Leia races home aboard her \
starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy.\x03'

encode_map = {chr(i): f'{i:08b}' for i in range(0, 128)}

print(f'Message to hide: \n{message_to_hide}'.format(message_to_hide=message_to_hide))

with Image.open("Rebel_Alliance_flag.png") as img:
    width, height = img.size

    available_storage = (width * height) / 8
    message_size = len(message_to_hide) * 8

    if message_size > available_storage:
        print('You are trying to store {message_size} bytes in {available_storage} bytes'.format(
            message_size=message_size, available_storage=available_storage))
        exit()

    height_count = 0
    width_count = 0

    for char in message_to_hide:

        encoded_char = encode_map[char]

        for bits in encoded_char:

            for bit in bits:
                if height_count == height:
                    width_count += 1
                    height_count = 0

                pixel = list(img.getpixel((width_count, height_count)))

                # Encode the message just in the Red channel
                pixel[0] = pixel[0] & ~1 | int(bit)

                # Uncomment to encode the message in the three channels
                # for n in range(0, 3):
                #     pixel[n] = pixel[n] & ~1 | int(bit)

                img.putpixel((width_count, height_count), tuple(pixel))

                height_count += 1

    img.save("encoded_image.png")

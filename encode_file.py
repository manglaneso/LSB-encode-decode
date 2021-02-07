from PIL import Image

message_to_hide = '-[------->+<]>+++.+[--->+<]>.-.-------.-[--->+<]>--.++[--->++<]>.---.[->++++++<]>.+[->+++<]>.--[' \
                  '--->+<]>-.---[->++++<]>.------------.---.--[--->+<]>-.---[' \
                  '----->++<]>.-------------.---.+++.+++++++.[++>---<]>--.[' \
                  '->+++<]>+.+++++++++++..---.--------.+++++++++++++.-----------.++.'

encode_map = {
    '-': '00101101',
    '[': '01011011',
    '>': '00111110',
    '+': '00101011',
    '<': '00111100',
    ']': '01011101',
    '.': '00101110',
}

print(f'Message to hide: \n\n {message_to_hide}'.format(message_to_hide=message_to_hide))

with Image.open("Google_Chrome_Logo.png") as img:
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
                for n in range(0, 3):
                    pixel[n] = pixel[n] & ~1 | int(bit)

                img.putpixel((width_count, height_count), tuple(pixel))

                height_count += 1

    img.save("encoded_logo.png")

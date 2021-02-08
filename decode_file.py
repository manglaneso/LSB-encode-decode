from PIL import Image

decode_map = {f'{i:08b}': chr(i) for i in range(0, 128)}

# End of text character
end_of_text_char = '00000011'

extracted_bin = []

with Image.open("encoded_image.png") as img:
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))

            extracted_bin.append(pixel[0] & 1)
            # Uncomment to read the 3 bytes in every pixel.
            # for n in range(0, 3):
            #    extracted_bin.append(pixel[n]&1)

    decoded_bytes = []

    count = 0

    to_save = []

    to_save_string = ''

    for bit in extracted_bin:

        if count % 8 == 0 and count != 0:
            byte_string = "".join(to_save)

            if byte_string == end_of_text_char:
                break

            try:
                to_save_string += decode_map[byte_string]
            except KeyError:
                pass

            decoded_bytes.append("".join(to_save))
            to_save = []

        to_save.append(str(bit))
        count += 1

    print(decoded_bytes)
    print(to_save_string)

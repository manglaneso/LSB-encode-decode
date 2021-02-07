from PIL import Image

decode_map = {
    '00101101': '-',
    '01011011': '[',
    '00111110': '>',
    '00101011': '+',
    '00111100': '<',
    '01011101': ']',
    '00101110': '.'
}

extracted_bin = []
with Image.open("encoded_logo.png") as img:
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))

            extracted_bin.append(pixel[0] & 1)
            # for n in range(0, 3):
            #    extracted_bin.append(pixel[n]&1)

    decoded_bytes = []

    count = 0

    to_save = []

    to_save_string = ''

    for bit in extracted_bin:

        if count % 8 == 0 and count != 0:
            byte_string = "".join(to_save)

            # if byte_string != '00000000':
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

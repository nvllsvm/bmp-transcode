import argparse
import os

import PIL.Image


DEFAULT_WIDTH = 800


def image_to_file(input_file, output_file):
    im = PIL.Image.open(input_file)
    width, height = im.size

    pix = im.load()
    (r, g, b) = pix[width-1, height-1]

    original_size = get_original_size((r, g, b))

    original_file = []

    count = 0

    x = 0
    y = 0

    for i in range(width * height):
        if x == width:
            x = 0
            y += 1

        (r, g, b) = pix[x, y]

        for subpixel in pix[x, y]:
            if count != original_size:
                b = bytes([subpixel])
                original_file.append(b)
                count += 1

        x += 1

    output = open(output_file, 'wb')
    for b in original_file:
        output.write(b)


def get_original_size(pixel):
    binary_string = ''

    for s in pixel:
        n = "{0:b}".format(s).zfill(8)
        binary_string += n

    return int(binary_string, base=2)


def read_in_chunks(file_object, chunk_size=3072):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def get_rgb(path):
    binary_file = open(path, 'rb')

    for chunk in read_in_chunks(binary_file):
        chunk_len = len(chunk)
        for i in range(0, chunk_len, 3):
            int_bytes = []
            for b in chunk[i:i+3]:
                new_byte = b
                int_bytes.append(new_byte)

            # change this
            if len(int_bytes) == 2:
                int_bytes.append(0)
            elif len(int_bytes) == 1:
                int_bytes.append(0)
                int_bytes.append(0)

            yield tuple(int_bytes)


def file_to_image(input_file, output_file, width):
    file_bytes = []
    with open(input_file, 'rb') as f:
        byte = f.read(1)
        while byte != b"":
            file_bytes.append(byte)
            byte = f.read(1)

    num_bytes = os.path.getsize(input_file)

    height = num_bytes // width // 3
    remainder = num_bytes % width

    if remainder > 0:
        height += 1

    size = (width, height)
    im = PIL.Image.new('RGB', size)

    pix = im.load()

    x = 0
    y = 0

    for c in get_rgb(input_file):
        pix[x, y] = c
        x += 1

        if x == width:
            x = 0
            y += 1

    x = width - 1

    binary_string = str(bin(num_bytes))[2:].zfill(24)
    r = int(binary_string[0:8], 2)
    g = int(binary_string[8:16], 2)
    b = int(binary_string[16:24], 2)

    size_pixel = (r, g, b)

    pix[x, y] = size_pixel

    im.save(output_file)


def main():
    parser = argparse.ArgumentParser()
    sp = parser.add_subparsers()
    sp_to = sp.add_parser('to', help='To bitmap')
    sp_from = sp.add_parser('from', help='From bitmap')
    sp_to.set_defaults(mode='to')
    sp_from.set_defaults(mode='from')
    sp_to.add_argument('-w', '--width',
                       default=DEFAULT_WIDTH, type=int,
                       help=f'width of the image. Default is {DEFAULT_WIDTH}')
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    if args.mode == 'from':
        image_to_file(args.input_file, args.output_file)
    elif args.mode == 'to':
        file_to_image(args.input_file, args.output_file, args.width)


if __name__ == '__main__':
    main()

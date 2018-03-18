import argparse
import io
import math
import sys

import PIL.Image
import pkg_resources


# Sizes larger than this may trip decompression bomb checks in pillow
# https://github.com/python-pillow/Pillow/blob/ddc9e73b476965b17d9b6c8513da78a0b0877d57/src/PIL/Image.py#L2497
MAX_FILE_SIZE = PIL.Image.MAX_IMAGE_PIXELS * 3


class ImageFile:

    def __init__(self, path, mode='r', width=None, height=None):
        self.path = path
        self.mode = mode
        self.error = False

        if self.mode == 'r':
            self.image = PIL.Image.open(path)
            self.data = self.image.tobytes()

            width, height = self.image.size
            start_index = -1 * num_size_bytes(width * height * 3)
            self.size = bytes_to_int(self.data[start_index:])
        elif self.mode == 'w':
            self.data = bytearray()
            self.size = 0
            self.width = width
            self.height = height

            if self.width is not None and self.height is not None:
                raise ValueError('cannot specify both width and height')
        else:
            raise ValueError("invalid mode: '{}'".format(mode))

    def read(self):
        if self.mode != 'r':
            raise io.UnsupportedOperation()
        return self.data[:self.size]

    def write(self, data):
        if self.mode != 'w':
            raise io.UnsupportedOperation()

        _data = bytearray(data)
        new_size = self.size + len(_data)
        self._check_size(new_size)

        self.size = new_size
        self.data.extend(_data)

    def close(self):
        if self.error:
            return

        if self.mode == 'w':
            size = len(self.data)
            size_block = int_to_bytes(size)

            if self.width is not None:
                width = self.width
                height = math.ceil(size / width / 3)
            elif self.height is not None:
                height = self.height
                width = math.ceil(size / height / 3)
            else:
                width = math.ceil(math.sqrt(size / 3))
                height = math.ceil(size / width / 3)

            while True:
                max_size = (width * height) * 3
                self._check_size(max_size)
                max_size_block = num_size_bytes(max_size)
                extra_bytes = max_size - size - max_size_block
                if extra_bytes < 0:
                    if self.height is not None:
                        width += 1
                    else:
                        height += 1
                else:
                    extra_bytes += max_size_block - len(size_block)
                    break

            self.data.extend([0 for _ in range(extra_bytes)])
            self.data.extend(size_block)

            image = PIL.Image.frombytes('RGB', (width, height),
                                        bytes(self.data))
            image.save(self.path, format='bmp')
            image.close()
        elif self.mode == 'r':
            self.image.close()

    def _check_size(self, size):
        if size > MAX_FILE_SIZE:
            self.error = True
            raise ValueError('combined input must not exceed {} bytes'.format(
                MAX_FILE_SIZE))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def bytes_to_int(bs):
    return sum([b << 8*(len(bs)-i-1) for i, b in enumerate(bs)])


def num_size_bytes(number):
    return math.ceil(math.log(number, 2) / 8)


def int_to_bytes(number):
    return bytearray([
        number >> (i-1)*8 & 255
        for i in range(num_size_bytes(number), 0, -1)])


def image_to_file(input_file, output_path):
    with open(output_path, 'wb') as output_file:
        with ImageFile(input_file) as image:
            output_file.write(image.read())


def file_to_image(input_file, output_file, width, height):
    with ImageFile(output_file, 'w', width=width, height=height) as image:
        with open(input_file, 'rb') as f:
            while True:
                chunk = f.read()
                if chunk == b'':
                    break
                image.write(chunk)


def main():
    parser = argparse.ArgumentParser(
        description='Transcode orindary files to and from bitmap images.')
    parser.add_argument(
        '--version',
        action='version',
        version=pkg_resources.get_distribution('bmp-transcode').version)
    parser.set_defaults(mode=None)
    sp = parser.add_subparsers()

    sp_from = sp.add_parser(
        'from', help='recover a file from a bitmap image')
    sp_from.set_defaults(mode='from')
    sp_from.add_argument('infile', help='image file to recover from')
    sp_from.add_argument('outfile', help='recovered file')

    sp_to = sp.add_parser(
        'to', help='convert a file to a bitmap image')
    sp_to.set_defaults(mode='to')
    sp_to.add_argument('infile', help='file to be convert')
    sp_to.add_argument('outfile', help='resulting image file')
    sp_to.add_argument('--width', type=int, help='width in pixels')
    sp_to.add_argument('--height', type=int, help='height in pixels')

    args = parser.parse_args()

    if args.mode == 'from':
        image_to_file(args.infile, args.outfile)
    elif args.mode == 'to':
        if args.width and args.height:
            sp_to.print_usage()
            sys.stderr.writelines(
                ('bmp-transcode to: error: '
                 'arguments --width and --height cannot be used together\n'))
            exit(2)
        file_to_image(
            args.infile, args.outfile, args.width, args.height)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

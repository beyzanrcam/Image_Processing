import numpy as np

class PGMImage:
    def __init__(self, magic_number, width, height, maxval, pixels):
        self.magic_number = magic_number
        self.width = width
        self.height = height
        self.maxval = maxval
        self.pixels = pixels

    def write_pgm(self, filename):
        pixel_array = np.array(self.pixels, dtype=np.uint8).reshape((self.height, self.width))

        with open(filename, 'wb') as file:
            file.write(f"{self.magic_number}\n".encode())
            file.write(f"{self.width} {self.height}\n".encode())
            file.write(f"{self.maxval}\n".encode())
            pixel_array.tofile(file)
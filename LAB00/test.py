"""import numpy as np

def read_pgm(file_path):
    with open(file_path, 'rb') as file:
        magic_number = file.readline().strip().decode('ascii')
        
        line = file.readline().strip()
        while line.startswith(b'#'):
            line = file.readline().strip()
        
        width, height = map(int, line.split())
        maxval = int(file.readline().strip())
        data = file.read()
        pixel_values = list(data)
    
    return pixel_values, width, height, maxval, magic_number

def write_pgm(filename, width, height, maxval, pixels, magic_number):
    pixel_array = np.array(pixels, dtype=np.uint8).reshape((height, width))
    
    with open(filename, 'wb') as file:
        file.write(f"{magic_number}\n".encode()) 
        file.write(f"{width} {height}\n".encode())  
        file.write(f"{maxval}\n".encode())  
        
        pixel_array.tofile(file)

file_path = 'lena.pgm'
pixel_values, width, height, maxval, magic_number = read_pgm(file_path)

pixels_2d = np.array(pixel_values, dtype=np.uint8).reshape((height, width))
pixels_2d[29:50, :] = 0

modified_pixels = pixels_2d.flatten().tolist()

output_file_path = 'myLena.pgm'
write_pgm(output_file_path, width, height, maxval, modified_pixels, magic_number)
"""

import numpy as np

class PGMImage:
    def __init__(self, file_path=None):
        self.magic_number = None
        self.width = 0
        self.height = 0
        self.maxval = 0
        self.pixels = []

        if file_path:
            self.read_pgm(file_path)

    def read_pgm(self, file_path):
        with open(file_path, 'rb') as file:
            self.magic_number = file.readline().strip().decode('ascii')

            line = file.readline().strip()
            while line.startswith(b'#'):
                line = file.readline().strip()

            self.width, self.height = map(int, line.split())
            self.maxval = int(file.readline().strip())
            data = file.read()
            self.pixels = list(data)

    def write_pgm(self, filename):
        pixel_array = np.array(self.pixels, dtype=np.uint8).reshape((self.height, self.width))

        with open(filename, 'wb') as file:
            file.write(f"{self.magic_number}\n".encode())
            file.write(f"{self.width} {self.height}\n".encode())
            file.write(f"{self.maxval}\n".encode())
            pixel_array.tofile(file)

    def modify_pixels(self, row_start, row_end, new_value):
        pixels_2d = np.array(self.pixels, dtype=np.uint8).reshape((self.height, self.width))
        pixels_2d[row_start:row_end, :] = new_value
        self.pixels = pixels_2d.flatten().tolist()


file_path = 'lena.pgm'
output_file_path = 'myLena.pgm'

pgm_image = PGMImage(file_path)

pgm_image.modify_pixels(29, 30, 0) # 30. satıra 0 koy
pgm_image.write_pgm(output_file_path)

pgm_image.modify_pixels(49, 50, 0) # 50. satıra 0 koy
pgm_image.write_pgm(output_file_path)


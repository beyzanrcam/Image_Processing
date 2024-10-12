from mypgmread import PGMImage as PGMRead
from mypgmwrite import PGMImage as PGMWrite

# 3x3 piksel boyutundaki görüntünün yazılıp okuması
pixels = [101, 102, 103,
          104, 105, 106,
          107, 108, 109]

magic_number = 'P5'
width = 3
height = 3
maxval = 255

pgm_writer = PGMWrite(magic_number, width, height, maxval, pixels)
pgm_writer.write_pgm('test.pgm')

pgm_reader = PGMRead('test.pgm')

for i in range(len(pgm_reader.pixels)):
    print(f"Pixel {i + 1}: {pgm_reader.pixels[i]}")

# lena görüntüsünün okunup 30-50. satırlarına 0 yazılması

file_path = 'lena.pgm'
output_file_path = 'myLena.pgm'

pgm_image = PGMRead(file_path)

pgm_image.modify_pixels(29, 50, 0)  

pgm_writer = PGMWrite(pgm_image.magic_number, pgm_image.width, pgm_image.height, pgm_image.maxval, pgm_image.pixels)

pgm_writer.write_pgm(output_file_path)
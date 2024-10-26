import os
from PIL import Image

def convert_images_to_pgm(directory, output_directory):
    """
    Converts all images in the specified directory to PGM format.
    
    Parameters:
    - directory (str): The path to the directory containing the images.
    """
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file and if it is an image
        if os.path.isfile(file_path):
            try:
                # Open image file
                with Image.open(file_path) as img:
                    # Convert to grayscale if needed
                    img = img.convert("L")  # 'L' mode is for grayscale
                    # Save the image in PGM format with the same name but .pgm extension
                    new_filename = os.path.splitext(filename)[0] + ".pgm"
                    new_file_path = os.path.join(output_directory, new_filename)
                    img.save(new_file_path, format="PPM")  # PGM is part of the Netpbm formats, so we specify 'PPM'
                    
                    print(f"Converted {filename} to {new_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    # Specify your directory here
    my_file_dir = os.path.dirname(os.path.realpath(__file__))
    convert_images_to_pgm(my_file_dir+"/DIP3E_Original_Images_CH04",my_file_dir+ "/images")

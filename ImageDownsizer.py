import os
import argparse
from PIL import Image

# Command-line argument parser
parser = argparse.ArgumentParser(description='Downsize images in a directory.')
parser.add_argument('-i', '--input', help='Path to the input directory', required=True)
parser.add_argument('-o', '--output', help='Path to the output directory', required=True)
parser.add_argument('-s', '--size', type=int, help='Maximum size for the longest dimension of the image', required=True)
args = parser.parse_args()

# Folder containing the original images
input_folder = args.input

# Output folder for downsized images
output_folder = args.output

# Max size for the longest dimension of the image
max_size = args.size

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    print('Creating output directory:', output_folder)
    os.mkdir(output_folder)

# Supported image file formats
img_formats = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.ico']

# Loop through all files in the original directory
print('Starting downsizing process...')
for filename in os.listdir(input_folder):
    if os.path.splitext(filename)[1].lower() in img_formats:
        print('Processing', filename)
        
        try:
            img = Image.open(os.path.join(input_folder, filename))
        except IOError:
            print(f'Error opening image {filename}. Skipping...')
            continue
        
        # Only downsize if image is larger than the required size
        if max(img.size[0], img.size[1]) > max_size:
            ratio = max_size / max(img.size[0], img.size[1])
            new_dimensions = (int(img.size[0]*ratio), int(img.size[1]*ratio))
            img = img.resize(new_dimensions, Image.LANCZOS)
        else:
            print(f'Image {filename} is already within the target size. Skipping...')
            continue
        
        # Split the filename into name and extension, add suffix to the name
        base_name, extension = os.path.splitext(filename)
        output_filename = f"{base_name}_downsized{extension}"
        
        try:
            img.save(os.path.join(output_folder, output_filename))
            print(f'Saved downsized image as: {output_filename}')
        except IOError:
            print(f'Error saving image {filename}. Skipping...')
            continue
        finally:
            img.close()

print('Downsizing completed.')
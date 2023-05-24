# ImageDownsizer

## Introduction
"TheCodeSherpa" brings to you a powerful Python utility, ImageDownsizer.py, designed to efficiently downsize images in a directory while maintaining their original aspect ratio. The utility is built to support various image formats, including JPEG, PNG, TIFF, BMP, and ICO.

In addition, ImageDownsizer.py stands out with its improved error handling abilities, which ensure seamless operation even when faced with issues such as inability to open or save files, or non-existing input directories.

## Requirements
Python 3.x is necessary to run this script, along with the following Python packages:

- os
- argparse
- PIL (Python Imaging Library)

These packages can be installed with pip:

```bash
pip install pillow argparse
```

## Usage
Use the script from the command line with the following command:

```bash
python ImageDownsizer.py -i input_directory -o output_directory -s max_size
```

Where:

- `-i` or `--input`: Path to the input directory containing the images you want to downsize.
- `-o` or `--output`: Path to the output directory where the downsized images will be saved. If the directory doesn't exist, the script will create it.
- `-s` or `--size`: Maximum size for the longest dimension of the downsized images.

For instance, if you need to downsize images in the directory `/path/to/images`, save them in `/path/to/output`, and the maximum size for the longest dimension is 800, you would use:

```bash
python ImageDownsizer.py -i /path/to/images -o /path/to/output -s 800
```

The script will downsize all supported images in the input directory, skipping any images that are already within the target size, and save the resulting images in the output directory. The filename for each downsized image will include `_downsized` appended to the original filename.

## Contributing
Your contributions are always welcome! Please feel free to submit pull requests or open issues if you want to contribute to the project. Make sure that your code includes appropriate comments that explain any modifications or additions you've made.

## License
This project is open-source and freely available under the [MIT License](LICENSE).

# Img Bitify

Img Bitify is a script made in Python that converts directories and subdirectories of images into 8-bit or 6-bit depending on current size. This can be modified easily in the file itself to compass many different image sizes. The script itself is very basic, and I wrote it to be able to maintain directory structure and filename while converting large amounts of images for a different project.

## Requirements

This script requires [Python](https://www.python.org/downloads/), and [OpenCV](https://pypi.org/project/opencv-python/) to be installed. 

```sh
pip3 install opencv-python
```

## Usage

Save the bitify.py file, cd into the directory it is saved.
The script can be run with scraper.py arg1 where
- arg1 is the name of the folder containing the image files to be converted

A folder "Output" will be created in the directory of the script containing the converted images.

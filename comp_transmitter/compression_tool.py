"""
- Program uses imagemagick, optipng, jpegoptim
    - For mac: `brew install imagemagick` and `brew install optipng jpegoptim`
"""

import argparse
import subprocess
import os
from PIL import Image

parser = argparse.ArgumentParser(description="Image compression tool")
parser.add_argument('--filename', type=str, help="name of the image to compress")
args = parser.parse_args()

filename = args.filename
extension = filename.split('.')[-1]

print("Attempting to compress {:} with extension .{:}".format(args.filename, extension))
image_size = os.stat(filename).st_size
print("Image file size = {:} bytes".format(image_size))

if extension == "bmp":
    print("Using bmp compression program ")
elif extension == "png":
    # convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% source.jpg result.jpg
    pass 

result_name = filename.replace(os.sep,"").split('.')[-2] + "." + extension

magick_result = "magic_" + result_name
command = "convert -strip -interlace Plane -gaussian-blur 0.5 -quality 95% {:} {:}".format(filename,magick_result)
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

magick_size = os.stat(magick_result).st_size
print("ImageMagick Image file size = {:} bytes ({:.2f}%)".format(magick_size, (image_size-magick_size)/float(image_size) * 100))

pil_result = "PIL_" + result_name
Image.open(filename).save(pil_result, optimize=True, quality=20) #quality low-high -> 0-100
pil_size = os.stat(pil_result).st_size
print("PIL Image file size = {:} bytes ({:.2f}%)".format(pil_size, (image_size-pil_size)/float(image_size)*100))

# optipng_name = "OP_" + result_name
# command = "optipng -keep -out={:} -o=3 -f=5 {:}".format(optipng_name,filename)
# subprocess.Popen(command.split()).communicate()
# opti_size = os.stat(optipng_name).st_size

jpeg_name = "JPEG_" + result_name
command = "jpegoptim --size=20% --dest=./ --overwrite {:}".format(filename) #90k
subprocess.Popen(command.split()).communicate()
# opti_size = os.stat(jpeg_name).st_size
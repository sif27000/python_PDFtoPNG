import sys
import os
from PIL import Image

# grabs arguments from console
path = sys.argv[1]
directory = sys.argv[2]

# check if directory exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# eterate filenames in the gives source directory
# opens each files and save it in the new directory
# converting JPG to PGN
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
print('\n All done!')


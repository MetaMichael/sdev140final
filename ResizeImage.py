# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"add_task.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
newsize = (50, 50)
im1 = im.resize(newsize)
# Shows the image in image viewer
im1.show()
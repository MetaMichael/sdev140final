from PIL import Image, ImageTk

def get_image(filename, width = None, height = None):
    """Opens and resizes an image."""
    image = Image.open(filename)
    if width and height:
        newsize = (width, height)
        image = image.resize(newsize)
    image = ImageTk.PhotoImage(image)
    return image
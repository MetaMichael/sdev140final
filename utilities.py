"""
Author: Michael Barnard

Contains utility functions that are used by multiple modules.
"""
import os

import tkinter as tk

from PIL import Image, ImageTk

def get_image(filename, width = None, height = None):
    """Opens and resizes an image."""
    image = Image.open(filename)
    if width and height:
        newsize = (width, height)
        image = image.resize(newsize)
    image = ImageTk.PhotoImage(image)
    return image

def errorMessage(message):
        """Displays an error message in a new window."""
        # Create error window
        top = tk.Toplevel()
        top.geometry("300x50")
        top.title("ERROR")
        # Display error message
        label = tk.Label(top, text = message)
        # Create Exit button
        button = tk.Button(top, text = "Close", command = top.destroy)
        # Add widget to error window
        label.pack()
        button.pack()

def validFileName(name):
    """Ensures the name is not empty and the file does not exist."""
    name = name.strip()
    
    isValid = True
    if not isinstance(name, str):
        errorMessage("Input must be a string.")
        isValid = False
    elif name.strip() == "":
        errorMessage("To Do lists must have a name.")
        isValid = False
    else:
        fileName = "%s.tdl" % name
        # Ensure that the file does not exist
        if os.path.exists(fileName):
            errorMessage("'%s' already exists in this directory." % name)
            isValid = False
    
    return isValid

"""
# USAGE 
# Image must be a class attribute to prevent Python's garbage 
# collection from removing it
self.addIcon = get_image("icons/add.png", 30, 30)
self.addTask["image"] = self.addIcon
"""
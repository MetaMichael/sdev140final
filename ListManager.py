"""
Authour: Michael Barnard

Manages To Do lists in the current directory.
"""
import os

import tkinter as tk
from breezypythongui import EasyFrame

from todolist import ToDoList
from utilities import get_image

class ListManager(EasyFrame):
    """Manages the To Do List in the current working directory."""

    def __init__(self, title="Memory Hole", width=250, height=400, background="white", resizable=True):
        super().__init__(title, width, height, background, resizable)

        # Set up a list box for displaying the To Do List
        self.todolists = self.addListbox(row = 1, column = 0, rowspan = 10, columnspan = 3, height = 20)

        # Find the To Do List in the CWD
        lists = self.get_list_names()
        # Display the list names
        for list in lists:
            self.todolists.insert(tk.END, list)
        self.todolists.setSelectedIndex(0)
            
        # New List
        self.newButton = self.addButton(text = "New", row = 0, column = 0, command = self.new)
        # Image must be attribute to prevent Python garbage collection from removing it
        # <a href="https://www.flaticon.com/free-icons/add-document" title="add document icons">Add document icons created by Andrean Prabowo - Flaticon</a>
        self.newIcon = get_image("icons/clipboard.png", 30, 30)
        self.newButton["image"] = self.newIcon

        # Open List
        self.openButton = self.addButton(text = "Open", row = 0, column = 1, command = self.open)
        # <a href="https://www.flaticon.com/free-icons/open" title="open icons">Open icons created by Dreamstale - Flaticon</a>
        self.openIcon = get_image("icons/open.png", 30, 30)
        self.openButton["image"] = self.openIcon

        # Delete List
        self.deleteButton = self.addButton(text = "Delete", row = 0, column = 2, command = self.delete)
        # <a href="https://www.flaticon.com/free-icons/delete" title="delete icons">Delete icons created by Freepik - Flaticon</a>
        self.deleteIcon = get_image("icons/delete.png", 30, 30)
        self.deleteButton["image"] = self.deleteIcon

    

    def __str__(self):
        """Returns a string representation of the To Do list."""
        last = self.todolists.size()
        todolists = self.todolists.get(0, last)
        string = "Memory Hole" + str(todolists)
        return string
           
    def get_list_names(self):
        """Finds the To Do list in the currect working directory."""
        files = os.listdir(os.getcwd())
        names = []
        for file in files:
            if file[-3:] == "tdl":
                names.append(file[:-4])
        return names


    ############################
    ## Fix self.new
    ############################
    def new(self):
        """Creates a new To Do list."""
        name = self.prompterBox(title = "Create New List", promptString = "New List Name")

        if name != "":
            # Insert the new list above the currently selected list
            index = self.todolists.getSelectedIndex()
            if index == -1:
                # Add To List to beginning because there are none
                self.todolists.insert(0, name)
                self.todolists.setSelectedIndex(0)
                # Enable the delete and open buttons
                self.deleteButton["state"] = "normal"
                self.openButton["state"] = "normal"
            else:
                # Add the new To List after the current selection
                self.todolists.insert(index + 1, name)
                # Select the next To Do list
                self.todolists.selection_clear(index)
                self.todolists.setSelectedIndex(index + 1)

    def open(self):
        """Opens the selected To Do list."""
        listName = self.todolists.getSelectedItem()

        ToDoList(self, listName)

    def delete(self):
        """Deletes the selected To Do list."""
        # Delete the selected To Do list file
        listName = self.todolists.getSelectedItem()
        try:
            os.remove(listName + ".tdl")
        except FileNotFoundError:
            print("To Do List does not exist.")

        # Remove the To Do list name
        index = self.todolists.getSelectedIndex()
        self.todolists.delete(index)

        # Get the number of To Do list
        size = self.todolists.size()

        if size == 0:
            # Disable the delete and open buttons when the list is empty
            self.deleteButton["state"] = "disabled" 
            self.openButton["state"] = "disabled" 
        elif size <= index:
            # Select the last task 
            self.todolists.setSelectedIndex(size - 1)
        else:
            # Select the next task
            self.todolists.setSelectedIndex(index)

def main():
    ListManager().mainloop()

if __name__ == "__main__":
    main()
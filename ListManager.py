"""
Authour: Michael Barnard

Demonstration of the scrolling list box widget.
"""
import os
from ToDoList import ToDoList

from breezypythongui import EasyFrame

from tkinter import END, Toplevel

class ListManager(EasyFrame):
    """Manages the To Do List in the current working directory."""

    def __init__(self, title="Memory Hole", width=250, height=200, background="white", resizable=True):
        super().__init__(title, width, height, background, resizable)

        # Set up a list box for displaying the To Do List
        self.todolists = self.addListbox(row = 1, column = 0, rowspan = 4, columnspan = 3)

        # Find the To Do List in the CWD
        lists = self.get_list_names()
        # Display the list names
        for list in lists:
            self.todolists.insert(END, list)
        self.todolists.setSelectedIndex(0)
    

        ###################################################################
        # Must think about how to open the existing ToDo lists
        ###################################################################        
        
        # Set up the labels, fields, and buttons
        self.addButton(text = "New", row = 0, column = 0, command = self.new)
        self.openButton = self.addButton(text = "Open", row = 0, column = 1, command = self.open)
        self.deleteButton = self.addButton(text = "Delete", row = 0, column = 2, command = self.delete)

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
        """Opens the To Do list in a new window."""
        print("opening %s" % self.todolists.getSelectedItem())
        new = Toplevel()
        new.mainloop()

    def delete(self):
        """Deletes the selected To Do list, then selects the next one."""
        # Delete the selected To Do list
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

    def get_list_names(self):
        files = os.listdir(os.getcwd())
        names = []
        for file in files:
            if file[-3:] == "tdl":
                names.append(file[:-4])
        return names

def main():
    ListManager().mainloop()

if __name__ == "__main__":
    main()
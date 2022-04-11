"""
Authour: Michael Barnard

Demonstration of the scrolling list box widget.
"""

from breezypythongui import EasyFrame

from tkinter import END

class ListManager(EasyFrame):
    def __init__(self, title="Memory Hole", width=250, height=200, background="white", resizable=True):
        super().__init__(title, width, height, background, resizable)

        # Set up the list box
        # Note the event handler parameter for selecting a list item
        self.listBox = self.addListbox(row = 1, column = 0, rowspan = 4, columnspan = 3,
                                    listItemSelected = self.listItemSelected)

        ###################################################################
        # Must think about how to save the existing ToDo lists
        ###################################################################        
        # Add some items to the list box and select the first one
        self.listBox.insert(END, "Apple")
        self.listBox.insert(END, "Banana")
        self.listBox.insert(END, "Cherry")
        self.listBox.insert(END, "Orange")
        self.listBox.setSelectedIndex(0)
        ###################################################################
        # Must think about how to save the existing ToDo lists
        ###################################################################
        
        # Set up the labels, fields, and buttons
        self.addButton(text = "New", row = 0, column = 0, command = self.new)
        self.openButton = self.addButton(text = "Open", row = 0, column = 1, command = self.open)
        self.deleteButton = self.addButton(text = "Delete", row = 0, column = 2, command = self.delete)
        
        # Display current index and currently selected item
        self.listItemSelected(0)

    def listItemSelected(self, index):
        """Responds to the selection of an item in the list box.
        Updates the fields with the current item and its index."""
        pass
        """
        self.indexField.setNumber(index)
        self.itemField.setText(self.listBox.getSelectedItem())
        """

    def new(self):
        """If an input is present, insert it before the selected
        item in the list box.  The selected item remains current.
        If the first item is added, select it and enable the
        remove button."""

        #item = self.inputField.getText()
        item = self.prompterBox(title = "Create New List", promptString = "New List Name")

        if item != "":
            # Insert the new list above the currently selected list
            index = self.listBox.getSelectedIndex()
            if index == -1:
                # There are no To Do list so start at the beginning
                self.listBox.insert(0, item)
                self.listBox.setSelectedIndex(0)
                self.deleteButton["state"] = "normal"
                self.openButton["state"] = "normal"
            else:
                self.listBox.insert(index + 1, item)
                #self.listBox.setSelectedIndex(index + 1)

    def open(self):
        """Opens the To Do list in a new window."""
        print("opening %s" % self.listBox.getSelectedItem())

    def delete(self):
        """If there are items in the list, remove
        the selected item, select previous one,
        and update the fields.  If there was no previous
        item, select the next one.  If the last item is
        removed, disable the remove button."""
        index = self.listBox.getSelectedIndex()
        self.listBox.delete(index)
        if self.listBox.size() > 0:
            if index > 0:
                index -= 1
            self.listBox.setSelectedIndex(index)
        else:
            self.deleteButton["state"] = "disabled"
            self.openButton["state"] = "disabled"   

#class ToDoList(EasyFrame):


def main():
    ListManager().mainloop()

if __name__ == "__main__":
    main()
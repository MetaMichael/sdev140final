"""
Authour: Michael Barnard

A ToDo list
"""

from breezypythongui import EasyFrame
from tkinter import END, PhotoImage # Index of the last item in the list box
from PIL import Image, ImageTk

def get_image(filename, width, height):
    image = Image.open(filename)
    newsize = (width, height)
    return image.resize(newsize)

class ToDoList(EasyFrame):
    def __init__(self, title="Memory Hole", width=250, height=200, background="white", resizable=True):
        super().__init__(title, width, height, background, resizable)

        # Lists the existing tasks
        self.tasks = self.addListbox(row = 0, column = 0, rowspan = 4, columnspan = 2)

        # Allow user to input a new task
        self.addLabel("New Task:", row = 4,  column = 0)
        self.newTask = self.addTextField(text = "", row = 4, column = 1)
        self.newTask.bind("<Return>", lambda event: self.add()) # Typing enter will add

        # Create buttons to add or delete tasks and save the to do list
        self.addButton(text = "Add Task", row = 5, column = 0, command = self.add)
        self.deleteButton = self.addButton(text = "Delete Task", row = 6, column = 0, command = self.delete)
        self.addButton(text = "Save List", row = 7, column = 0, command = self.save)

        # # Load the image and associate it with the image label.
        # self.imageLabel = self.addLabel(text = "", row = 6, column = 0, sticky = "NSEW")
        # image = ImageTk.PhotoImage(get_image("add_task.png", width = 100, height = 100))
        # self.imageLabel.image = image
        #         
        ###################################################################
        # Must think about how to load an existing ToDo lists
        ################################################################### 
        
    def add(self):
        """Inserts a task after the currently selected task."""
        task = self.newTask.getText()
        if task != "":
            # Get the index of the current selection
            index = self.tasks.getSelectedIndex()
            if index == -1:
                # Add task to beginning because the list is empty
                self.tasks.insert(0, task)
                self.tasks.setSelectedIndex(0)
                # Enable the delete button
                self.deleteButton["state"] = "normal"
            else:
                # Add the new task after the current selection
                self.tasks.insert(index + 1, task)
                # Select the new task
                self.tasks.selection_clear(index)
                self.tasks.setSelectedIndex(index + 1)  

    def delete(self):
        """Deletes the selected task, then selects the next task."""
        # Delete the selected task
        index = self.tasks.getSelectedIndex()
        self.tasks.delete(index)

        # Get the number of task on the list
        size = self.tasks.size()

        if size == 0:
            # Disable the delete button when the list is empty
            self.deleteButton["state"] = "disabled" 
        elif size <= index:
            # Select the last task 
            self.tasks.setSelectedIndex(size - 1)
        else:
            # Select the next task
            self.tasks.setSelectedIndex(index)

    def save(self):
        """Saves the to do list."""
        # Request the file name
        name = self.prompterBox(title = "Save List", promptString = "List Name:")

        print("I will save this list as %s." % name)

        # Get the tasks as a tuple
        length = self.tasks.size()
        tasks = self.tasks.get(0, length)
        print(tasks)

        with open(name + ".txt", "w") as file:
            for task in tasks:
                file.write(str(task) + "\n")

        print("Save complete")

def main():
    ToDoList().mainloop()

if __name__ == "__main__":
    main()
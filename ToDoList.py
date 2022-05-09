"""
Authour: Michael Barnard

Defines the ToDoList class
"""
import tkinter as tk
#from tkinter import END, Toplevel, Tk
from breezypythongui import EasyFrame

from utilities import get_image

class ToDoList(EasyFrame, tk.Toplevel):
    """Window that displays a To Do list."""
    def __init__(self, parent, name, width=250, height=470, background="white", 
            resizable=True):
        # Open the To Do list in another window
        super(tk.Toplevel, self).__init__(parent, "toplevel")
        self.title(name)
        self.geometry("%dx%d" % (width, height))

        # The name of the To Do list
        self.name = name
        
        # Add task button
        self.addLabel(text = "Add", row = 0, column = 0, sticky = "S")
        self.addTask = self.addButton(text = "Add Task", row = 1, column = 0, 
                command = self.add)
        # Plus icons created by Kiranshastry - Flaticon
        # https://www.flaticon.com/free-icons/plus
        # Image must be a class attribute to prevent Python's garbage 
        # collection from removing it
        self.addIcon = get_image("icons/add.png", 30, 30)
        self.addTask["image"] = self.addIcon

        # Save list button
        self.addLabel(text = "Save", row = 0, column = 1, sticky = "S")
        self.saveButton = self.addButton(text = "Save List", row = 1, 
                column = 1, command = self.save)        
        # Save file icons created by Freepik
        # https://www.flaticon.com/free-icons/save-file
        self.saveIcon = get_image("icons/save-file.png", 30, 30)
        self.saveButton["image"] = self.saveIcon

        # Remove task button
        self.addLabel(text = "Remove", row = 0, column = 2, sticky = "S")
        self.removeTask = self.addButton(text = "Remove Task", row = 1, 
                column = 2, command = self.delete)
        # Minus icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/minus
        self.removeIcon = get_image("icons/minus.png", 30, 30)
        self.removeTask["image"] = self.removeIcon

        # Allow user to input a new task
        self.addLabel("New Task:", row = 2,  column = 0)
        self.newTask = self.addTextField(text = "", row = 2, column = 1)
        # Typing enter will add the task
        self.newTask.bind("<Return>", lambda event: self.add())

        # Display the tasks
        self.addLabel(text = "Tasks", row = 3, column = 0, 
                columnspan = 3, font = "bold")
        self.tasks = self.addListbox(row = 4, column = 0, rowspan = 10, 
                columnspan = 3, height = 20)
        with open(self.name + '.tdl', 'r') as tasksFile:
            for task in tasksFile:
                self.tasks.insert(tk.END, task.strip())

        # Disable the delete button when the list is empty
        size = self.tasks.size()
        if size == 0:
            self.removeTask["state"] = "disabled" 

    def __str__(self):
        """Returns a string representation of the To Do list."""
        last = self.tasks.size()
        tasks = self.tasks.get(0, last)
        string = self.name + str(tasks)
        return string

    def add(self):
        """Inserts a new task in the list."""
        task = self.newTask.getText()
        if isinstance(task, str):
            task = task.strip()
            if task != "":
                # Get the index of the current selection
                index = self.tasks.getSelectedIndex()
                if index == -1:
                    # Add task to beginning because the list is empty
                    self.tasks.insert(0, task)
                    self.tasks.setSelectedIndex(0)
                    # Enable the delete button
                    self.removeTask["state"] = "normal"
                else:
                    # Add the new task after the current selection
                    self.tasks.insert(index + 1, task)
                    # Select the new task
                    self.tasks.selection_clear(index)
                    self.tasks.setSelectedIndex(index + 1)  

    def delete(self):
        """Deletes the selected task."""
        # Delete the selected task
        index = self.tasks.getSelectedIndex()
        self.tasks.delete(index)

        # Get the number of task on the list
        size = self.tasks.size()

        if size == 0:
            # Disable the delete button when the list is empty
            self.removeTask["state"] = "disabled" 
        elif size <= index:
            # Select the last task 
            self.tasks.setSelectedIndex(size - 1)
        else:
            # Select the next task
            self.tasks.setSelectedIndex(index)

    def save(self):
        """Saves the to do list with a 'tdl' file extension."""
        # Get the tasks as a tuple
        length = self.tasks.size()
        tasks = self.tasks.get(0, length)

        # Save the tasks to a text file
        with open(self.name + ".tdl", "w") as file:
            for task in tasks:
                file.write(str(task) + "\n")

def main():
    # Create a window as the parent of TopLevel
    root = tk.Tk()
    ToDoList(root, "Example List").mainloop()

if __name__ == "__main__":
    main()
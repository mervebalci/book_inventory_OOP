# Rewriting the App Using Classes and OOP
# frontend.py

from tkinter import *
from backend import Database


# Creating an OBJECT from the CLASS
database = Database("books.db")


# Creating the CLASS
class Window(object):


# Creating INIT METHOD
    def __init__(self, window):

        self.window = window

        # Adding a TITLE to the program
        self.window.wm_title("BookStore")


        # Creating Label Object
        label1 = Label(window, text = "Title")
        label1.grid(row = 0, column = 0)

        label2 = Label(window, text = "Author")
        label2.grid(row = 0, column = 2)

        label3 = Label(window, text = "Year")
        label3.grid(row = 1, column = 0)

        label4 = Label(window, text = "ISBN")
        label4.grid(row = 1, column = 2)


        # Creating Entry for Each Label
        self.title_text = StringVar()
        self.entry1 = Entry(window, textvariable = self.title_text)
        self.entry1.grid(row = 0, column = 1)

        self.author_text = StringVar()
        self.entry2 = Entry(window, textvariable = self.author_text)
        self.entry2.grid(row = 0, column = 3)

        self.year_text = StringVar()
        self.entry3 = Entry(window, textvariable = self.year_text)
        self.entry3.grid(row = 1, column = 1)

        self.isbn_text = StringVar()
        self.entry4 = Entry(window, textvariable = self.isbn_text)
        self.entry4.grid(row = 1,column = 3)


        # Creating a Listbox
        self.list = Listbox(window, height = 7, width = 48)
        self.list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)


        # Creating a Scrollbar
        scrollbar = Scrollbar(window)
        scrollbar.grid(row = 2, column = 2, rowspan = 6)


        # Applying a Configure Method to the Listbox and to the Scrollbar on y-axis
        self.list.configure(yscrollcommand = scrollbar.set)
        scrollbar.configure(command = self.list.yview)


        # Adding a BIND Function
        self.list.bind('<<ListboxSelect>>', self.get_selected_row)


        # Adding Buttons
        button1 = Button(window, text = "View all", width = 12, command = self.view_command)
        button1.grid(row = 2, column = 3)

        button2 = Button(window, text = "Search entry", width = 12, command = self.search_command)
        button2.grid(row = 3, column = 3)

        button3 = Button(window, text = "Add entry", width = 12, command = self.add_command)
        button3.grid(row = 4, column = 3)

        button4 = Button(window, text = "Update selected", width = 12, command = self.update_command)
        button4.grid(row = 5, column = 3)

        button5 = Button(window, text = "Delete selected", width = 12, command = self.delete_command)
        button5.grid(row = 6, column = 3)

        button6 = Button(window, text = "Close", width = 12, command = window.destroy)
        button6.grid(row = 7, column = 3)


    def get_selected_row(self, event):
        index = self.list.curselection()[0]
        self.selected_tuple = self.list.get(index)
        self.entry1.delete(0, END)
        self.entry1.insert(END, self.selected_tuple[1])
        self.entry2.delete(0, END)
        self.entry2.insert(END, self.selected_tuple[2])
        self.entry3.delete(0, END)
        self.entry3.insert(END, self.selected_tuple[3])
        self.entry4.delete(0, END)
        self.entry4.insert(END, self.selected_tuple[4])


    # Creating a VIEW Method to call backend (View Function has no parameters, not like Search Method)
    def view_command(self):
        self.list.delete(0, END)
        for row in database.view():
            self.list.insert(END, row)


    # Creating a SEARCH Method to call backend and look for entries
    # Be Careful !!! Search Function has parameters. We need to append GET method to output a string object
    def search_command(self):
        self.list.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list.insert(END, row)


    # Creating an INSERT Method to add new entries
    # Again Insert Function in the backend has arguments, so we need to append GET method
    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list.delete(0, END)
        self.list.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    # Creating a DELETE Method to remove entries
    def delete_command(self):
        database.delete(self.selected_tuple[0])


    # Creating an UPDATE Method to update the entries
    # Update Function is not much different than Delete Function.
    # The only difference is Delete Function in backend has only one argument while Update Function in backend has 5
    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())


# Creating a WINDOW OBJECT
window = Tk()
Window(window)


# Applying a Mainloop Method which is a way to wrap up all the widgets you enter
window.mainloop()
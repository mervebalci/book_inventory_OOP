"""
A program that stores book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add an entry
Update an entry
Delete an entry
Close
"""

from tkinter import *
from backend import Database
# We import the database class from backend script. So, this makes available the database class for us.
# Database is BLUEPRINT.


# Creating a CLASS
database = Database("books.db")


# After we say View All, when we click on any entry, it will pop up on the entry section
# Without TRY-EXCEPT, when you click on the listbox on empty GUI, python gives you IndexError
def get_selected_row(event):
    try:
        global selected_tuple
        index = list.curselection()[0]
        selected_tuple = list.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass


# Creating a VIEW Fumction to call backend (View Function has no parameters)
def view_command():
    list.delete(0,END)
    for row in database.view():
        list.insert(END, row)


# Creating a SEARCH Function to call backend and look for entries
# Be Careful !!! Search Function has parameters. We need to append GET method to output a string object
def search_command():
    list.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list.insert(END, row)


# Creating an INSERT Function to add new entries
# Again Insert Function in the backend has arguments, so  we need to append GET method
def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


# Creating a DELETE Function to remove entries
def delete_command():
    database.delete(selected_tuple[0])


# Creating an UPDATE Function to update the entries
# Update Function is not much different than Delete Function.
# The only difference is Delete Function in backend has only one argument while Update Function in backend has 5
def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


# Creating a Window Object
window=Tk()


# Adding a Title for the program
window.title('Book Store')


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
title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.grid(row = 0, column = 1)

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.grid(row = 0, column = 3)

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.grid(row = 1, column = 1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.grid(row = 1, column = 3)


# Creating a Listbox
list = Listbox(window, height = 7, width = 48)
list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)


# Creating a Scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2, rowspan = 6)


# Applying a Configure Method to the Listbox and to the Scrollbar on y-axis
list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = list.yview)


# Adding a BIND Function
list.bind('<<ListboxSelect>>', get_selected_row)


# Adding Buttons
button1 = Button(window, text = "View All", width = 13, command = view_command)
button1.grid(row = 2, column = 3)

button2 = Button(window, text = "Search", width = 13, command = search_command)
button2.grid(row = 3, column = 3)

button3 = Button(window, text = "Add", width = 13, command = add_command)
button3.grid(row = 4, column = 3)

button4 = Button(window, text = "Update", width = 13, command = update_command)
button4.grid(row = 5, column =3)

button5 = Button(window, text = "Delete", width = 13, command = delete_command)
button5.grid(row = 6, column =3)

button6 = Button(window, text ="Close", width =13, command = window.destroy)
button6.grid(row = 7, column =3)


# Applying a Mainloop Method which is a way to wrap up all the widgets you enter
window.mainloop()
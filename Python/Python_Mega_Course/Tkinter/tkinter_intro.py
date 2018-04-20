# Section 14 - Building Graphical User Interfaces with Tkinter
# 117 - Introduction to Tkinter
# Introduction to GUI - Desktop Applications
# Steps to make a BookStore database
# You can add new books to the database and also search for new ones
# #############################################################################
# Modification Idea - Automate the process of adding a book to the database
# pdf parsing + webscrapping to extract the book relevant information
# Machine Learning classification algorithm to select the relevant category/folder
# to the book file
# #############################################################################
# 118 - Setting up a GUI with Widgets
# The program will use Tkinter and SQLite3

# 119 - Connecting GUI Widgets with Callback Functions
# execute functions when clicking in a button, or modifying widgets
# to do that we use the command argument in the button definition
# note that we should not pass the brackets for the function in the
# command argument.

# for python 3 the library it is tkinter, for python 2 Tkinter
# We are going to import all from tkinter library
from tkinter import *

# we need to create a window to put our Widgets and a loop to execute that window
# everthing will go between our window initialization and the window.mainloop()
window=Tk()

# function to be executed when pressing the button
def km_to_miles():
    # we will look at the entry widged to get the value to be converted
    # the entry is stored in the e1_value string variable, so will work with that
    # note that we need to apply the get method, because e1_value is not really
    # a string, it is a Tkinter StringVal object.
    print(e1_value.get())
    try:
        miles = float(e1_value.get())*1.6
        t1.insert(END, miles)
        # now, lets insert the value stored in miles to the text widget
    except:
        miles = "Type a valid number!"
        t1.insert(END, miles)

# creating a button widged
b1=Button(window, text='Execute', command=km_to_miles)
# we need to specify where to put the button in the window
# there are two methods for that, pack and grid
# with grid we have more control over the positio
b1.grid(row=0, column=0)
# lets add some more widgeds
# to access the text in a Entry widget we need to declare a StringVar and pass
# it as argument for the textvariable
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0,column=2)


window.mainloop()

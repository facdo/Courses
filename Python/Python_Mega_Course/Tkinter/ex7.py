# Coding Exercise 7: Creating a Multi-Widget GUI

# Create a python program that expects a Kg input value and converts that value
# to grams, pounds and ounces when the user pushes the convert button.

from tkinter import *

window = Tk()


def convert():
    print(kg_value.get())
    # reset the text boxes
    gram_txt.delete('1.0', END)
    pound_txt.delete('1.0', END)
    ounce_txt.delete('1.0', END)
    try:
        grams = float(kg_value.get())*1000
        pounds = float(kg_value.get())*2.20462
        ounces = float(kg_value.get())*35.274
        gram_txt.insert(END, grams)
        pound_txt.insert(END, pounds)
        ounce_txt.insert(END, ounces)
    except:
        gram_txt.insert(END, "Type a valid number!")

kg_label = Label(window, text="Kg")
kg_label.grid(row=0,column=0)

kg_value = StringVar()
entry = Entry(window, textvariable=kg_value)
entry.grid(row=0, column=1)

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=2)

gram_txt = Text(window, height=1, width=20)
gram_txt.grid(row=1, column=0)

pound_txt = Text(window, height=1, width=20)
pound_txt.grid(row=1, column=1)

ounce_txt = Text(window, height=1, width=20)
ounce_txt.grid(row=1, column=2)

window.mainloop()

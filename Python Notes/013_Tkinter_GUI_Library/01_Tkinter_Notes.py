from tkinter import *

''' Importing from a class * allows us to use that class as it is.'''
window = Tk()
window.title("My First Clicking Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Label", font=("Times New Roman", 31, "bold"))
my_label.pack(expand=True)

my_label["text"] = "New Text"
my_label.config(text="Am I Clicked?")

# Button

def button_clicked():
	print("I got clicked!")
	my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack(side="bottom")

# Entry

input = Entry()
input.pack()

window.mainloop()

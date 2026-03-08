from tkinter import *


def button_clicked():
	print("I got fucked")
	label_mile.config(text=float(input.get()) * 5 / 3)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

label_1 = Label(text="Miles", font=("Arial", 14, "bold"))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Arial", 14, "bold"))
label_2.grid(column=0, row=1)

label_3 = Label(text="Km", font=("Arial", 14, "bold"))
label_3.grid(column=2, row=1)

label_mile = Label(text="0", font=("Arial", 14, "bold"))
label_mile.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(END, string="0")

button = Button(text="Convert", command=button_clicked, font=("Arial", 16, "bold"))
button.grid(column=1, row=2)

window.mainloop()

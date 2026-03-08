from tkinter import *
import requests
import os

def get_quote():
    quotes = requests.get(url="https://api.kanye.rest/")
    quotes.raise_for_status()
    quote = quotes.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "background.png")
background_img = PhotoImage(file=image_path)

canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "kanye.png")
kanye_img = PhotoImage(file=image_path)

kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
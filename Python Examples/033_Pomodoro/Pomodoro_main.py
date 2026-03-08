from tkinter import *
import math
import os  # os modülünü ekleyin

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	global reps
	window.after_cancel(timer)
	my_label.config(text="Timer") 
	canvas.itemconfig(timer_text, text="00:00")
	checkmark.config(text="")
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	if reps % 8 == 0:
		count_down(long_break_sec)
		my_label.config(text="Long Break", fg=RED)
	elif reps % 2 == 0:
		count_down(short_break_sec)
		my_label.config(text="Break", fg=PINK)
	else:
		count_down(work_sec)
		my_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"
	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps / 2)
		for x in range(work_sessions):
			marks += "✔"
		checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

my_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, )
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
script_directory = os.path.dirname(__file__)
image_path = os.path.join(script_directory, "tomato.png")

tomato_png = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, bg="white", font=(FONT_NAME, 12, "bold"))
start_button.grid(column=0, row=2)

checkmark = Label(text="", font=(FONT_NAME, 31, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
checkmark.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer, bg="white", font=(FONT_NAME, 12, "bold"))
reset_button.grid(column=2, row=2)

window.mainloop()

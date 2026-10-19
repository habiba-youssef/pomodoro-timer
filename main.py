from tkinter import *
import math

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
timer_running = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps

    reps = 0
    window.after_cancel(timer_running)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="STUDY!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_running

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_running = window.after(100, count_down, count-1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(reps/2)

        for _ in range(work_session):
            mark += "✔"
            check_mark.config(text= mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Method")
window.configure(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,135,text='00:00',font=(FONT_NAME,30,'bold'),fill='white')

canvas.grid(row=2,column=2)

title_label = Label(text="TIMER", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(row=1,column=2)

start_button = Button(text='Start',width=6, command=start_timer)
start_button.grid(row=3,column=0)

restart_button = Button(text='Reset',width=6, command=reset)
restart_button.grid(row=3,column=4)

check_mark = Label(text='', font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW)
check_mark.grid(row=4,column=2)

window.mainloop()

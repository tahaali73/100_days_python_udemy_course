import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
raps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global raps
    raps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_time():
    global raps
    raps += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if raps % 8 == 0:
        title_label.config(text="break",fg=RED)
        count_down(long_break_sec)

    elif raps % 2 == 0:
        title_label.config(text="break",fg=PINK)
        count_down(short_break_sec)
    
    else: 
        count_down(work_sec)
        title_label.config(text="Timer",fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
       count_sec = f"0{count_sec}"
      
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)

    else: 
        star_time()
        marks =""
        session = int(raps/2)
        for _ in range(session):
            marks += "✔"

        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", bg=YELLOW,fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200,height=224, bg=YELLOW)
tomato_img=tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
time_text = canvas.create_text(102,130, fill="white",text="00:00" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#count_down(5)

start_button = tk.Button(text="Start", bg=YELLOW, command=star_time)
start_button.grid(column=0,row=2)

stop_button = tk.Button(text="Reset", bg=YELLOW, command=reset_timer)
stop_button.grid(column=2,row=2)

check_mark  = tk.Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()
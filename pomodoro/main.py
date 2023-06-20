import tkinter
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
timer = None #used to reset

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer) #cancels window.after so timer stops
    timer_label.config(text="Timer",font=(FONT_NAME,28,"bold"))
    check_mark_label.config(text='')
    canvas.itemconfig(time_on_canvas, text="00:00")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps #counts how many times the timer started
    reps += 1
    print(reps)
    if reps%8==0:
        count_down(LONG_BREAK_MIN *60)
        timer_label.config(text="Long-Break",font=(FONT_NAME,28,"bold"))
    elif reps%2 == 0:
        count_down(SHORT_BREAK_MIN *60)
        timer_label.config(text="Short-Break",font=(FONT_NAME,28,"bold"))
    else:
        count_down(WORK_MIN *60)
        timer_label.config(text="Timer",font=(FONT_NAME,28,"bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    mins = math.floor(count / 60)
    secs = math.floor(count % 60)
    '''if and elif are to print single digit values into 
    double digits'''
    if secs == 0:
        secs = '00'
        
    elif secs < 10: 
        secs=f"0{secs}"
        
    canvas.itemconfig(time_on_canvas, text=f"{mins}:{secs} ")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_time()
        check_mark=''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✔ "
        check_mark_label.config(text=check_mark, fg=RED)
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomorodo")
window.minsize(600,400)
window.config(padx=50,pady=50,bg=YELLOW)
#we need to use canvas widget to add tomato image on to the window
#canvas allows us to draw or place top of that canvas

canvas = tkinter.Canvas(width=230,height=224,bg=PINK,highlightthickness=0) #set canvas geometry according to image geometry (for this pro only)
#bg(for background color of canvas) and highlightthickness(border around canvas) are attributes
#how to add image in canvas
tomato = tkinter.PhotoImage(file='Python/Tkinter/pomorodo/tomato.png')
# print(type(tomato))
canvas.create_image(115,113,image=tomato) #100,112 are coordinates where image has to be placed
#we cannot assign image address directly to image argument because img type expected by create_image() is different (photoimage)
time_on_canvas = canvas.create_text(110,130,text='00:00', font=(FONT_NAME,28,"bold"))
canvas.grid(row=1,column=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,28,"bold"))
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text='Start', padx=10,pady=10,command=start_time)
start_button.grid(row=2,column=0)

reset_button = tkinter.Button(text='Reset', padx=10,pady=10, command=reset)
reset_button.grid(row=2,column=2)

check_mark_label = tkinter.Label(bg=YELLOW, fg=RED)
check_mark_label.grid(row=3,column=1) 
window.mainloop()

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
timer = None #We have to initialise the timer variable to make the reset (stop()) function work
#We just set it to none so it has literally no value. We just want it to exist 


# ---------------------------- TIMER RESET ------------------------------- # 

def stop():
    global reps
    reps = 0

    window.after_cancel(timer)  #This will cancel the timer using the after_cancel() method

    main_label.config(text= "Timer")
    canvas.itemconfig(timer_text, text = "0:00")
    checkmark.config(text="")




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def take_break(time):
    main_label.config(text= "Take a Break")
    count_down(time)

def work(time):
    main_label.config(text= "Work")
    count_down(time)

def start_timer():
    global reps
    reps += 1

    if reps >= 8 and reps % 8 == 0:
        take_break(LONG_BREAK_MIN*60)
    elif reps % 2 != 0:
        work(WORK_MIN*60)
    else:
        take_break(SHORT_BREAK_MIN*60)


        




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#Tkinter is an event driven GUI
#She explains in the video why we can't use time.sleep()
#So we have to do it using Tkinter methods

#We're basically gonna use recursion to solve our little problem
def count_down(count):
    global reps

    count_minute = math.floor(count / 60)
    count_second = count % 60

    #This is to make the seconds display like a normal timer
    if count_second < 10:
        count_second = f"0{count_second}"

    #thanks to DYNAMIC TYPING, we can do stuff like on the line above and below

    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_second}")  #Need this function to change text on canvas
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        #using the after() method, after 1000 ms, it will perform a function (count_down() in this case, which is why its recursive)), and pass 
        #the following parameters into said function (in this case, count - 1)
    else:
        start_timer()   #This is so the timer keeps going automatically once it reaches 0

        #This is to show the check marks for each completed work session
        marks = ""
        for rep in range(math.floor(reps/2)):
            marks += "✓"
        checkmark.config(text= marks)

        if reps == 8:
            reps = 0


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)

canvas = Canvas(width= 400, height= 224, bg= YELLOW, highlightthickness= 0) 
#numbers are from the size of the tomato png, but we put 224 instead of 223 so we get to work with even numbers

tomato_image = PhotoImage(file= "tomato.png")   #for Tkinter, we need to put images in a Photoimage object in order to use it, like in a canvas
canvas.create_image(200, 112, image = tomato_image) #The 100 and 112 is the x and y values, respectively, of the placement of the image
#We did this so it's bang in the middle of the canvas

timer_text = canvas.create_text(200, 130, text= "00:00", fill="white", font= (FONT_NAME, 35, "bold")) #130 is to center the text relative to the tomato

main_label = Label(text="Timer", bg= YELLOW, fg = GREEN, font = (FONT_NAME, 35, "bold"))
main_label.grid(row = 0, column = 1)

checkmark = Label(text="", bg= YELLOW, fg = GREEN, font= (FONT_NAME, 20, "bold"))
checkmark.grid(row= 3, column= 1)

start = Button(text= "Start", command= start_timer)
start.grid(row= 2, column= 0)

reset = Button(text= "Reset", command= stop)
reset.grid(row= 2, column= 2)

canvas.grid(row= 1, column= 1)  







window.mainloop()
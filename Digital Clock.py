from tkinter import Label, Tk
import time

#Define the title and size of our application
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1, 1)

#Define the font of the time and its color, its border width and 
#the background color of the digital clock

text_font = ("Boulder", 68, 'bold')
background = '#f2e750'
foreground = '#363529'
border_width = 25

#Combine all the elements to define the label of the clock application

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

#Define the main function of our digital clock.
#Here I will set the text of the label as the realtime

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
    

digital_clock()
app_window.mainloop()
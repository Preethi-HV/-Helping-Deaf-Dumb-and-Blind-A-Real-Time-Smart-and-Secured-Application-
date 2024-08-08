from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os

app = Tk()
app.title("Welcome")
img =Image.open('C:\\Users\\Preethi Aradhya\\Desktop\\deaf_dumb_blind\\deaf_dumb_blind\\bg image.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("1650x1050")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = "ASSITIVE COMMUNICATION SYSTEM FOR DEAF,DUMB &BLIND PEOPLES",bg="#3db7bf",
               font=("Times New Roman", 24))

label2.pack(pady = 50)


import os

def button1():
    os.system('start cmd /c python text_to_speech.py')
    
def button2():
    os.system('python gesture_to_voice.py')

def button3():
    os.system('start cmd /c python voice_to_text.py')
    
def button4():
    os.system('start cmd /c python image_to_voice.py')

def button5():
    os.system('python ObjectDetection.py')

def Submit():
    pass  
    
b1=tk.Button(app,text="text_to_speech",command=button1,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=100,y=200)

b1=tk.Button(app,text="gesture_to_voice",command=button2,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=400,y=200)

b1=tk.Button(app,text="voice_to_text",command=button3,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=700,y=200)

b1=tk.Button(app,text="image_to_voice",command=button4,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=1000,y=200)

b1=tk.Button(app,text="Object Detection",command=button5,bg="#3db7bf",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=20)
b1.place(x=700,y=300)


app.mainloop()


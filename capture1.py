from tkinter import *
import tkinter.font as font
import time 
import pyscreenshot
import os
master = Tk() 
master.title("Mohit's Counter") 
global a 
def openNewWindow(): 
    newWindow = Toplevel(master) 
    newWindow.title("New Window") 
    # sets the geometry of toplevel 
    newWindow.geometry("400x400") 
   

def fun1():
	try:
		print ("Hello")
		path = "C:\\Screenshots"
		if not os.path.isdir(path):
			os.mkdir(path)
		
		image = pyscreenshot.grab()
		name = e1.get()
		image.save(f"C:\\Screenshots\\{name}.png")
		print ("SS taken")
		
	except Exception as e :
		print (e)
	



e1 = Entry(master,bg='#ffffb3')

button = Button(master, text='Capture', width=5, command=fun1, bg='#0052cc', fg='#ffffff',font=("Helvetica", 10))


e1.grid(row=0, column=1) 

button.grid(row=2,column=1 )
mainloop() 
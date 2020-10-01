# purpose: 
# a simple GUI app that saves the applications that you want to run and run them all with one button

# Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python
# interface to the Tk GUI toolkit, and is Python's de facto standard GUI. 
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

# --------------------------- LOGIC ---------------------------------
apps = []

# import the previous opened apps, if any
if os.path.isfile('savedapps.txt'):
    with open('savedapps.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    """
    if you are using Windows, you can limit the file types that users can access to
    filetyps = (("executables","*.exe"),("all files","*.*")
    """
    filename = filedialog.askopenfilename(initialdir="/", title="Select File")
    apps.append(filename)

    # let's add the file name to our frame
    # before doing that let's clear what is on the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # here, we create a label for each filename. These labels can be added to the frame.
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApp():
    for app in apps:
        os.popen(app) # the windows equivalent of this command is os.startfile()




# --------------------------- CANVAS ---------------------------------
# let's attach a canvas to our root
# Canvas widget to display graphical elements like lines or text.
# define the canvas first
canvas = tk.Canvas(root, height=500, width=800, bg='#aae7ae')
# attach the canvas to the root.
canvas.pack()


# --------------------------- FRAME ---------------------------------
# let's attach a frame to our root
# Frame widget which may contain other widgets and can have a 3D border.
# define the frame first
frame = tk.Frame(root, bg="#aaaaaa")
# place the frame inside the canvas. You should determine the relative height, width and its 
# relative place on the canvas
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# --------------------------- BUTTONS ---------------------------------
# let's add a button to the root
# Button widget.
openfile = tk.Button(root, text="Open File", padx=10,pady=5, fg="white", bg="#f64242", command=addApp)
openfile.pack() # this button is attached to the root

# let's add another button to the root
runapp = tk.Button(root, text="Run Applications", padx=10,pady=5, fg="white", bg="#f64242", command=runApp)
runapp.pack() # this button is attached to the root



for app in apps:
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()

root.mainloop()


# --------------------------- SAVE ---------------------------------
# let's save our files in a text file for future access
with open('savedapps.txt','w') as f:
    for app in apps:
        f.write(app + ',')
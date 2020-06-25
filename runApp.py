import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("RUN APPS")
apps = []

# =====================Functions===================

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApp = tempApps.split(',')
        apps = [x for x in tempApp if x.strip()]


def deleteChild():
    for widget in frame.winfo_children():
        widget.destroy()


def frameText():
    for app in apps:
        appName = app.split("/")
        lable = tk.Label(frame, text=appName[len(
            appName)-2], bg="#fff5ee")
        lable.pack()


def addApps():
    deleteChild()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executable", "*.exe"), ("All File", "*.*")))
    apps.append(filename)

    frameText()


def runApp():
    for app in apps:
        os.startfile(app)


def clearApps():
    del apps[:]
    os.remove('save.txt')
    deleteChild()
    frameText()

# ================= GUI LAYOUT====================


frame1 = tk.Frame(root, width=500, height=500, bg="#375782")
frame1.grid(row=0)

frame = tk.Frame(frame1, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

frame2 = tk.Frame(root, width=500, height=100)
frame2.grid(row=1)

openFile = tk.Button(frame2, text="Open File", padx=55.4,
                     pady=5, fg="white", bg="#375782", command=addApps)
openFile.grid(row=0, column=0)

runApps = tk.Button(frame2, text="Run Apps", padx=55.4,
                    pady=5, fg="white", bg="#375782", command=runApp)
runApps.grid(row=0, column=1)

clearAll = tk.Button(frame2, text="Clear All", padx=55.4,
                     pady=5, fg="white", bg="#375782", command=clearApps)
clearAll.grid(row=0, column=2)

frameText()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+",")

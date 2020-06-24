import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("RUN APPS")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApp = tempApps.split(',')
        apps = [x for x in tempApp if x.strip()]


def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executable", "*.exe"), ("All File", "*.*")))
    apps.append(filename)

    for app in apps:
        lable = tk.Label(frame, text=app, bg="grey")
        lable.pack()


def runApp():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, width=500, height=500, bg="#375782")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="#375782", bg="white", command=addApps)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#375782", command=runApp)
runApps.pack()

for app in apps:
    lable = tk.Label(frame, text=app, bg="grey")
    lable.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+",")

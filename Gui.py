import tkinter
from tkinter import ttk
import codeToRun
import sv_ttk

# main = codeToRun.codeToRun()

root = tkinter.Tk(screenName="Traveling Salesperson")

root.geometry("800x800")

frame = ttk.Frame(root)

label = ttk.Label(frame, text="Traveling Salesperson", font=("Ariel", 20, "bold"))

time_label = ttk.Label(frame, text="", font=("Ariel", 10, "bold"))
label.pack(pady=20)
time_label.pack(pady=10)

buttons = [ttk.Button(frame, text="Naive", style='Accent.TButton'),
           ttk.Button(frame, text="Optim", style='Accent.TButton'),
           ttk.Button(frame, text="Aprox", style='Accent.TButton')]

for button in buttons:
    button.pack(pady=20, padx=20, side="left")

frame.pack()


# This is where the magic happens
sv_ttk.set_theme("dark")


root.mainloop()
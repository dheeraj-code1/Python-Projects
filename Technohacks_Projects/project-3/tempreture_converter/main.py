import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    if option.get() == options[0]:
        tmp = (input_temp.get() * 9 / 5) + 32
        output_temp.set(f"{round(tmp,4)}°F")
    else:
        tmp = (input_temp.get() - 32) * 5 / 9
        output_temp.set(f"{round(tmp,4)}°C")

# Window
window = ttk.Window(themename='cyborg')
window.title("Temperature Converter")
window.geometry('350x200')
window.resizable(0, 0)

# Fonts
title_font = tkFont.Font(family="Comic Sans MS", size=18, weight="bold")
output_font = tkFont.Font(family="Comic Sans MS", size=22, weight="bold")

# Title
title_label = ttk.Label(master=window, text='Temperature converter', font=title_font)
title_label.pack()

# Frame
frame = ttk.Frame(window)
frame.pack(side='top')

# Combo Box
options = ["Celsius to Fahrenheit (°C to °F)", "Fahrenheit to Celsius (°F to °C)"]
option = tk.StringVar(value=options[0])
combo = ttk.Combobox(frame, textvariable=option,font="Cursive 9 bold")
combo['values'] = options
combo.pack(pady=10, expand=True, fill='x')

# Input
input_temp = tk.DoubleVar(value=0.0)
entry = ttk.Entry(frame, textvariable=input_temp)
entry.pack(padx=10, side='left', fill='x', expand=True)

button = ttk.Button(master=frame, text='Convert', command=convert)
button.pack(side='left', expand=True, fill='x')
window.bind("<Return>",lambda x:convert())

# Output
output_temp = tk.StringVar(value='')

output_label = ttk.Label(window, textvariable=output_temp, font=output_font)
output_label.pack(side='bottom')

# Run
window.mainloop()

import tkinter as tk
import subprocess

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import warnings
warnings.filterwarnings("ignore")  

def open_file1():
    subprocess.Popen(["python", r"E:\Academics Project\MiniProject\main.py"])

def open_file2():
    subprocess.Popen(["python", r"E:\Academics Project\MiniProject\Volume_and_brightness_control.py"])

window = tk.Tk()
window.title("My Interface")

button1 = tk.Button(window, text="Cursor Control", command=open_file1)
button1.pack(pady=20)

button2 = tk.Button(window, text="Volume/Brightness \nControl", command=open_file2)
button2.pack(pady=20)

window.mainloop()

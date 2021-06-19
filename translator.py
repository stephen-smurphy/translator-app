import tkinter as tk
from tkinter.constants import LEFT, RIGHT

#Window
window = tk.Tk()
window.geometry("848x480")
window.title("Translator App")

#Input Side (Left)
inputLabel = tk.Label(text = "Enter Text" ).grid(row=0, column=0)
input = tk.StringVar()

inputEntry = tk.Entry().grid(row=0, column=1)

#Output Side (Right)
label = tk.Label(text = "Translation:" ).grid(row=1, column=0)

window.mainloop()
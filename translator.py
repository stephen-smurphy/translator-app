import tkinter as tk
from tkinter.constants import LEFT, RIGHT


def getTranslation():
    print("test")


window = tk.Tk()
window.geometry("848x480")
window.title("Translator App")

inputLabel = tk.Label(text = "Enter Text" ).grid(row=0, column=0)
inputEntry = tk.Entry().grid(row=0, column=1)
inputButton = tk.Button(text = "Go", command = getTranslation).grid(row=0, column=2)

output = tk.StringVar()
output.set("Translation: ")
outputLabel = tk.Label(textvariable = output).grid(row=2, column=0)

window.grid_rowconfigure(0, minsize=100)
window.mainloop()
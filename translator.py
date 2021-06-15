import tkinter as tk
from tkinter.constants import LEFT, RIGHT

window = tk.Tk()
window.geometry("848x480")
window.title("Translator App")

frame = tk.Frame(window)
frame.pack()

leftFrame = tk.Frame(window)
leftFrame.configure(background="red")
leftFrame.pack(side=LEFT)

rightFrame = tk.Frame(window)
rightFrame.configure(background="blue")
rightFrame.pack(side=RIGHT)

#Input Side (Left)
label = tk.Label(leftFrame, text = "Enter Text" )
label.pack()

translateInput = tk.Entry(leftFrame, width = 20)
translateInput.pack(padx = 5, pady = 5)

#Output Side (Right)
label = tk.Label(rightFrame, text = "Translation:" )
label.pack()

window.mainloop()
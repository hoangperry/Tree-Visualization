from tkinter import *

root = Tk()

canvas = Canvas(root, width=900, height=500)
canvas.pack()
menu = Menu(root)
root.config(menu=Menu)


root.mainloop()
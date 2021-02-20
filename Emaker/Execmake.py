"""
Wasam Ashraf Syed

Creating executable from dataofish tutorial

"""

import tkinter as MyWin

root = MyWin.Tk()

canvas1 = MyWin.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello():
    label1 = MyWin.Label(root, text = 'Hello World!', fg = 'Red', font = ('Times New Roman', 14, 'bold'))
    canvas1.create_window(150, 200, window = label1)
    
button1 = MyWin.Button(text = 'Click Me!', command = hello, bg = 'brown', fg = 'white')
canvas1.create_window(150, 150, window = button1)

root.mainloop()
import os
import pyscreenshot as ImageGrab
import tkinter as tk

root= tk.Tk()

root.wm_title("easyshot")

canvas1 = tk.Canvas(root, width = 250, height = 150, bg = '#FFD43B', relief = 'raised')
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(125, 50, window=entry1)

def takeScreenshot ():
    im = ImageGrab.grab()
    name = entry1.get()
    im.save(f'{name}.png')

    
button1 = tk.Button(text='      Take Screenshot      ', command=takeScreenshot, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(125, 100, window=button1)


root.mainloop()

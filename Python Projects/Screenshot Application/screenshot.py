import pyautogui 
from unicodedata import name
import tkinter as tk
import time

def screenshot():
    time.sleep(5)
    name=time.time()
    name='D:/SKILLS/Python Programming/Python Projects/Screenshot Application/{}.png'.format(name)
    img=pyautogui.screenshot()
    img.save(name)
    img.show()



root=tk.Tk()
frame=tk.Frame(root)
frame.pack()


button=tk.Button(frame,text="Take screenshot",command=screenshot)
button.pack(side=tk.LEFT)

close=tk.Button(frame,text="QUIT",command=quit)
close.pack(side=tk.LEFT)


root.mainloop()


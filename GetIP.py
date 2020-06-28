from tkinter import *
import requests
import pyperclip


root = Tk()
root.resizable(0,0)

label = Label(root, text = 'Checking...',fg='black',bg='yellow',font = '50',width='30',height='5')
label.pack(side = TOP)

try:
    r = requests.get("https://api.ipify.org/?format=json").json()
    ip = r["ip"]
    label.config(text = ip)
except:
    label.config(text = "Can't Connect To a Server!!!" )

def copy():
    pyperclip.copy(ip)
button = Button(root,text = 'Click To Copy',fg = 'black',bg = 'orange',font='50',width='30',height='3',command = copy)
button.pack(side = TOP)

root.mainloop()
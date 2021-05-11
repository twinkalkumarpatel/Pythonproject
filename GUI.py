import tkinter as tk
from tkinter import Label,messagebox,Button,Entry,TOP,BOTTOM
import webbrowser

root = tk.Tk()
root.geometry("300x100")
root.minsize(300,100)
root.maxsize(300,100)

root.title("Multiple open URL")



labal1 = Label(text = "Enter New URL:")
labal1.pack()


E1 = Entry()
E1.pack()

def url():
    webbrowser.Chrome("C:/Program Files/Google/Chrome/Application/chrome.exe").open_new(E1.get())    


button1 = Button(text = "Open URL", command = url, fg = "green")
button1.pack()

root.mainloop()
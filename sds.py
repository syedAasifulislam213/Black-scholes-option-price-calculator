from tkinter import *

root = Tk()
root.configure(background='black')
root.geometry('400x200')
root.title("Test GUI")

label = Label(root, text="Hello", bg="purple", fg="white", font=("Arial", 25))
label.grid(row=0, column=0)

entry = Entry(root, bg="yellow", fg="black", font=("Arial", 20))
entry.grid(row=0, column=1)

root.mainloop()
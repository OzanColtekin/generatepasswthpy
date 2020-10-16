import pyperclip
import random
from tkinter import *

class Generator():
    def __init__(self):
        self.password_str = StringVar()
        self.password_keys = StringVar()
        self.password_len = IntVar()

    def create(self):
        password = ""
        for x in range(self.password_len.get()):
            password = password + random.choice(self.password_keys.get())
        self.password_str.set(password)


    def copy(self):
        random_password = self.password_str.get()
        pyperclip.copy(random_password)

    def Button(self,root):
        Label(root, text="Password Generator",font="calibri 20 bold").pack()
        Label(root, text="Which letters or numbers do you want to include in your password").pack(pady=3)
        Entry(root, textvariable=self.password_keys).pack(pady=3)
        Label(root, text="Enter password length").pack(pady=3)
        Entry(root, textvariable=self.password_len).pack(pady=3)
        Button(root, text="Generate password",command=self.create).pack(pady=7)
        Entry(root, textvariable=self.password_str).pack(pady=3)
        Button(root, text="Copy!",command=self.copy).pack()
        self.password_len.set("Please enter a integer!")

root = Tk()
root.title("Random Password Generator v0.1")
root.geometry = "600x600"

for_main = Generator()
for_main.Button(root)

root.mainloop()

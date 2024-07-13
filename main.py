import random
import tkinter as tk
from tkinter import *


def passwordGenerator():
    inp = area.get()
    if inp.isdigit():
        charactersList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        password = []
        for i in range(int(inp)):
            x = random.choice(charactersList)
            password.append(x)
        generated_password = "".join(password)
        result.set(generated_password)
        l1.configure(text="Your Password")
        evaluateStrength(generated_password)
    else:
        l1.configure(text="Enter Only digits", font="bold")


def evaluateStrength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()" for char in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 8 and (has_upper or has_lower) and has_digit and has_special:
        strength = "Moderate"
    else:
        strength = "Weak"

    l2.configure(text=f"Password Strength: {strength}")


def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    root.update()  # now it stays on the clipboard after the window is closed
    l3.configure(text="Password copied to clipboard!")


root = Tk()
root.geometry("400x300")
root.title("Password Generator")
root.wm_iconbitmap("icon.ico")
input1 = StringVar()
result = StringVar()

area = Entry(root, textvariable=input1, font="lucida 12")
area.pack(pady=10)

l1 = Label(root, text="Enter password length", font="lucida 10")
l1.pack()

b1 = Button(root, text="Generate Password", font="lucida 12", command=passwordGenerator, width=20)
b1.pack(pady=10)

area2 = Entry(root, textvariable=result, font="lucida 12", state='readonly')
area2.pack(pady=10)

l2 = Label(root, text="Your Password Strength", font="lucida 10")
l2.pack()

b2 = Button(root, text="Copy to Clipboard", font="lucida 12", command=copyToClipboard, width=20)
b2.pack(pady=10)

l3 = Label(root, text="", font="lucida 10")
l3.pack()

root.mainloop()

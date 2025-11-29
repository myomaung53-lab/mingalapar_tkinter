import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import bcrypt

def on_enter(event):
    if user_entry.get() == 'Username':
        user_entry.delete(0, 'end')

def on_leave(event):
    if user_entry.get() == '':
        user_entry.insert(0, 'Username')

def on_enter_1(e):
    if pws_entry.get() == 'Password':
        pws_entry.delete(0, 'end')
        pws_entry.config(show='*')

def on_leave_1(e):
    if pws_entry.get() == '':
        pws_entry.insert(0, 'Password')
        pws_entry.config(show='')


def toggle_password():
    if pws_entry.cget('show') == '':
        pws_entry.config(show='*')
    else:
        pws_entry.config(show='')

def register_user():
    username = user_entry.get()
    password = pws_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields")
        return
    if users_collection.find_one({"username": username}):
        messagebox.showerror("Error", "Username already exists")
        return

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) #  Hash password
    print(hashed_password)

    users_collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    messagebox.showinfo("Success", "Registered successfully!")

def login_user():
    username = user_entry.get()
    password = pws_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields")
        return

    user = users_collection.find_one({"username": username})

    if user:
        ans = bcrypt.checkpw(password.encode(), user["password"]) # to check password
        if ans:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid password")
    else:
        messagebox.showerror("Error", "User not found")


window = tk.Tk()
window.geometry('800x700')
window.config(bg='white')

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
users_collection = db["users"]

img = Image.open("Pictogrammers-Material-Light-Eye.48.png")
resized = img.resize((24, 24))  # (width, height)
eye_img = ImageTk.PhotoImage(resized)

logo = Image.open("Untitled-2.png")
logo.thumbnail((320, 320))
logo_img = ImageTk.PhotoImage(logo)

tk.Label(window, bg='white', image=logo_img,).pack(pady=(10, 20))
user_entry = tk.Entry(window, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 12)) # username အတွက် Entry ထည့်ခြင်း
user_entry.pack(pady=(0, 2))
tk.Frame(window, width=295, height=2, bg='black').pack(pady=(0, 15)) # frame widget  ကိုအသုံးပြုပြီ line ပုံစံ ပြုလုပ်ခြင်း

# ======================= [Password Entry + Eye Button] -> Frame =====================
pw_frame = tk.Frame(window, bg='white')  # password entry & button ကိုအတူတူထည့်မယ့် frame
pw_frame.pack()
pws_entry = tk.Entry(pw_frame, width=22, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 12))
pws_entry.pack(side='left', pady=(0, 2))
tk.Button(pw_frame, bg='white', border=0, image=eye_img, command=toggle_password).pack(side='left') # 

tk.Frame(window, width=295, height=2, bg='black').pack(pady=(0, 20)) # for line

tk.Button(window, width=39, pady=7, text='Register', bg='#57a1f8', fg='white', border=0, command=register_user,).pack(pady=10) 
tk.Button(window, width=39, pady=7, text='Login', bg='#57a1f8', fg='white', border=0, command=login_user,).pack(pady=10) 

user_entry.insert(0, 'Username')
pws_entry.insert(0, 'Password')

user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)
pws_entry.bind("<FocusIn>", on_enter_1)
pws_entry.bind("<FocusOut>", on_enter_1)

window.mainloop()





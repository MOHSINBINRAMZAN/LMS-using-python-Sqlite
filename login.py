from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
from time import strftime
from math import sin, cos, radians
import sqlite3
from PIL.Image import Resampling  # Corrected import

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        # Background colors
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # Login frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=650, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # Username
        lbl_user = Label(login_frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_user = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=50, y=130, width=250)

        # Password
        lbl_pass = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_pass = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=50, y=200, width=250)

        # Sign In Button
        btn_login = Button(login_frame, text="Sign In", command=self.login_action, font=("times new roman", 14), bg="darkgreen", fg="white")
        btn_login.place(x=50, y=250, width=120, height=35)

        # Forget Password Button
        btn_forgot_password = Button(login_frame, text="Forget Password?", command=self.forget_password_action, font=("times new roman", 12), bg="white", fg="blue", borderwidth=0)
        btn_forgot_password.place(x=50, y=290, width=150, height=30)

        # Clock
        self.lbl = Label(left_lbl, text="webcode clock", font=("times new roman", 15), bg="#08A3D2", fg="white")
        self.lbl.place(x=100, y=100, width=400, height=400)
        self.working()

    def login_action(self):
        # Placeholder for login action
        print("Username:", self.txt_user.get())
        print("Password:", self.txt_pass.get())

    def forget_password_action(self):
        # Placeholder for forget password action
        print("Forget Password clicked")

    def working(self):
        string = strftime("%H:%M:%S %p")
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png")
        
        bg = bg.resize((300, 300), Resampling.LANCZOS)  # Updated resampling filter
        clock.paste(bg, (50, 50))
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="black", width=4)
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="blue", width=3)
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="green", width=2)
        draw.ellipse((195, 195, 210, 210), fill="black")
        clock.save("images/clock_new.png")

if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()
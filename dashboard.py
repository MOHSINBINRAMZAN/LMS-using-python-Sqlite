

from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from PIL.Image import Resampling  
from math import radians, sin, cos
from courses import Courseclass
from student import studentclass
from result import Resultclass
from report import reportclass
from tkinter import messagebox
import os
from datetime import datetime
from time import strftime

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Icons
        image = Image.open("images/logo_p.png")
        image = image.resize((50, 50), Resampling.LANCZOS) 
        self.logo_dash = ImageTk.PhotoImage(image)
        
        title = Label(self.root, text="Student Result Management System", image=self.logo_dash, font=("goudy old style", 40, "bold"), bg="#033054", fg="white", compound='left', padx=10, pady=10)
        title.place(x=0, y=0, relwidth=1, height=80)

        M_Frame = LabelFrame(self.root, text="Menu", font=("times new roman", 15, "bold"), bg="white")
        M_Frame.place(x=10, y=80, width=1300, height=80)

        btn_course = Button(M_Frame, text="Courses", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_course ).place(x=20, y=5, width=200, height=35)
        btn_student = Button(M_Frame, text="Students", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_student).place(x=240, y=5, width=200, height=35)
        btn_result = Button(M_Frame, text="Results", font=("goudy old style", 15, "bold"), command=self.add_result, bg="#0b5377", fg="white", cursor="hand2").place(x=460, y=5, width=200, height=35)
        btn_viewstudentresult = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_report).place(x=680, y=5, width=200, height=35)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=35)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.exit).place(x=1120, y=5, width=200, height=35)
        
        self.bg_img = Image.open("images/png.jpeg.png")
        self.bg_img = self.bg_img.resize((920, 350), Resampling.LANCZOS)  # Corrected usage of Resampling
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.label_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)
        
        self.label_courses = Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE, bg="#262626", fg="white").place(x=400, y=540, width=250, height=90)
        
        self.label_students = Label(self.root, text="Total students\n[0]", font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE, bg="#e43b06", fg="white").place(x=710, y=540, width=250, height=90)
        
        self.label_result= Label(self.root, text="Total results\n[0]", font=("goudy old style", 20, "bold"), bd=5, relief=RIDGE, bg="#038074", fg="white").place(x=1020, y=540, width=250, height=90)
        
        footer = Label(self.root, text="SRMS_Student Result Management System \n contact us for any technical issue: 987xxxxx01", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        # Clock
        self.img = ImageTk.PhotoImage(file="images/c.png")  # Placeholder for initial clock image
        self.lbl = Label(self.root, image=self.img)
        # Adjust the clock position
        self.lbl.place(x=0, y=160, width=400, height=400)
        self.working()

    def working(self):
        string = strftime("%H:%M:%S %p")
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
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
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Courseclass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentclass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Resultclass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportclass(self.new_win)
            
    def logout(self):
        np=messagebox.askyesno("Confirm","Do you want to logout?",parent=self.root)
        if np==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        np=messagebox.askyesno("Confirm","Do you want to exit?",parent=self.root)
        if np==True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
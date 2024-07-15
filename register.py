from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left Image
        self.left = ImageTk.PhotoImage(file="images/side.png")
        Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Main Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # First Name
        fname = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        fname.place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        lname = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        lname.place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        contact.place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        email.place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        question.place(x=50, y=240)
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.cmb_question["values"] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_question.place(x=50, y=270, width=250)
        self.cmb_question.current(0)

        # Answer
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        answer.place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # Password
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        password.place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        # Confirm Password
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        cpassword.place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # Terms and Conditions
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        chk.place(x=50, y=380)

        # Register Button
        btn_register = Button(frame1, text="Register Now", command=self.register_data, font=("times new roman", 15), bg="green", fg="white")
        btn_register.place(x=50, y=420, width=250)

    def register_data(self):
        # Registration logic here
        pass

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
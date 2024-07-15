from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Add Student Details", font=("goudy old style", 25, "bold"), bg="#FFA500", fg="#262626").place(x=10, y=15, width=1180, height=50)
        
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_obt = StringVar()
        self.var_total_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=80)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_course = Label(self.root, text="Enter Course", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=200)
        lbl_marks_obt = Label(self.root, text="Enter Marks Obtained", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)
        lbl_total_marks = Label(self.root, text="Enter Total Marks", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=320)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy old style", 15), state="readonly", justify=CENTER)
        self.txt_student.place(x=280, y=80, width=200)
        self.txt_student.set("Select")

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=500, y=80, width=100, height=28)

        text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightgray", state="readonly").place(x=280, y=140, width=320)
        text_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15), bg="lightgray", state="readonly").place(x=280, y=200, width=320)
        text_marks = Entry(self.root, textvariable=self.var_marks_obt, font=("goudy old style", 15), bg="lightgray").place(x=280, y=260, width=320)
        text_fullmarks = Entry(self.root, textvariable=self.var_total_marks, font=("goudy old style", 15), bg="lightgray").place(x=280, y=320, width=320)

        self.btn_add = Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add).place(x=280, y=380, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2",command=self.clear).place(x=400, y=380, width=110, height=40)
        
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.label_bg = Label(self.root, image=self.bg_img).place(x=650, y=100)

    def fetch_roll(self):
        conn = sqlite3.connect("RMS.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT roll FROM students")
            rows = cur.fetchall()
            self.roll_list = ['Select']  # Start with 'Select' option
            if rows:
                for row in rows:
                    self.roll_list.append(row[0])
                self.txt_student['values'] = self.roll_list
                self.txt_student.current(0)  # Set combobox to show 'Select'
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            conn.close()

    def search(self):
        con = sqlite3.connect("RMS.db")
        cur = con.cursor()
        try:
            # Fetch the student's name and course based on the roll number
            cur.execute("SELECT name, course FROM students WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                # If a record is found, set the name and course in the form
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def add(self):
        conn = sqlite3.connect("RMS.db")
        cur = conn.cursor()
        try:
            if self.var_roll.get() == "Select" or not self.var_roll.get():
                messagebox.showerror("Error", "Please select a student roll number", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    try:
                        percentage = (int(self.var_marks_obt.get()) / int(self.var_total_marks.get())) * 100
                        cur.execute("INSERT INTO result (roll, name, course, marks_obtained, full_marks, percentage) VALUES (?, ?, ?, ?, ?, ?)", (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks_obt.get(),
                            self.var_total_marks.get(),
                            "{:.2f}".format(percentage)  # Format percentage to two decimal places
                        ))
                        conn.commit()
                        messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                    except ValueError:
                        messagebox.showerror("Error", "Invalid marks entered. Please enter numeric values.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            conn.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_obt.set("")
        self.var_total_marks.set("")
        self.fetch_roll()

if __name__ == "__main__":
    root = Tk()
    obj = Resultclass(root)
    root.mainloop()
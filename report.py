from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class reportclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="View Student Result", font=("goudy old style", 25, "bold"), bg="#FFA500", fg="#262626").place(x=10, y=15, width=1180, height=50)
        # search
        self.var_search = StringVar()
        lbl_select = Label(self.root, text=" Search by Rollno", font=("goudy old style", 15, "bold"), bg="white").place(x=250, y=80)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="lightyellow").place(x=410, y=85)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=620, y=85, width=80, height=28)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2", command=self.clear_fields).place(x=710, y=85, width=80, height=28)

        # Static labels
        Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        Label(self.root, text="Full Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)

        # Dynamic content labels (placeholders for now)
        self.lbl_roll_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_roll_val.place(x=150, y=280, width=150, height=50)
        self.lbl_name_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_name_val.place(x=300, y=280, width=150, height=50)
        self.lbl_course_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_course_val.place(x=450, y=280, width=150, height=50)
        self.lbl_marks_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_marks_val.place(x=600, y=280, width=150, height=50)
        self.lbl_fullmarks_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_fullmarks_val.place(x=750, y=280, width=150, height=50)
        self.lbl_percentage_val = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_percentage_val.place(x=900, y=280, width=150, height=50)

        # Delete button correctly placed in the __init__ method
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.clear_fields)
        btn_delete.place(x=500, y=350, width=80, height=28)

    def search(self):
        con = sqlite3.connect("RMS.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll number required", parent=self.root)
                return
            else:
                # Fetch the student's name and course based on the roll number
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.fullmarks.config(text=row[5])
                    self.percentage.config(text=row[6])
                
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect("RMS.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll number required", parent=self.root)
                return
            else:
                # Fetch the student's name and course based on the roll number
                cur.execute("DELETE FROM result WHERE roll=?", (self.var_search.get(),))
                con.commit()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                self.clear_fields()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear_fields(self):
        self.var_search.set("")
        # Clear dynamic labels
        self.lbl_roll_val.config(text="")
        self.lbl_name_val.config(text="")
        self.lbl_course_val.config(text="")
        self.lbl_marks_val.config(text="")
        self.lbl_fullmarks_val.config(text="")
        self.lbl_percentage_val.config(text="")



if __name__ == "__main__":
    root = Tk()
    obj = reportclass(root)
    root.mainloop()
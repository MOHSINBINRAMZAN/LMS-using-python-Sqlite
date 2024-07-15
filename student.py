import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Create database and table if they don't exist
        self.create_db_table()

        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 25, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # column 1
        lbl_rollno=Label(self.root, text="ROLL NO", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_name=Label(self.root, text="NAME", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_email=Label(self.root, text="EMAIL", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_gender= Label(self.root, text="GENDER", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_state= Label(self.root, text="STATE", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        txt_state=Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="lightgray").place(x=150, y=220, width=150)

        lbl_city= Label(self.root, text="CITY", font=("goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        txt_city=Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg="lightgray").place(x=380, y=220, width=100)

        lbl_pin= Label(self.root, text="PIN", font=("goudy old style", 15, "bold"), bg="white").place(x=490, y=220)
        txt_pin=Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="lightgray").place(x=560, y=220, width=120)

        lbl_address= Label(self.root, text="ADDRESS", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=250)
        
        # Entries
        
        Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightgray").place(x=150, y=60, width=200)

        txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightgray").place(x=150, y=100, width=200)
        txt_email=Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightgray").place(x=150, y=140, width=200)
        self.txt_gender=ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Rather Not Say"),font=("goudy old style", 15), state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        # column 2
        lbl_dob=Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=60)
        lbl_contact=Label(self.root, text="CONTACT", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=100)
        lbl_admission=Label(self.root, text="ADMISSION", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=140)
        lbl_course= Label(self.root, text="COURSE", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=180)

        self.course_list=["Empty"]

        self.txt_dob=Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightgray").place(x=485, y=60, width=200)
        txt_contact=Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightgray").place(x=485, y=100, width=200)
        txt_admission=Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15), bg="lightgray").place(x=485, y=140, width=200)
        self.txt_course=ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,font=("goudy old style", 15), state='readonly',justify=CENTER)
        self.txt_course.place(x=485, y=180, width=200)
        self.txt_course.set("select")

        # Addresses
        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightgray")
        self.txt_address.place(x=150, y=250, width=500, height=100)

        # Buttons
        self.btn_save = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_save.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search
        self.var_search_roll = StringVar()
        lbl_search_roll = Label(self.root, text="Search By | Roll NO", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        text_search_roll = Entry(self.root, textvariable=self.var_search_roll, font=("goudy old style", 15), bg="lightgray").place(x=950, y=60, width=150)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1110, y=60, width=60, height=25)

        # Contents
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        self.course_table = ttk.Treeview(self.C_frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.course_table.heading('roll', text='Roll No')
        self.course_table.heading('name', text='Name')
        self.course_table.heading('email', text='Email')
        self.course_table.heading('gender', text='Gender')
        self.course_table.heading('dob', text='D.O.B')
        self.course_table.heading('contact', text='Contact')
        self.course_table.heading('admission', text='Admission')
        self.course_table.heading('course', text='Course')
        self.course_table.heading('state', text='State')
        self.course_table.heading('city', text='City')
        self.course_table.heading('pin', text='Pin')
        self.course_table.heading('address', text='Address')
        
        self.course_table["show"] = "headings"

        self.course_table.column("roll", width=100)
        self.course_table.column("name", width=100)
        self.course_table.column("email", width=100)
        self.course_table.column("gender", width=100)
        self.course_table.column("dob", width=100)
        self.course_table.column("contact", width=100)
        self.course_table.column("admission", width=100)
        self.course_table.column("course", width=100)
        self.course_table.column("state", width=100)
        self.course_table.column("city", width=100)
        self.course_table.column("pin", width=100)
        self.course_table.column("address", width=150)
        
        self.course_table.pack(fill=BOTH, expand=1)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.course_table.yview)
        scrollx.config(command=self.course_table.xview)
        
        self.show()
        self.fetch_course()

    def create_db_table(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS student (
                        roll TEXT PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        gender TEXT,
                        dob TEXT,
                        contact TEXT,
                        admission TEXT,
                        course TEXT,
                        state TEXT,
                        city TEXT,
                        pin TEXT,
                        address TEXT
                    )""")
        con.commit()
        con.close()

    # Insert Data into DB
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Roll No. already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO student (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END).strip()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Update Data
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Roll No.", parent=self.root)
                else:
                    cur.execute("UPDATE student SET name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? WHERE roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END).strip(),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        self.var_roll.config(state='readonly')
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content['values']
        self.var_roll.set(row[0]),
        self.var_name.set(row[0]),
        self.var_email.set(row[0]),
        self.var_gender.set(row[0]),
        self.var_dob.set(row[0]),
        self.var_contact.set(row[0]),
        self.var_a_date.set(row[0]),
        self.var_course.set(row[0]),
        self.var_state.set(row[0]),
        self.var_city.set(row[0]),
        self.var_pin.set(row[0]),
        self.txt_address.delete('1.0', END).strip()
        self.txt_address.insert(END, row[0])

    # Delete Data
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Roll No.", parent=self.root)
                else:
                    cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Clear Fields
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete('1.0', END)
        self.txt_gender.current(0)
        self.txt_course.current(0)

    # Show Data in Treeview
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM courses")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.course_list.append("Empty")
                for row in rows:
                    self.course_list.append(row[0])
                print(self.course_list)

            else:
                self.course_list.append("Empty")
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Search Data
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_search_roll.get(),))
            row = cur.fetchone()
            if row:
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()

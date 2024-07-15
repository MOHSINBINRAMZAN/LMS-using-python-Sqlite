from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3

class Courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 25, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_course_name = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # Entry Labels
        Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        
        # Entries
        Entry(self.root, textvariable=self.var_course_name, font=("goudy old style", 15), bg="lightgray").place(x=150, y=60, width=200)
        Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15), bg="lightgray").place(x=150, y=100, width=200)
        Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15), bg="lightgray").place(x=150, y=140, width=200)
        
        # Description
        Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        self.txt_description = Text(self.root, font=("goudy old style", 15), bg="lightgray")
        self.txt_description.place(x=150, y=180, width=500, height=100)

        # Buttons
        self.btn_save = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_save.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        self.var_search = StringVar()
        lbl_searc_course_name = Label(self.root, text="Search By | Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        text_seaarch_course_name = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="lightgray").place(x=950, y=60, width=150)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2").place(x=1110, y=60, width=60, height=25)
       
       
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        self.course_table = ttk.Treeview(self.C_frame, columns=("cid", "name", "duration", "charges", "description"))

        self.course_table.heading('cid', text='Course ID')
        self.course_table.heading('name', text='Name')
        self.course_table.heading('duration', text='Duration')
        self.course_table.heading('charges', text='Charges')
        self.course_table.heading('description', text='Description')

        # Correctly setting column widths
        self.course_table.column('cid', width=50)
        self.course_table.column('name', width=100)
        self.course_table.column('duration', width=100)
        self.course_table.column('charges', width=100)
        self.course_table.column('description', width=150)

        self.course_table.pack(fill=BOTH, expand=1)
        self.show()

    def add(self):
        conn = sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            if self.var_course_name.get()=="" or self.var_duration.get()=="" or self.var_charges.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select * from courses where name=? ",(self.var_course_name.get(),)) 
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Course name already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO courses (name, duration, charges, description) values (?,?,?,?)", (
                        self.var_course_name.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0', END)
                    ))

                    conn.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        self.var_course_name.config(state='readonly')
        self.var_course_name
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content['values']
        self.var_course_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.insert('1.0', row[4])

    def update(self):
        conn=sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            if self.var_course_name.get()=="" or self.var_duration.get()=="" or self.var_charges.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select * from courses where name=? ",(self.var_course_name.get(),)) 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid course name", parent=self.root)
                else:
                    cur.execute("update courses set duration=?, charges=?, description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0', END),
                        self.var_course_name.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        conn=sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error", "Course name is required", parent=self.root)
            else:
                cur.execute("select * from courses where name=? ",(self.var_course_name.get(),)) 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid course name", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from courses where name=?",(self.var_course_name.get(),))
                        conn.commit()
                        messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def clear(self):
        self.show()
        self.var_course_name.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)

    def show(self):
        conn=sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            cur.execute("select * from courses")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)
           
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        conn=sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            cur.execute("select * from courses")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('', END, values=row)
           
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            
    def fetch_course(self):
        conn=sqlite3.connect(database="RMS.db")
        cur=conn.cursor()
        try:
            cur.execute("select name from courses")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Courseclass(root)
    root.mainloop()
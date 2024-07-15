import sqlite3 

def create_db():
    conn = sqlite3.connect(database="RMS.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            cid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            duration TEXT, 
            charges TEXT, 
            description TEXT
        )
    """)
    conn.commit()
   # Properly close the connection

    cur.execute("""CREATE TABLE IF NOT EXISTS students (roll INTEGER PRIMARY KEY AUTOINCREMENT, "name", "email", "gender", "dob","contact","admission","course","state","city","pin","address")""")
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT, 
            roll TEXT, 
            name TEXT, 
            course TEXT, 
            marks_obtained TEXT,
            full_marks TEXT,
            percentage TEXT
                
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid INTEGER PRIMARY KEY AUTOINCREMENT, 
            f_name TEXT, 
            l_name TEXT, 
            contact TEXT, 
            email TEXT,
           question TEXT,
            ansswer TEXT,
            password TEXT
                
        )
    """)
    conn.commit()

    conn.close() 
if __name__ == "__main__":
 create_db()
 print("Database and table created successfully.")
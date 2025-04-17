import sqlite3
import os

def create_db():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path)
    db = sqlite3.connect(db_path + './Notes.db')
    
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        summary TEXT NOT NULL,
        category TEXT NOT NULL) ''')
    
    db.commit()
    db.close()

if __name__ == "__main__":
    create_db()
    print("Database created successfully.")
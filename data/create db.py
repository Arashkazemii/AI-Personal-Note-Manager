import sqlite3
import os

def create_db():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path)
    db = sqlite3.connect(db_path + './Notes.db')
    
    cursor = db.cursor()
    
    # Create Notes table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL,
        archived BOOLEAN NOT NULL DEFAULT 0,
        priority TEXT NOT NULL DEFAULT "Medium"
        )''')
    db.commit()
    
    # Create Labels table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Labels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )''')
    db.commit()
    
    # Create NoteLabels table
    cursor.execute('''CREATE TABLE IF NOT EXISTS NoteLabels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note_id INTEGER NOT NULL,
        label_id INTEGER NOT NULL
        )''')
    db.commit()
    
    # Create Tasks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        deadline TIMESTAMP NOT NULL,
        created_at TIMESTAMP NOT NULL
        )''')
    db.commit()
    
    # Create Reminders table
    cursor.execute('''CREATE TABLE IF NOT EXISTS SearchCache (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        result_note_ids TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL
        )''')
    
    db.commit()
    db.close()

if __name__ == "__main__":
    create_db()
    print("Database created successfully.")
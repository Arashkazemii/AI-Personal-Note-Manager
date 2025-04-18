from flask import Flask, request, redirect, url_for, render_template, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path, '../data/Notes.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM Notes ORDER BY created_at DESC LIMIT 6').fetchall()
    conn.close()
    return render_template('home.html', notes=notes)

@app.route('/new_note')
def new_note():
    return render_template('new_note.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    priority = request.form.get('priority')
    labels = request.form.get('labels')
    created_at = updated_at = datetime.now()

    if not title or not content or not priority:
        return "Missing required fields!", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the note
    cursor.execute('''
        INSERT INTO Notes (title, content, created_at, updated_at, priority)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, created_at, updated_at, priority))
    
    note_id = cursor.lastrowid  # آیدی نوت جدید
    
    # Insert labels if provided
    if labels:
        label_list = [label.strip() for label in labels.split(',') if label.strip()]
        for label in label_list:
            cursor.execute('SELECT id FROM Labels WHERE name = ?', (label,))
            label_row = cursor.fetchone()
            if label_row:
                label_id = label_row['id']
            else:
                cursor.execute('INSERT INTO Labels (name) VALUES (?)', (label,))
                label_id = cursor.lastrowid
            cursor.execute('INSERT INTO NoteLabels (note_id, label_id) VALUES (?, ?)', (note_id, label_id))

    conn.commit()
    conn.close()

    return redirect(url_for('home'))

@app.route('/tasks')
def tasks():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()

    todo = [task for task in tasks if task['status'] == 'To Do']
    inprogress = [task for task in tasks if task['status'] == 'In Progress']
    done = [task for task in tasks if task['status'] == 'Done']

    conn.close()
    return render_template('tasks.html', todo=todo, inprogress=inprogress, done=done)

@app.route('/new_task')
def new_task():
    return render_template('new_task.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')
    deadline = request.form.get('deadline')

    if not title or not priority:
        return "Title and Priority are required!", 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Tasks (title, description, priority, deadline, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, description, priority, deadline, 'To Do', datetime.now()))

    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        deadline = request.form.get('deadline')

        cursor.execute('''
            UPDATE Tasks
            SET title = ?, description = ?, priority = ?, deadline = ?
            WHERE id = ?
        ''', (title, description, priority, deadline, task_id))

        conn.commit()
        conn.close()
        return redirect(url_for('tasks'))
    else:
        cursor.execute('SELECT * FROM Tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        conn.close()
        return render_template('edit_task.html', task=task)

@app.route('/update_task_status', methods=['POST'])
def update_task_status():
    data = request.get_json()
    task_id = data['task_id']
    new_status = data['status']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE Tasks
        SET status = ?
        WHERE id = ?
    ''', (new_status, task_id))

    conn.commit()
    conn.close()

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)

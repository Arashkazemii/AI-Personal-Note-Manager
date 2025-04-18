# Note AI Assistant

Welcome to **Note AI Assistant** – your personal smart note and task manager, powered by cutting-edge AI!

---

## ✨ Features

- 📝 **Create and Manage Notes**  
  Easily create, label, prioritize, and organize your notes.

- ✅ **Task Manager with Kanban Board**  
  Visualize your tasks in a clean drag & drop Kanban board.

- 🔥 **AI Suggestions** (powered by Llama3.1-8B)  
  Get smart suggestions and summaries for your notes and tasks.

- 🛠️ **Priority Tagging**  
  High, Medium, Low priority for tasks.

- 🗓️ **Deadline and Reminders**  
  Set due dates for tasks.

- 🖋️ **Markdown Support (upcoming)**  
  Format your notes beautifully.

- 📄 **Export Notes** (upcoming)  
  Export your notes as PDF or Markdown files.

- 🔍 **Smart Search** (upcoming)  
  Search your notes and tasks using natural language powered by AI.

---

## 🚀 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite
- **AI Integration:** Ollama (running Llama3.1-8B model locally)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/Arashkazemii/AI-Personal-Note-Manager.git
cd AI-Personal-Note-Manager
```

2. Install Python packages:

```bash
pip install flask
```

3. Setup the database:

```bash
python create_db.py
```

4. (Optional) Install and run [Ollama](https://ollama.com) and download the `llama3:8b` model.

```bash
ollama run llama3
```

5. Start the server:

```bash
python app.py
```

6. Visit `http://127.0.0.1:5000/` to use the app!

---

## ⚙️ Project Structure

```
/AI-Personal-Note-Manager
│
├── app.py           # Main Flask server
├── create_db.py     # Database setup script
├── templates/
│   ├── home.html
│   ├── new_note.html
│   ├── new_task.html
│   ├── edit_task.html
│   ├── tasks.html
│
├── static/
│   ├── styles/
│   └── scripts/
│
└── README.md        # You are here 😉
```

---

## 🤖 AI Integration

- Uses **Ollama API** at `localhost:11434`
- Sends note/task content to `llama3.1-8b`
- Receives intelligent suggestions/summaries
- Shows output on the UI in a beautiful way

---

## ✍️ Author

Developed with 💙 by [Arash Kazemi](https://github.com/Arashkazemii)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> "Notes are no longer boring. Notes are evolving." 🚀  
> — **Note AI Assistant**
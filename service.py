import sqlite3

DATABASE_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return tasks


def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    conn.close()
    return dict(row) if row else None


def create_task(title, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (title, description)
    )

    conn.commit()

    task_id = cursor.lastrowid

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = dict(cursor.fetchone())

    conn.close()
    return task


def update_task(task_id, title=None, description=None, completed=None):
    conn = get_connection()
    cursor = conn.cursor()

    task = get_task_by_id(task_id)
    if not task:
        return None

    title = title if title is not None else task["title"]
    description = description if description is not None else task["description"]
    completed = completed if completed is not None else task["completed"]

    cursor.execute(
        "UPDATE tasks SET title=?, description=?, completed=? WHERE id=?",
        (title, description, completed, task_id)
    )

    conn.commit()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    updated = dict(cursor.fetchone())

    conn.close()
    return updated


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    conn.close()
    return True
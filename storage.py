import storage


def get_all_tasks():
    return storage.get_all_tasks()


def get_task_by_id(task_id):
    return storage.get_task_by_id(task_id)


def create_task(title, description):
    if not title:
        return None, "Title is required"

    task = storage.create_task(title, description)
    return task, None


def update_task(task_id, title=None, description=None, completed=None):
    task = storage.update_task(task_id, title, description, completed)

    if task is None:
        return None, "Task not found"

    return task, None


def delete_task(task_id):
    task = storage.delete_task(task_id)

    if task is None:
        return None, "Task not found"

    return task, None


def complete_task(task_id):
    task = storage.update_task(task_id, completed=1)

    if task is None:
        return None, "Task not found"

    return task, None
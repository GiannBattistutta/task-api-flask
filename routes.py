from flask import Blueprint, jsonify, request
import service

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = service.get_all_tasks()
    return jsonify(tasks), 200


@tasks_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = service.get_task_by_id(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    description = data.get("description", "")

    if title is None or not title.strip():
        return jsonify({"error": "Title is required"}), 400

    title = title.strip()
    description = description.strip() if description else ""

    task, error = service.create_task(title, description)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(task), 201


@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    description = data.get("description")
    completed = data.get("completed")

    if title is not None:
        title = title.strip()

        if not title:
            return jsonify({"error": "Title cannot be empty"}), 400

    if description is not None:
        description = description.strip()

    if completed is not None and not isinstance(completed, bool):
        return jsonify({"error": "Completed must be true or false"}), 400

    task, error = service.update_task(
        task_id=task_id,
        title=title,
        description=description,
        completed=completed
    )

    if error:
        return jsonify({"error": error}), 404

    return jsonify(task), 200


@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task, error = service.delete_task(task_id)

    if error:
        return jsonify({"error": error}), 404

    return jsonify({
        "message": "Task deleted successfully",
        "deleted_task": task
    }), 200


@tasks_bp.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    task, error = service.update_task(task_id, completed=True)

    if error:
        return jsonify({"error": error}), 404

    return jsonify(task), 200
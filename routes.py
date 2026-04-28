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
    description = data.get("description")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = service.create_task(title, description)

    return jsonify(task), 201


@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    description = data.get("description")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = service.update_task(task_id, title, description)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = service.get_task_by_id(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    service.delete_task(task_id)

    return jsonify({"message": "Task deleted successfully"}), 200


@tasks_bp.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    task = service.update_task(task_id, completed=True)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200
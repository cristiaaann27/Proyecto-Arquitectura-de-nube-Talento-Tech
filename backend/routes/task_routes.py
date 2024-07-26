from flask import Blueprint, request, jsonify

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    # Logic to create a task
    return jsonify({'message': 'Task created'})

@task_routes.route('/tasks', methods=['GET'])
def list_tasks():
    # Logic to list tasks
    return jsonify({'tasks': []})

@task_routes.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    # Logic to update a task
    return jsonify({'message': 'Task updated'})

@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Logic to delete a task
    return jsonify({'message': 'Task deleted'})


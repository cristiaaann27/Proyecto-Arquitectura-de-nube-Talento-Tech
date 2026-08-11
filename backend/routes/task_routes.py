from flask import Blueprint, current_app, jsonify, request

from services.exceptions import TaskNotFoundError, TaskValidationError

task_routes = Blueprint('task_routes', __name__)


def _task_service():
    return current_app.extensions['task_service']


@task_routes.route('/tasks', methods=['POST'])
def create_task():
    payload = request.get_json(silent=True) or {}
    try:
        task = _task_service().create_task(
            name=payload.get('name'), due_date=payload.get('due_date')
        )
    except TaskValidationError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify(task.to_dict()), 201


@task_routes.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = _task_service().list_tasks()
    return jsonify({'tasks': [task.to_dict() for task in tasks]})


@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    payload = request.get_json(silent=True) or {}
    fields = {key: payload[key] for key in ('name', 'due_date') if key in payload}
    try:
        task = _task_service().update_task(task_id, **fields)
    except TaskValidationError as exc:
        return jsonify({'error': str(exc)}), 400
    except TaskNotFoundError as exc:
        return jsonify({'error': str(exc)}), 404
    return jsonify(task.to_dict())


@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        _task_service().delete_task(task_id)
    except TaskNotFoundError as exc:
        return jsonify({'error': str(exc)}), 404
    return jsonify({'message': 'Tarea eliminada'})

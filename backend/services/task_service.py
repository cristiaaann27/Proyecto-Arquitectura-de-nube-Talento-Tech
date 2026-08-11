from datetime import date

from services.exceptions import TaskNotFoundError, TaskValidationError


class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, name, due_date=None):
        name = (name or '').strip()
        if not name:
            raise TaskValidationError('El nombre de la tarea no puede estar vacío')

        parsed_due_date = self._parse_due_date(due_date)
        return self.repository.add(name=name, due_date=parsed_due_date)

    def get_task(self, task_id):
        task = self.repository.get(task_id)
        if task is None:
            raise TaskNotFoundError(f'Tarea {task_id} no encontrada')
        return task

    def get_task_by_name(self, name):
        name = (name or '').strip().lower()
        for task in self.repository.list_all():
            if task.name.strip().lower() == name:
                return task
        return None

    def list_tasks(self):
        return self.repository.list_all()

    def update_task(self, task_id, **fields):
        if 'name' in fields:
            fields['name'] = (fields['name'] or '').strip()
            if not fields['name']:
                raise TaskValidationError('El nombre de la tarea no puede estar vacío')
        if 'due_date' in fields:
            fields['due_date'] = self._parse_due_date(fields['due_date'])

        task = self.repository.update(task_id, **fields)
        if task is None:
            raise TaskNotFoundError(f'Tarea {task_id} no encontrada')
        return task

    def delete_task(self, task_id):
        deleted = self.repository.delete(task_id)
        if not deleted:
            raise TaskNotFoundError(f'Tarea {task_id} no encontrada')

    @staticmethod
    def _parse_due_date(due_date):
        if due_date in (None, ''):
            return None
        if isinstance(due_date, date):
            return due_date
        try:
            return date.fromisoformat(due_date)
        except (TypeError, ValueError):
            raise TaskValidationError('due_date debe tener formato ISO (YYYY-MM-DD)')

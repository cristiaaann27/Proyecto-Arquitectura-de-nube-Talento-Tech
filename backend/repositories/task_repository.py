import abc

from extensions import db
from models.task import Task


class TaskRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, name, due_date=None):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, task_id):
        raise NotImplementedError

    @abc.abstractmethod
    def list_all(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, task_id, **fields):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, task_id):
        raise NotImplementedError


class SQLAlchemyTaskRepository(TaskRepository):
    def add(self, name, due_date=None):
        task = Task(name=name, due_date=due_date)
        db.session.add(task)
        db.session.commit()
        return task

    def get(self, task_id):
        return db.session.get(Task, task_id)

    def list_all(self):
        return Task.query.order_by(Task.id).all()

    def update(self, task_id, **fields):
        task = self.get(task_id)
        if task is None:
            return None
        for key, value in fields.items():
            setattr(task, key, value)
        db.session.commit()
        return task

    def delete(self, task_id):
        task = self.get(task_id)
        if task is None:
            return False
        db.session.delete(task)
        db.session.commit()
        return True

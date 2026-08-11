import pytest

from repositories.task_repository import SQLAlchemyTaskRepository
from services.exceptions import TaskNotFoundError, TaskValidationError
from services.task_service import TaskService


@pytest.fixture
def task_service(app):
    return TaskService(SQLAlchemyTaskRepository())


def test_create_task_persists_and_returns_task(task_service):
    task = task_service.create_task(name='Comprar leche', due_date='2026-08-15')

    assert task.id is not None
    stored = [t.name for t in task_service.list_tasks()]
    assert 'Comprar leche' in stored


def test_create_task_without_name_raises(task_service):
    with pytest.raises(TaskValidationError):
        task_service.create_task(name='   ')


def test_update_task_changes_fields(task_service):
    task = task_service.create_task(name='Lavar el auto')

    updated = task_service.update_task(task.id, name='Lavar el auto rojo')

    assert updated.name == 'Lavar el auto rojo'


def test_update_task_missing_raises_not_found(task_service):
    with pytest.raises(TaskNotFoundError):
        task_service.update_task(999, name='no existe')


def test_delete_task_removes_it(task_service):
    task = task_service.create_task(name='Tarea temporal')

    task_service.delete_task(task.id)

    assert task_service.repository.get(task.id) is None


def test_get_task_by_name_is_case_insensitive(task_service):
    task_service.create_task(name='Pagar factura')

    found = task_service.get_task_by_name('pagar FACTURA')

    assert found is not None
    assert found.name == 'Pagar factura'

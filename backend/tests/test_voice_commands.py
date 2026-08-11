import pytest

from commands.voice_commands import VoiceCommandRegistry
from repositories.task_repository import SQLAlchemyTaskRepository
from services.task_service import TaskService


@pytest.fixture
def task_service(app):
    return TaskService(SQLAlchemyTaskRepository())


@pytest.fixture
def registry():
    return VoiceCommandRegistry()


def test_crear_tarea_command_creates_task(registry, task_service):
    message = registry.dispatch('crear tarea comprar pan', task_service)

    assert 'comprar pan' in message
    assert task_service.get_task_by_name('comprar pan') is not None


def test_listar_tarea_command_reports_empty(registry, task_service):
    message = registry.dispatch('listar tarea', task_service)

    assert message == 'No tienes tareas'


def test_borrar_tarea_command_deletes_existing_task(registry, task_service):
    task_service.create_task(name='comprar pan')

    message = registry.dispatch('borrar tarea comprar pan', task_service)

    assert 'borrada' in message
    assert task_service.get_task_by_name('comprar pan') is None


def test_actualizar_tarea_command_renames_task(registry, task_service):
    task_service.create_task(name='comprar pan')

    message = registry.dispatch('actualizar tarea comprar pan a comprar leche', task_service)

    assert 'actualizada' in message
    assert task_service.get_task_by_name('comprar leche') is not None


def test_registry_falls_back_to_unrecognized(registry, task_service):
    message = registry.dispatch('hacer una pirueta', task_service)

    assert message == 'Comando no reconocido'

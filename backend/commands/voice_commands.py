import abc

from services.exceptions import TaskNotFoundError, TaskValidationError


class VoiceCommand(abc.ABC):
    @abc.abstractmethod
    def matches(self, text):
        raise NotImplementedError

    @abc.abstractmethod
    def execute(self, text, task_service):
        raise NotImplementedError


class CrearTareaCommand(VoiceCommand):
    KEYWORD = 'crear tarea'

    def matches(self, text):
        return self.KEYWORD in text

    def execute(self, text, task_service):
        name = text.split(self.KEYWORD, 1)[1].strip()
        try:
            task = task_service.create_task(name=name)
        except TaskValidationError:
            return 'Di el nombre de la tarea después de "crear tarea"'
        return f'Tarea "{task.name}" creada'


class ListarTareaCommand(VoiceCommand):
    KEYWORD = 'listar tarea'

    def matches(self, text):
        return self.KEYWORD in text

    def execute(self, text, task_service):
        tasks = task_service.list_tasks()
        if not tasks:
            return 'No tienes tareas'
        names = ', '.join(task.name for task in tasks)
        return f'Tus tareas son: {names}'


class ActualizarTareaCommand(VoiceCommand):
    KEYWORD = 'actualizar tarea'

    def matches(self, text):
        return self.KEYWORD in text

    def execute(self, text, task_service):
        remainder = text.split(self.KEYWORD, 1)[1].strip()
        if ' a ' not in remainder:
            return 'Di el comando así: "actualizar tarea <nombre actual> a <nombre nuevo>"'

        current_name, new_name = remainder.split(' a ', 1)
        current_name = current_name.strip()
        new_name = new_name.strip()

        task = task_service.get_task_by_name(current_name)
        if task is None:
            return f'No encontré una tarea llamada "{current_name}"'

        try:
            task_service.update_task(task.id, name=new_name)
        except (TaskValidationError, TaskNotFoundError):
            return f'No pude actualizar la tarea "{current_name}"'
        return f'Tarea "{current_name}" actualizada a "{new_name}"'


class BorrarTareaCommand(VoiceCommand):
    KEYWORD = 'borrar tarea'

    def matches(self, text):
        return self.KEYWORD in text

    def execute(self, text, task_service):
        name = text.split(self.KEYWORD, 1)[1].strip()
        task = task_service.get_task_by_name(name)
        if task is None:
            return f'No encontré una tarea llamada "{name}"'

        task_service.delete_task(task.id)
        return f'Tarea "{name}" borrada'


class VoiceCommandRegistry:
    def __init__(self, commands=None):
        self.commands = commands if commands is not None else [
            CrearTareaCommand(),
            ListarTareaCommand(),
            ActualizarTareaCommand(),
            BorrarTareaCommand(),
        ]

    def dispatch(self, text, task_service):
        for command in self.commands:
            if command.matches(text):
                return command.execute(text, task_service)
        return 'Comando no reconocido'

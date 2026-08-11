import pytest

import azure.cognitiveservices.speech as speech_sdk

from commands.voice_commands import VoiceCommandRegistry
from repositories.task_repository import SQLAlchemyTaskRepository
from services.task_service import TaskService
from services.voice_command_service import VoiceCommandService


class FakeRecognitionResult:
    def __init__(self, reason, text=''):
        self.reason = reason
        self.text = text


class FakeRecognizer:
    def __init__(self, result):
        self._result = result

    def recognize_once(self):
        return self._result


class FakeSpeechProvider:
    def __init__(self, result):
        self._recognizer = FakeRecognizer(result)

    def get_recognizer(self):
        return self._recognizer


@pytest.fixture
def task_service(app):
    return TaskService(SQLAlchemyTaskRepository())


def test_handle_voice_command_dispatches_recognized_speech(task_service):
    result = FakeRecognitionResult(speech_sdk.ResultReason.RecognizedSpeech, 'crear tarea comprar pan')
    service = VoiceCommandService(task_service, FakeSpeechProvider(result), VoiceCommandRegistry())

    message = service.handle_voice_command()

    assert 'comprar pan' in message
    assert task_service.get_task_by_name('comprar pan') is not None


def test_handle_voice_command_reports_no_speech_recognized(task_service):
    result = FakeRecognitionResult(speech_sdk.ResultReason.NoMatch)
    service = VoiceCommandService(task_service, FakeSpeechProvider(result), VoiceCommandRegistry())

    message = service.handle_voice_command()

    assert message == 'No se reconoció ningún comando'

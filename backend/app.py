from flask import Flask
from flask_cors import CORS

from commands.voice_commands import VoiceCommandRegistry
from config import Config
from extensions import db
from repositories.task_repository import SQLAlchemyTaskRepository
from routes.task_routes import task_routes
from routes.voice_routes import voice_routes
from services.speech_provider import SpeechRecognizerProvider
from services.task_service import TaskService
from services.voice_command_service import VoiceCommandService


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)

    task_service = TaskService(SQLAlchemyTaskRepository())
    speech_provider = SpeechRecognizerProvider(
        speech_key=app.config['SPEECH_KEY'],
        speech_region=app.config['SPEECH_REGION'],
        language=app.config['SPEECH_LANGUAGE'],
    )
    voice_command_service = VoiceCommandService(
        task_service=task_service,
        speech_provider=speech_provider,
        command_registry=VoiceCommandRegistry(),
    )

    app.extensions['task_service'] = task_service
    app.extensions['voice_command_service'] = voice_command_service

    app.register_blueprint(task_routes)
    app.register_blueprint(voice_routes)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)

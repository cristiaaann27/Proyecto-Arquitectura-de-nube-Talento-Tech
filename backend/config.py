import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tasks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SPEECH_KEY = os.getenv('SPEECH_KEY')
    SPEECH_REGION = os.getenv('SPEECH_REGION')
    SPEECH_LANGUAGE = os.getenv('SPEECH_LANGUAGE', 'es-ES')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

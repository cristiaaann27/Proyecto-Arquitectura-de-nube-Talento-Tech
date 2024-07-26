from flask import Blueprint, request, jsonify
import azure.cognitiveservices.speech as speech_sdk
from dotenv import load_dotenv
import os

# Initialize the Blueprint
voice_routes = Blueprint('voice_routes', __name__)

# Load environment variables
load_dotenv()
SPEECH_KEY = os.getenv('SPEECH_KEY')
SPEECH_REGION = os.getenv('SPEECH_REGION')

# Configure speech service
speech_config = speech_sdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config)

@voice_routes.route('/voice-command', methods=['POST'])
def process_voice_command():
    try:
        # Record and transcribe voice command
        result = speech_recognizer.recognize_once()
        if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
            voice_command = result.text
            print("Recognized command:", voice_command)
        else:
            return jsonify({'message': 'No command recognized'}), 400

        # Process the transcribed text
        response_message = process_command(voice_command)

        return jsonify({'message': response_message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_command(command):
    command = command.lower()
    if 'create task' in command:
        return 'Task created'
    elif 'list tasks' in command:
        return 'Here are your tasks'
    elif 'update task' in command:
        return 'Task updated'
    elif 'delete task' in command:
        return 'Task deleted'
    else:
        return 'Command not recognized'

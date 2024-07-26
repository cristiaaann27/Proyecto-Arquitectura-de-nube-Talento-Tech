from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()
SPEECH_KEY = os.getenv('SPEECH_KEY')
SPEECH_REGION = os.getenv('SPEECH_REGION')

# Configure speech service
speech_config = speech_sdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
speech_config.speech_recognition_language = "es-ES"
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config)

# Endpoint for voice command processing
@app.route('/voice-command', methods=['POST'])
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
    if 'crear tarea' in command:
        return 'Task created'
    elif 'listar tarea' in command:
        return 'Here are your tasks'
    elif 'actualizar tarea' in command:
        return 'Task updated'
    elif 'borrar tarea' in command:
        return 'Task deleted'
    else:
        return 'Command not recognized'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Blueprint, current_app, jsonify

voice_routes = Blueprint('voice_routes', __name__)


@voice_routes.route('/voice-command', methods=['POST'])
def process_voice_command():
    voice_command_service = current_app.extensions['voice_command_service']
    message = voice_command_service.handle_voice_command()
    return jsonify({'message': message})

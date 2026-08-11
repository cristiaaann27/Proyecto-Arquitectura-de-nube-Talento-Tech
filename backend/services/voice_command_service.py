import azure.cognitiveservices.speech as speech_sdk


class VoiceCommandService:
    def __init__(self, task_service, speech_provider, command_registry):
        self.task_service = task_service
        self.speech_provider = speech_provider
        self.command_registry = command_registry

    def handle_voice_command(self):
        try:
            recognizer = self.speech_provider.get_recognizer()
            result = recognizer.recognize_once()

            if result.reason != speech_sdk.ResultReason.RecognizedSpeech:
                return 'No se reconoció ningún comando'

            text = result.text.lower()
            return self.command_registry.dispatch(text, self.task_service)
        except Exception as exc:
            return f'Error al procesar el comando de voz: {exc}'

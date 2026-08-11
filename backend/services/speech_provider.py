import azure.cognitiveservices.speech as speech_sdk


class SpeechRecognizerProvider:
    def __init__(self, speech_key, speech_region, language):
        self.speech_key = speech_key
        self.speech_region = speech_region
        self.language = language
        self._speech_config = None

    def _get_speech_config(self):
        if self._speech_config is None:
            self._speech_config = speech_sdk.SpeechConfig(
                subscription=self.speech_key, region=self.speech_region
            )
            self._speech_config.speech_recognition_language = self.language
        return self._speech_config

    def get_recognizer(self):
        return speech_sdk.SpeechRecognizer(speech_config=self._get_speech_config())

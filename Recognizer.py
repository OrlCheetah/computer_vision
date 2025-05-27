import threading
import speech_recognition as sr

class Recognizer:
    """
    Classe pour la reconnaissance vocale.
    Utilise la bibliothèque SpeechRecognition pour écouter et traiter la voix.
    """
    def __init__(self):
        self.is_listening = False

    def listen_and_process(self, on_text_callback):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone(2)
        recognizer.energy_threshold = 400
        recognizer.dynamic_energy_threshold = False

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Prêt à écouter...")

            while self.is_listening:
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    print("Reconnaissance vocale en cours...")
                    text = recognizer.recognize_google(audio, language="fr-FR")
                    print(f"Texte reconnu : {text}")
                    on_text_callback(text)

                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    print("Je n'ai pas compris, réessayez.")
                except sr.RequestError as e:
                    print(f"Erreur Google Speech: {e}")
                    break

        print("Reconnaissance vocale arrêtée.")

    def start_google_voice_recognition(self, on_text_callback):
        self.is_listening = True
        thread = threading.Thread(target=self.listen_and_process, args=(on_text_callback,))
        thread.daemon = True
        thread.start()

    def stop_google_voice_recognition(self):
        self.is_listening = False

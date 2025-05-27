import tkinter as tk
from tkinter import messagebox, filedialog

from Executor import Executor
from NLP import Nlp_model
from outils import set_app_path
from Recognizer import Recognizer

class Orl_GUI:
    """
    Classe principale de l'interface graphique pour OrlVoice.
    Permet à l'utilisateur de choisir entre la reconnaissance vocale et la saisie texte.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OrlVoice Interface")
        self.root.geometry("400x300")
        self.voice_enabled = tk.BooleanVar(value=True)
        self.setup_ui()

        self.nlp = Nlp_model()
        self.executor = Executor()

    def setup_ui(self):
        label = tk.Label(self.root, text="Choisissez votre mode de commande:", font=("Arial", 12))
        label.pack(pady=10)

        voice_toggle = tk.Checkbutton(self.root, text="Activer le mode vocal", variable=self.voice_enabled)
        voice_toggle.pack(pady=5)

        voice_button = tk.Button(self.root, text="Parler", command=self.on_voice_command, width=25)
        voice_button.pack(pady=5)

        tk.Label(self.root, text="Ou écrivez votre commande:").pack(pady=5)

        self.text_entry = tk.Entry(self.root, width=40)
        self.text_entry.pack(pady=5)

        text_button = tk.Button(self.root, text="Envoyer", command=self.on_text_command, width=25)
        text_button.pack(pady=5)

    def on_voice_command(self):
        rec = Recognizer()
        if self.voice_enabled.get():
            rec.start_google_voice_recognition(self.on_text_recognized)
            messagebox.showinfo("OrlVoice", "Reconnaissance vocale activée. Parlez !")
        else:
            rec.stop_google_voice_recognition()
            messagebox.showinfo("OrlVoice", "Reconnaissance vocale désactivée.")

    def on_text_command(self):
        user_input = self.text_entry.get()
        if user_input.strip():
            self.on_text_recognized(user_input.strip())
        else:
            messagebox.showwarning("OrlVoice", "Veuillez entrer une commande texte.")

    def on_text_recognized(self, text):
        text = text.lower()
        print(f"Commande reçue : {text}")
        action = self.nlp.predict_intent(text)
        self.executor.execute_action(action=action, text=text)
    def run(self):
        self.root.mainloop()

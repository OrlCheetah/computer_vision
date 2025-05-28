import tkinter as tk
from tkinter import messagebox

from Executor import Executor
from NLP import Nlp_model
from Recognizer import Recognizer

class Orl_GUI:
    """
    Interface graphique principale d'OrlVoice.
    Choix entre commande vocale et saisie texte, avec retour utilisateur.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OrlVoice Interface")
        self.root.geometry("460x350")
        self.root.resizable(False, False)

        self.voice_enabled = tk.BooleanVar(value=True)
        self.nlp = Nlp_model()
        self.executor = Executor()

        self.setup_ui()
        self.recognizer = Recognizer()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title = tk.Label(main_frame, text="OrlVoice Commande", font=("Arial", 14, "bold"))
        title.pack(pady=(0,15))

        voice_toggle = tk.Checkbutton(main_frame, text="Activer le mode vocal", variable=self.voice_enabled,
                                      font=("Arial", 11))
        voice_toggle.pack(anchor="w", pady=(0,10))

        self.voice_button = tk.Button(main_frame, text="🎤 Parler", command=self.on_voice_command,
                                      width=25, font=("Arial", 11), bg="#4CAF50", fg="white",
                                      activebackground="#45a049", relief="raised")
        self.voice_button.pack(pady=(0,15))

        text_label = tk.Label(main_frame, text="Ou écrivez votre commande :", font=("Arial", 12))
        text_label.pack(anchor="w")

        self.text_entry = tk.Entry(main_frame, width=40, font=("Arial", 11))
        self.text_entry.pack(pady=(5,10))
        self.text_entry.bind("<Return>", lambda e: self.on_text_command())

        self.text_button = tk.Button(main_frame, text="Envoyer", command=self.on_text_command,
                                     width=25, font=("Arial", 11), bg="#2196F3", fg="white",
                                     activebackground="#1e88e5", relief="raised")
        self.text_button.pack(pady=(0,15))

        self.status_label = tk.Label(main_frame, text="", font=("Arial", 10), fg="gray")
        self.status_label.pack()

    def on_voice_command(self):
        if self.voice_enabled.get():
            self.status_label.config(text="Reconnaissance vocale activée.\n"
                                          "Remarquez que votre micro s'active à chaque fois qu'un "
                                          "son est détecté. \nParlez...")
            try:
                self.recognizer.start_google_voice_recognition(self.on_text_recognized)
                messagebox.showinfo("OrlVoice", "transcripteur vocal activé !")
            except Exception as e:
                messagebox.showerror("OrlVoice", f"Erreur démarrage reconnaissance vocale :\n{e}")
                self.status_label.config(text="Erreur de reconnaissance vocale")
        else:
            try:
                self.recognizer.stop_google_voice_recognition()
                messagebox.showinfo("OrlVoice", "Reconnaissance vocale désactivée.")
                self.status_label.config(text="Reconnaissance vocale désactivée.")
            except Exception as e:
                messagebox.showerror("OrlVoice", f"Erreur arrêt reconnaissance vocale :\n{e}")
                self.status_label.config(text="Erreur lors de la désactivation")

    def on_text_command(self):
        user_input = self.text_entry.get().strip()
        if user_input:
            self.on_text_recognized(user_input)
            self.text_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("OrlVoice", "Veuillez entrer une commande texte.")

    def on_text_recognized(self, text):
        text = text.lower()
        self.status_label.config(text=f"Commande reçue : {text}")
        print(f"Commande reçue : {text}")
        try:
            action = self.nlp.predict_intent(text)
            self.executor.execute_action(action=action, text=text)
        except Exception as e:
            messagebox.showerror("OrlVoice", f"Erreur lors de l'exécution de la commande :\n{e}")
            self.status_label.config(text="Erreur exécution commande")

    def run(self):
        self.root.mainloop()


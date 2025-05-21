import os
import re
import subprocess
from tkinter import messagebox, filedialog

import pyautogui
from outils.app_path_config import set_app_path, get_app_path

class Executor:
    def __init__(self):
        pass

    @staticmethod
    def execute_action(action: str, slot: str = ):
        liste0 = ["ouvrir", "ouvres", "ouvert", "lancer", "lances", "lance", "demarrer", "demarres"
                  , "demarer", "demare", "demares", "démarrer", "démarer", "démares", "démarré", "démarrez",
                  "demarrez"]
        liste1 = ["fermer", "ferme", "quitter", "quitte", "fermes", "quittes", "arreter", "arretes"
                  , "arrete", "fermez", "quittez", "arretez", "arreté", "quitté", "fermé", "kiter",
                  "former"]
        try:
            action = action.lower()

            def open_app(app_name, friendly_name=None):
                path = get_app_path(app_name)
                if not path or not os.path.exists(path):
                    friendly_name = friendly_name or app_name
                    messagebox.showinfo("Orl", f"Veuillez sélectionner l’exécutable de {friendly_name}.")
                    path = filedialog.askopenfilename(title=f"Choisir {friendly_name}", filetypes=[("Fichiers EXE", "*.exe")])
                    if path:
                        set_app_path(app_name, path)
                if path:
                    subprocess.Popen(path)

                for st in liste0:
                    if action.startswith("ouvrir "):
                        app = action.replace("ouvrir ", "").strip()
                        open_app(app, friendly_name=app)

            elif action == "clic gauche":
                pyautogui.click()
            elif action == "double clic":
                pyautogui.doubleClick()
            elif action == "clic droit":
                pyautogui.rightClick()

            elif action.startswith("déplace la souris"):
                pattern = r"vers (\w+)(?: de (\d+))?"
                match = re.search(pattern, action)
                dx, dy = 0, 0
                if match:
                    direction = match.group(1)
                    distance = int(match.group(2)) if match.group(2) else 100
                    if direction == "gauche":
                        dx = -distance
                    elif direction == "droite":
                        dx = distance
                    elif direction == "haut":
                        dy = -distance
                    elif direction == "bas":
                        dy = distance
                pyautogui.moveRel(dx, dy, duration=0.5)

            elif action == "scroll haut":
                pyautogui.scroll(500)
            elif action == "scroll bas":
                pyautogui.scroll(-500)
            elif action == "scroll gauche":
                pyautogui.hscroll(-500)
            elif action == "scroll droite":
                pyautogui.hscroll(500)

            elif action.startswith("tape ") or action.startswith("écris ") or action.startswith("écrit "):
                text = action.split(" ", 1)[1]
                pyautogui.write(text)

            else:
                messagebox.showwarning("Orl", f"Action inconnue: {action}")

        except Exception as e:
            print("Erreur execution action: ", e)

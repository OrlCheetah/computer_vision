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
    def execute_action(action: str = "", text: str | None = None):
        """Exécute une action basée sur la commande vocale ou textuelle fournie.
       Args:
           action (str): La commande à exécuter.
           text (str | None): Texte supplémentaire pour la commande ecrire.
        """
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
                    messagebox.showinfo("Orl", f"{app_name} a été ouvert avec succès.")
            
            def close_app(app_name, friendly_name=None):
                friendly_name = friendly_name or app_name
                try:
                    result = subprocess.run(
                        ["taskkill", "/f", "/im", app_name],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    if result.returncode == 0:
                        messagebox.showinfo("Orl", f"{friendly_name} a été fermé avec succès.")
                    else:
                        messagebox.showwarning("Orl", f"Impossible de fermer {friendly_name}.\n{result.stderr.strip()}")
                except Exception as e:
                    messagebox.showerror("Orl", f"Erreur lors de la fermeture de {friendly_name} : {str(e)}")

            if action == "clic gauche":
                pyautogui.click()
            elif action == "double clic":
                pyautogui.doubleClick()
            elif action == "clic droit":
                pyautogui.rightClick()

            elif action.startswith("deplacer_", ""):
                pattern = r"deplacer_souris:(\w+)_(\d+)"
                match = re.match(pattern, action)
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
            elif action.startswith("déplacer souris"):
                pyautogui.moveTo(40, 40, duration=0.5)
            elif action == "scroll haut":
                pyautogui.scroll(500)
            elif action == "scroll bas":
                pyautogui.scroll(-500)
            elif action == "scroll gauche":
                pyautogui.hscroll(-500)
            elif action == "scroll droite":
                pyautogui.hscroll(500)
            if text is not None:
                text = text.split(" ", 1)[1]
                pyautogui.write(text)

            else:
                messagebox.showwarning("Orl", f"Action inconnue: {action}")

        except Exception as e:
            print("Erreur execution action: ", e)

    
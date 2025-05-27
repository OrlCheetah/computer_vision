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
    def execute_action(action: str, text: str | None = None):
        """Exécute une action basée sur la commande vocale ou textuelle fournie.
       Args:
           action (str): La commande à exécuter.
           text (str | None): Texte supplémentaire pour la commande ecrire.
        """
        try:
            print(action)
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
                process_map = {
                    "google chrome": "chrome.exe",
                    "chrome": "chrome.exe",
                    "mozilla firefox": "firefox.exe",
                    "firefox": "firefox.exe",
                    "edge": "msedge.exe",
                    "microsoft edge": "msedge.exe",
                    "opera": "opera.exe",
                    "brave": "brave.exe",
                    "notepad": "notepad.exe",
                    "bloc-notes": "notepad.exe",
                    "word": "WINWORD.EXE",
                    "excel": "EXCEL.EXE",
                    "powerpoint": "POWERPNT.EXE",
                    "outlook": "OUTLOOK.EXE",
                    "teams": "Teams.exe",
                    "vlc": "vlc.exe",
                    "spotify": "Spotify.exe",
                    "discord": "Discord.exe",
                    "steam": "steam.exe",
                    "skype": "Skype.exe",
                    "visual studio": "devenv.exe",
                    "vs code": "Code.exe",
                    "vscode": "Code.exe",
                    "android studio": "studio64.exe",
                    "pycharm": "pycharm64.exe",
                    "intellij": "idea64.exe",
                    "explorateur de fichiers": "explorer.exe",
                    "explorer": "explorer.exe",
                    "calculatrice": "CalculatorApp.exe",
                    "paint": "mspaint.exe",
                    "cmd": "cmd.exe",
                    "invite de commande": "cmd.exe",
                    "powershell": "powershell.exe",
                    "terminal": "WindowsTerminal.exe",
                    "zoom": "Zoom.exe",
                    "notion": "Notion.exe",
                    "obs": "obs64.exe",
                    "gimp": "gimp-2.10.exe",
                    "whatsapp": "WhatsApp.exe",
                    "telegram": "Telegram.exe",
                    "instagram": "Instagram.exe",
                    "facebook": "Facebook.exe",
                    "audacity": "audacity.exe",
                    "adobe reader": "AcroRd32.exe",
                    "acrobat": "AcroRd32.exe",
                    "wordpad": "wordpad.exe",
                    "onenote": "ONENOTE.EXE"
                }
                app_process = process_map.get(friendly_name.lower(), friendly_name)
                try:
                    result = subprocess.run(
                        ["taskkill", "/f", "/im", app_process],
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

            if action in {"ouvrir_app", "fermer_app"} and text:

                match = re.search(r"(?:ouvre|ouvrir|ferme|fermer)\s+(.+)", text)
                if match:
                    app_name = match.group(1)
                    if action == "ouvrir_app":
                        open_app(app_name)
                        return
                    elif action == "fermer_app":
                        close_app(app_name)
                        return
            elif action == "clic gauche":
                pyautogui.click()
            elif action == "double clic":
                pyautogui.doubleClick()
            elif action == "clic droit":
                pyautogui.rightClick()

            elif action.startswith("deplacer_"):
                pattern = r"deplacer_souris:(\w+)_(\d+)"
                match = re.match(pattern, action)
                if match:
                    direction = match.group(1)
                    distance = int(match.group(2)) if match.group(2) else 100
                    dx, dy = 0, 0
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

            elif action == "écrire_texte" and text:
                texte_a_ecrire = " ".join(text.split(" ")[1:]) if " " in text else ""
                pyautogui.write(texte_a_ecrire)
                return

            else:
                messagebox.showwarning("Orl", f"Action inconnue: {action}")

        except Exception as e:
            print("Erreur execution action: ", e)

    def ask_user_for_path(self, app_name):
        messagebox.showinfo("OrlVoice", f"Veuillez sélectionner l’exécutable de {app_name.capitalize()}.")
        file_path = filedialog.askopenfilename(title=f"Choisir {app_name}", filetypes=[("Fichiers EXE", "*.exe")])
        if file_path:
            set_app_path(app_name, file_path)
            return file_path
        return None

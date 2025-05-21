import json
import os

CONFIG_FILE = ".cache/app_paths.json"

default_config = {
    "whatsapp_path": "",
    "chrome_path": ""
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def set_app_path(app_name, path):
    config = load_config()
    config[f"{app_name}_path"] = path
    save_config(config)

def get_app_path(app_name):
    config = load_config()
    return config.get(f"{app_name}_path", "")

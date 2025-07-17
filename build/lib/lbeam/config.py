# src/lbeam/config.py
import os
import toml

CONFIG_PATH = os.path.expanduser("~/.config/lbeam/config.toml")

def load_config():
    if os.path.exists(CONFIG_PATH):
        return toml.load(CONFIG_PATH)
    return {}

def save_config(cfg):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, 'w') as f:
        toml.dump(cfg, f)

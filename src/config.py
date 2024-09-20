"""
This module handles loading and saving the application's configuration.

Functions:
    - load_settings(): Loads settings from the JSON configuration file.
    - save_settings(settings): Saves settings to the JSON configuration file.
"""

import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')


def load_settings():
    """
    Loads settings from the JSON configuration file.

    Returns:
        dict: A dictionary of settings loaded from the configuration file.
              If the file is missing or corrupted, returns default settings.
    """
    default_settings = {
        "reminder_interval": 20,  # Default to 20 minutes if config is missing
        "custom_message": "Time to stretch!",
        "play_sound": True,
        "notification_timeout": 10
    }

    try:
        with open(CONFIG_PATH, 'r') as f:
            settings = json.load(f)
        return settings
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or invalid JSON, return default settings
        return default_settings


def save_settings(settings):
    """
    Saves the given settings to the JSON configuration file.

    Args:
        settings (dict): A dictionary of settings to be saved to the configuration file.
    """
    with open(CONFIG_PATH, 'w') as f:
        json.dump(settings, f, indent=4)

"""
This module handles the creation of the settings GUI, allowing users to modify 
reminder settings like interval, message, and timeout.

Functions:
    - create_settings_gui(): Creates and runs the settings GUI.
    - save_new_settings(interval_entry, message_entry, sound_var, timeout_entry): 
      Saves new settings entered by the user to the configuration file.
"""

import tkinter as tk
from tkinter import messagebox
from config import load_settings, save_settings


def save_new_settings(interval_entry, message_entry, sound_var, timeout_entry):
    """
    Saves new settings entered by the user to the configuration file.

    Args:
        interval_entry (tk.Entry): Entry widget for the reminder interval.
        message_entry (tk.Entry): Entry widget for the custom reminder message.
        sound_var (tk.IntVar): Variable tracking whether the "Play Sound" option is enabled.
        timeout_entry (tk.Entry): Entry widget for the notification timeout.
    """
    try:
        new_interval = int(interval_entry.get())
        new_timeout = int(timeout_entry.get())
        new_message = message_entry.get()
        play_sound = sound_var.get()

        if new_interval <= 0 or new_timeout <= 0:
            raise ValueError

        settings = load_settings()
        settings['reminder_interval'] = new_interval
        settings['custom_message'] = new_message
        settings['play_sound'] = bool(play_sound)
        settings['notification_timeout'] = new_timeout
        save_settings(settings)

        messagebox.showinfo("Success", "Settings saved successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive numbers for interval and timeout.")


def create_settings_gui():
    """
    Creates and runs the settings GUI for the reminder application.
    Allows the user to modify the reminder interval, custom message, sound setting, and notification timeout.
    """
    # Load current settings
    settings = load_settings()
    current_interval = settings.get('reminder_interval', 20)
    current_message = settings.get('custom_message', "Time to stretch!")
    current_timeout = settings.get('notification_timeout', 10)
    current_play_sound = settings.get('play_sound', True)

    # Create the root window
    root = tk.Tk()
    root.title("Settings")
    
    # Make the window wider for better layout
    root.geometry("400x250")  # Increased width to 400 pixels
    
    # Reminder Interval
    tk.Label(root, text="Reminder Interval (minutes):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    interval_entry = tk.Entry(root, width=30)  # Wider entry box
    interval_entry.grid(row=0, column=1, padx=10, pady=5)
    interval_entry.insert(0, str(current_interval))

    # Custom Message
    tk.Label(root, text="Custom Reminder Message:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    message_entry = tk.Entry(root, width=30)  # Wider entry box
    message_entry.grid(row=1, column=1, padx=10, pady=5)
    message_entry.insert(0, current_message)

    # Play Sound Checkbox
    sound_var = tk.IntVar(value=int(current_play_sound))
    tk.Checkbutton(root, text="Play Sound", variable=sound_var).grid(row=2, columnspan=2, pady=10)

    # Notification Timeout
    tk.Label(root, text="Notification Timeout (seconds):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    timeout_entry = tk.Entry(root, width=30)  # Wider entry box
    timeout_entry.grid(row=3, column=1, padx=10, pady=5)
    timeout_entry.insert(0, str(current_timeout))

    # Save button
    save_button = tk.Button(root, text="Save Settings", command=lambda: save_new_settings(interval_entry, message_entry, sound_var, timeout_entry))
    save_button.grid(row=4, columnspan=2, pady=20)

    root.mainloop()

"""
This module manages the system tray icon for the Stretch Reminder application.

It provides the following features:
    - A tray icon that updates based on the reminder state (enabled/disabled).
    - A menu that allows users to enable/disable reminders, access settings, or exit the app.
    - Integration with the pystray library to run the tray icon in the system tray.

Functions:
    - create_icon(enabled): Creates a tray icon with a visual indicator (green circle/red line) based on the reminder state.
    - toggle_reminders(icon): Toggles the reminder state and updates the tray icon.
    - update_menu(icon, reminder_text): Updates the menu with the current reminder state (Enable/Disable).
    - open_settings(): Opens the settings GUI in a separate thread.
    - setup_tray(): Initializes and runs the tray icon and menu.
"""

import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
from reminder import schedule_reminder
from config import load_settings
from settings_gui import create_settings_gui  # Import the GUI function


# Global state to track whether reminders are enabled
reminders_enabled = False


def create_icon(enabled):
    """
    Creates the tray icon based on the reminder state.

    Args:
        enabled (bool): If True, the icon will show a green circle. 
                        If False, it will show a red horizontal line.

    Returns:
        Image: The generated icon image.
    """
    image = Image.new('RGBA', (64, 64), color=(255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle as the icon background (rounded corners)
    corner_radius = 12
    draw.rounded_rectangle([0, 0, 64, 64], radius=corner_radius, fill="white", outline="black")

    if enabled:
        draw.ellipse([12, 12, 52, 52], fill="green")  # Green circle when enabled
    else:
        draw.line([12, 32, 52, 32], fill="red", width=8)  # Red horizontal line when disabled

    return image


def toggle_reminders(icon):
    """
    Toggles the reminder state and updates the tray icon accordingly.

    Args:
        icon (pystray.Icon): The tray icon to update.
    """
    global reminders_enabled

    if not reminders_enabled:
        # Enable reminders
        settings = load_settings()
        interval = settings.get("reminder_interval", 20)

        reminder_thread = threading.Thread(target=schedule_reminder, args=(interval,))
        reminder_thread.daemon = True
        reminder_thread.start()

        reminders_enabled = True
        icon.icon = create_icon(True)  # Update to green circle
        update_menu(icon, "Disable Reminders")  # Update menu text
    else:
        # Disable reminders
        reminders_enabled = False
        icon.icon = create_icon(False)  # Update to red line
        update_menu(icon, "Enable Reminders")  # Update menu text


def update_menu(icon, reminder_text):
    """
    Updates the tray menu with the current reminder state.

    Args:
        icon (pystray.Icon): The tray icon whose menu needs updating.
        reminder_text (str): The text to display for the reminder toggle (Enable/Disable).
    """
    icon.menu = Menu(
        MenuItem(reminder_text, lambda: toggle_reminders(icon)),  # Update the reminder toggle text
        MenuItem("Settings", lambda: open_settings()),  # Add settings option
        MenuItem("Exit", lambda: icon.stop())
    )


def open_settings():
    """
    Opens the settings GUI in a new thread.
    """
    threading.Thread(target=create_settings_gui).start()  # Open GUI in a separate thread


def setup_tray():
    """
    Sets up the system tray icon and menu, and starts the tray application.
    """
    icon_image = create_icon(reminders_enabled)
    menu = Menu(
        MenuItem("Enable Reminders", lambda: toggle_reminders(icon)),  # Starts as "Enable"
        MenuItem("Settings", lambda: open_settings()),  # Add settings option
        MenuItem("Exit", lambda: icon.stop())
    )
    icon = Icon("Stretch Reminder", icon_image, menu=menu)
    icon.run()


if __name__ == "__main__":
    setup_tray()

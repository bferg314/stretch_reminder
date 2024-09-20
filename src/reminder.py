"""
This module handles the scheduling of reminders and sending notifications to the user.

Functions:
    - notify(message, timeout): Sends a notification to the user.
    - schedule_reminder(interval): Schedules reminders at regular intervals.
"""

import time
from plyer import notification
from config import load_settings

def notify(message, timeout):
    """
    Sends a notification to the user.

    Args:
        message (str): The message to display in the notification.
        timeout (int): The number of seconds the notification will be displayed before disappearing.
    """
    notification.notify(
        title="Stretch Reminder!",
        message=message,
        timeout=timeout
    )


def schedule_reminder(interval):
    """
    Schedules reminders to be sent at regular intervals.

    Args:
        interval (int): The interval in minutes between reminders.
    """
    settings = load_settings()
    custom_message = settings.get("custom_message", "Time to stretch!")
    timeout = settings.get("notification_timeout", 10)

    print(f"Reminders will be sent every {interval} minutes.")

    while True:
        time.sleep(interval * 60)  # Wait for the specified interval in minutes
        print(f"Sending reminder: {custom_message}")  # Debugging output
        notify(custom_message, timeout)


# Stretch Reminder App

A simple cross-platform system tray application to remind you to take breaks and stretch during long periods of work. The app is configurable and supports regular notifications with customizable intervals, messages, and sounds.

## Features

- **Tray Icon**: Shows the current state of reminders (enabled/disabled).
- **Reminders**: Regular pop-up notifications to remind you to stretch.
- **Settings GUI**: Allows users to customize reminder interval, message, and other settings.
- **Cross-Platform**: Works on both Windows and macOS.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd stretch_reminder
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate    # On Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    python src/tray.py
    ```

## Configuration

- The application uses a `settings.json` file for configuration. You can modify the following settings:
  - `reminder_interval`: Time in minutes between reminders.
  - `custom_message`: The message that will be displayed in the notification.
  - `play_sound`: Whether a sound should play with the notification (True/False).
  - `notification_timeout`: How long the notification should be displayed (in seconds).

## Usage

- The tray icon provides an easy way to enable or disable reminders. You can also access the settings GUI from the tray menu to change settings.
- Double-click the tray icon to toggle reminders on and off.

## Requirements

- Python 3.10 or later
- Required Python libraries (listed in `requirements.txt`):
  - `pystray`
  - `plyer`
  - `Pillow`

## License

This project is licensed under the MIT License.

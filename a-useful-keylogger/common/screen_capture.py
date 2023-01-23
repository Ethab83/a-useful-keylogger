# test_screen_capture.py
import numpy as np
import cv2
import pyautogui
from PIL import Image

class Screen_Capture:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        self.count = 0
        self.width = 1920
        self.height = 1080
        self.cropped_width = 200
        self.cropped_height = 200

    def calculate_box(self, x, y):
        # left edge
        self.left = x - self.cropped_width / 2
        if self.left < 0:
            self.left = 0

        # right edge
        self.right = x + self.cropped_width / 2
        if self.right > 1920:
            self.right = 1920

        # top edge
        self.top = y - self.cropped_height / 2
        if self.top < 0:
            self.top = 0

        # bottom edge
        self.bottom = y + self.cropped_height / 2
        if self.bottom > 1080:
            self.bottom = 108
        
    def take_screenshot(self, x, y, filename=''):
        filename = filename + str(self.count) + '.png'
        image = pyautogui.screenshot()
        self.calculate_box(x, y)
        image = image.crop((self.left, self.top, self.right, self.bottom))
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename, image)
        self.count += 1

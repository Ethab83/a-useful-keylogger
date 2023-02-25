# A Useful Keylogger

Since this project is unfinished the readme will just have to do with creating it

---

## Project Idea

A keylogger that can write step-by-step guides on everything the user does while it is recording
Basically like [Problem Steps Recorder](https://support.microsoft.com/en-us/windows/record-steps-to-reproduce-a-problem-46582a9b-620f-2e36-00c9-04e25d784e47) but platform independent and outputting to markdown

---

## Requirements

- Log mouse clicks, and key commands
    - Tell the difference between typing and commands
- Put terminal commands as `code`
- Take screenshots of mouse-click locations
- DO NOT LOG PASSWORDS
- Create numbered step-by-step guide in markdown

---

## Use Cases

- Easily create reproducible steps for IT
- Automate build/installation docs

---

## For Devs

### pip installs

- screen capturing
    - numpy
    - cv2
    - pyautogui
    - PIL [TODO: verify its all caps]
- keyboard/mouse monitoring
    - pynput
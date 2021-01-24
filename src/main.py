import numpy
import cv2
import pyautogui
import keyboard

filename = "screencapture"
width, height = pyautogui.size()
resolution = (width, height)
framerate = 30.0
codec = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(filename + ".mp4", codec, framerate, resolution)

while True:
    screenshot = pyautogui.screenshot()
    numpy_array = numpy.array(screenshot)
    frame = cv2.cvtColor(numpy_array, cv2.COLOR_BGR2RGB)
    video.write(frame)

    if keyboard.is_pressed('F4'):
        cv2.destroyAllWindows()
        video.release()
        break

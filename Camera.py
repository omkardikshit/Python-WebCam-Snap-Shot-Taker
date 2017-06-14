import time
import cv2

camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(1)
return_value, image = camera.read()
cv2.imwrite("Capture.png", image)
del(camera) 

import picamera
import time
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(4)
camera.start_preview()

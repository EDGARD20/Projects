from picamera import PiCamera
from time import sleep


camera = PiCamera()
camera.resolution=(490 ,480)
camera.rotation=180
camera.start_preview()
sleep(5)
camera.start_preview()
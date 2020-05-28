
# This program will take a pics and scan faces come across the raspberry pi camera in real time.

# these Libs must be available on python.

import picamera
from time import sleep
import numpy
# openCV
import cv2
import io


# makes a loop to take pics constantly
try:
    while True:
        # Create a memory stream so photos doesn't need to be saved in a file.
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            # Get the picture (low resolution, so it should be quite fast)
            camera.resolution = (320, 240)
            camera.rotation=180 # you may not need this, my camera is upside down...
            camera.capture(stream, format = 'jpeg')

        # then convert that picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype = numpy.uint8)

        # now create an OpenCV image
        image = cv2.imdecode(buff, 1)

        #load a cascade file for the detecting faces(or anything you want)
        # the open source link is :
        # https://github.com/opencv/opencv/tree/master/data/haarcascades
        # you just need to copy the link like this.
        face_detection = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

        # then convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # now, search for the faces,
        # if you wand search for "detectMultiScale" there is nice document explain this very nice
        faces = face_detection.detectMultiScale(gray, 1.1, 5)
        # if you want you can print the result here also.
        print "found  " + str(len(faces)) + "  faces"

        # it is time for marking around the face,
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h), (2500,250,0), 2)

        # you can also save the pic, it is better not to, bc it take time.
        cv2.imwrite('result.jpg', image)



except KeyboardInterrupt:
    print "ThE EnD"
    print "Enjoy"
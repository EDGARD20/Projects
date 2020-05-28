clc
clear rpi
rpi = raspi('192.168.0.32','pi','Mohmir12');
myCam = cameraboard(rpi,'Resolution','640x480');
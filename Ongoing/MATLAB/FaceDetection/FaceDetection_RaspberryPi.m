%%
% MATLAB offered a special build for raspberry pi. You can download it via
% "HOME >> Add-On" and search for "MATLAB Support Package for raspberry
% pi". If you runs the initial setting for the first time on MATLAB, the SW
% palage for Raspberry pi will install automatically on your PI. it will
% take a couple of minutes, so be pationt.

% The initial Setting is used to connect MATLAB to Raspberry Pi, over WiFi
% or Ethernet conecction. You should not always use that, but if you have
% to, make sure you clear Worspace first.

% The initial Setting, should be like this:
% clear 
% rpi = raspi('Pi IP Address','Pi user','Pi Password');
% myCam = cameraboard(rpi, 'Resolution','640x480')
% the resolution size is up to you.

% I have set the Initial Setting on the seperate file due to avoid running
% it all the time. but for the first time. it should be run.
Initial_setting;
%%
% for getting an stream image form Raspberry Pi, we need a loop

for i = 1:1:50
   % take an image from PiCamera
   mySnap = snapshot(myCam);
   % take the image and keep it for a while 
   imshow( mySnap);
   hold on
   % Inside the prantesis you can mention exactly which object you want to
   % detect, fullfront face is the defult option, I will try with nose.
   fd = vision.CascadeObjectDetector('Nose');
   
   % merge the image to the pattern
   bbox = step(fd, mySnap);
   % Prepared output image by using the pattern and recognize the
   % interesting area
   
   imageOut = insertObjectAnnotation(mySnap,'rectangle', bbox,'Nose');
   % create the image to show up
   imshow(imageOut);
   title('Detected Nose');
   % here, it will draw the final image including the detection box and
   % text title abound the interesting area
   drawnow
    
end

% to be more convenient, close all figure after all
close all










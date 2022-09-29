# to use the cam
import cv2
# to config the audio
from playsound import playsound
# to config the fire 
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
# to open cam
cap = cv2.VideoCapture(0)
while(True):
    # to read what is in front of the cam
    ret,frame = cap.read()
    # to convert the color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # to detect the fire in mutiscale 
    # 1.2 refers to the accurecy of the detection of the fire 
    # 5 refers to the features of detection of the fire
    fire = fire_cascade.detectMultiScale(frame,1.2,5)
    # x,y,w,h refer to the directions 
    for (x,y,w,h) in fire:
        # to specifie the area of the fire
        ms_gray = gray[y:y+h, x:x+w]
        ms_color = frame[y:y+h , x:x+w]
        print('Fire is detected')
        playsound('audio.mp3')
     # to show the window    
    cv2.imshow('MS', frame)
    # to open the window until press on q from keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
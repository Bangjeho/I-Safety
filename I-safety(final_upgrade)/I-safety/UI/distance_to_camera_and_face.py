#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wmi
def brightness_control(blights):
    brightness = blights # percentage [0-100]
    c = wmi.WMI(namespace='wmi')

    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


# In[2]:


from tkinter import Tk
from tkinter import messagebox
import tkinter
import time as t
import cv2
import math
import threading
import sys
import pandas as pd
from datetime import datetime

check_list = [0]
ambient_light = [51]
getbrightness = [0]

# checking for between loop and break.
def check(check_value):
    check_list[0] = check_value

#set ambient light default 51
def ambient_light_check(light_value):
    ambient_light[0] = light_value

# alert message
def break_time_alert():
    i = 0
    sec = 3600
    while True:
        t.sleep(sec)
        i += 1
        root = Tk()
        root.withdraw()
        tkinter.messagebox.showwarning("주의","사용한 지 %d 시간 지났습니다. 10분 정도 휴식을 취하세요." 
                                    % i)

# brightness control from distance
def define_brights(distance,ambient_light):
    global brights
    if ambient_light[0] < 51:
        brights = 20
    else:
        if distance <= 30 and distance >= 0 :
            brights = 30
        elif distance > 30 and distance <= 60 :
            brights = 40
        elif distance > 60:
            brights = 50
    return brights

def get_brightness_value():
    return getbrightness

# face_dectection and find distance with eye and camera, control brightness
def face_detection(label):
    count = 1
    distance = 0.0
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Capture from the default deivce
    cap = cv2.VideoCapture(0)
    
    # The samples thingy
    # Make sure the file is in the same folder as the program..
    # otherwise this will not work
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        if check_list[0] == -1:
            sys.exit()

    # sleep for 5 minute after image capture
        if count % 61 == 0:
            data = pd.read_csv('data.csv')
            brights = define_brights(distance,ambient_light)
            brightness_control(brights)
            getbrightness[0] = brights
            label.setText("      Distance : "+ str(distance)+" cm             "+"Brightness : "+str(brights) +" lumens")
            k = len(data)
            data.loc[k] = [datetime.now().strftime('%Y'),datetime.now().strftime('%m'),datetime.now().strftime('%d'),distance]
            data.to_csv(R'C:\Users\entity\Desktop\I-safety\UI\data.csv',header = True, index = False)
            break

        # Caputure a single frame
        ret, huge_frame = cap.read()
        frame = cv2.resize(huge_frame, (0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_NEAREST)
        # Create the greyscale and detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # Add squeres for each face
        for (x, y, w, h) in faces:
            distancei = (2*3.14 * 180)/(w+h*360)*1000 + 3
        #        distance = distancei *2.54
            distance = math.floor(distancei*2.54)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

        # Display the resulting frame
            cv2.putText(frame,'D = ' + str(distance) + 'cm', (x+w,y+h),font,1,(0,255,0),2)

        cv2.imshow('face detection', frame)
        count += 1
    
    # Stop the capture
    cap.release()
    # Destory the window     
    cv2.destroyAllWindows()
    
    t.sleep(10)
    face_detection(label)

# threading alert and face dection
def play(label):
    alert_t = threading.Thread(target=break_time_alert) 
    face_d_t = threading.Thread(target=face_detection, args = (label,))
    alert_t.start()
    face_d_t.start()

if __name__ == "__main__":
    play()


# In[ ]:





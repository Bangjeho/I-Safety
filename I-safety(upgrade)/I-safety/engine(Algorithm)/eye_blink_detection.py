#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import cv2
import dlib
from scipy.spatial import distance as dist
import time as t
import threading

timer_check = 0
time = [0]
def eye_aspect_ratio(eye):
    # compute the euclidean distance between the vertical eye landmarks
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal eye landmarks
    C = dist.euclidean(eye[0], eye[3])

    # compute the EAR
    ear = (A + B) / (2 * C)
    return ear
def eye_blink_detect():
    global timer_check
    JAWLINE_POINTS = list(range(0, 17))
    RIGHT_EYEBROW_POINTS = list(range(17, 22))
    LEFT_EYEBROW_POINTS = list(range(22, 27))
    NOSE_POINTS = list(range(27, 36))
    RIGHT_EYE_POINTS = list(range(36, 42))
    LEFT_EYE_POINTS = list(range(42, 48))
    MOUTH_OUTLINE_POINTS = list(range(48, 61))
    MOUTH_INNER_POINTS = list(range(61, 68))

    EYE_AR_THRESH = 0.22
    EYE_AR_CONSEC_FRAMES = 3
    EAR_AVG = 0
    timer_check = 0
    COUNTER = 0
    TOTAL = 0
# to detect the facial region
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    # capture video from live video stream
    cap = cv2.VideoCapture(0)
    while True:
        # get the frame
        ret, frame = cap.read()
        #frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        if ret:
            # convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)
            for rect in rects:
                x = rect.left()
                y = rect.top()
                x1 = rect.right()
                y1 = rect.bottom()
                # get the facial landmarks
                landmarks = np.matrix([[p.x, p.y] for p in predictor(frame, rect).parts()])
                # get the left eye landmarks
                left_eye = landmarks[LEFT_EYE_POINTS]
                # get the right eye landmarks
                right_eye = landmarks[RIGHT_EYE_POINTS]
                # draw contours on the eyes
                left_eye_hull = cv2.convexHull(left_eye)
                right_eye_hull = cv2.convexHull(right_eye)
                cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1) # (image, [contour], all_contours, color, thickness)
                cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)
                # compute the EAR for the left eye
                ear_left = eye_aspect_ratio(left_eye)
                # compute the EAR for the right eye
                ear_right = eye_aspect_ratio(right_eye)
                # compute the average EAR
                ear_avg = (ear_left + ear_right) / 2.0
                # detect the eye blink
                if ear_avg < EYE_AR_THRESH:
                    COUNTER += 1
                else:
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1
                        timer_check = 1

            cv2.imshow("Checking Dry eye syndrome", frame)
            key = cv2.waitKey(1) & 0xFF
            # When key 'Q' is pressed, exit
            if timer_check == 1 :
#             if key is ord('q'):
                break

    # release all resources
    cap.release()
    # destroy all windows
    cv2.destroyAllWindows()


# In[17]:


def timer():
    sc = 20
    for i in range(1,sc+1):
        if timer_check == 1:
            break
        else:
            time[0] = i
            print(time[0])
            t.sleep(1)

def get_time():
    return time
            
def Run():            
    eye_b_t = threading.Thread(target = eye_blink_detect)
    timer_t = threading.Thread(target = timer)
    eye_b_t.start()
    timer_t.start()
    
if __name__ == '__main__':
    Run()


# In[ ]:





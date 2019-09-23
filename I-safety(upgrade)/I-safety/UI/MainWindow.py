#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *
import distance_to_camera_and_face as dtc
import eye_blink_detection as ebd
import time as t
import DryEyeSyndromeWindow


# In[2]:


form_class = uic.loadUiType("MainWindow.Ui")[0]
class MainWindow(QMainWindow,form_class):
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(321, 527)
        self.setUI()
        
    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.OnOffButtonClick)
        self.horizontalSlider.valueChanged.connect(self.ambient_light_control)
#         self.pushButton_3.clicked.connect(self.self_eye_test)
        self.pushButton_3.clicked.connect(self.open_DiagnosisWindow)
        
#     def brightness_control(self):
#         brightness = dtc.get_brightness_value()
#         self.label_7.setText(str(brightness[0]) + ' lx')
    def open_DiagnosisWindow(self):
        from DryEyeSyndromeWindow import DryEyeSyndromeWindow
        self.DiagnosisWindow = DryEyeSyndromeWindow()
        self.DiagnosisWindow.show()
        self.hide()
    def self_eye_test(self):
        if self.pushButton.isChecked():
            self.pushButton.setChecked(False)
            dtc.check(-1)
            t.sleep(1)
        ebd.Run()
#         t.sleep(10)
        time = ebd.get_time()
        
        print('time:',time[0])
    def OnOffButtonClick(self):
        if self.pushButton.isChecked():
            dtc.check(1)
            dtc.play(self.label_6)
        else:
            dtc.check(-1)
    
    def ambient_light_control(self):
        value = self.horizontalSlider.value()
        self.label_4.setText(str(value))
        dtc.ambient_light_check(value)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MainWindow()
    myApp.show()
    app.exec()
        


# In[ ]:





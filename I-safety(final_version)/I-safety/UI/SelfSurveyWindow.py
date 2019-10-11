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


# In[ ]:


form_class = uic.loadUiType("SelfSurvey.Ui")[0]
class SelfSurveyWindow(QMainWindow,form_class):
    def __init__(self):
        self.count = 0
        super().__init__()
        self.setFixedSize(321, 527)
        self.setUI()
        self.pushButton.clicked.connect(self.Checkresult)
        self.checkBox.clicked.connect(self.Checked)
        self.checkBox_2.clicked.connect(self.Checked)
        self.checkBox_3.clicked.connect(self.Checked)
        self.checkBox_4.clicked.connect(self.Checked)
        self.checkBox_5.clicked.connect(self.Checked)
        self.checkBox_6.clicked.connect(self.Checked)
        
    def setUI(self):
        self.setupUi(self)
    
    def Checked(self):
        self.count += 1

    def Checkresult(self):
        time = ebd.get_time()
        from ResultWindow import ResultWindow
        self.rw = ResultWindow()
        self.rw.label_6.setText(str(time[0]) + " sec")
        self.rw.label_7.setText(str(self.count))
        self.rw.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = SelfSurveyWindow()
    myApp.show()
    app.exec()


# In[ ]:





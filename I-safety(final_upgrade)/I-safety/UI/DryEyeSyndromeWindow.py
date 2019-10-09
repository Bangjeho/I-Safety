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


# In[2]:


form_class = uic.loadUiType("DryEyeSyndromeWindow.Ui")[0]
class DryEyeSyndromeWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setFixedSize(321, 278)
        self.setUI()
        
    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.BackMainWindow)
        self.pushButton_3.clicked.connect(self.Clickblink)
        self.pushButton_4.clicked.connect(self.Clicksurvey)
        
    def Clicksurvey(self):
        from SelfSurveyWindow import SelfSurveyWindow
        if self.pushButton_3.isChecked():
            self.ssWin = SelfSurveyWindow()
            self.ssWin.show()
        else:
            QMessageBox.about(self, "Waring!", "please Check 'Catch eye blink' Button.")
    def Clickblink(self):
        QMessageBox.about(self, "notice", "checking your eyes blink in 20sec. \n Keep your eyes open for 20 sec. ")
        ebd.Run()
        if self.pushButton_3.isChecked():
            pass
        else:
            self.pushButton_3.setChecked(True)

    def BackMainWindow(self):
        from MainWindow import MainWindow
        self.MainWin = MainWindow()
        self.MainWin.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = DryEyeSyndromeWindow()
    myApp.show()
    app.exec()


# In[ ]:





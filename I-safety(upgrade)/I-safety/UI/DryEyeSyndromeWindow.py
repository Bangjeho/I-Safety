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
        self.setFixedSize(321, 527)
        self.setUI()
        
    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.BackMainWindow)

    def BackMainWindow(self):
        from MainWindow import MainWindow
        print('clicked!!')
        self.MainWin = MainWindow()
        self.MainWin.show()
        self.hide()        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = DryEyeSyndromeWindow()
    myApp.show()
    app.exec()


# In[ ]:





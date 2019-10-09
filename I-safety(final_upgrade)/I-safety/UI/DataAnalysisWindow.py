#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *
import distance_to_camera_and_face as dtc
import eye_blink_detection as ebd
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import image_making as im


# In[3]:


form_class = uic.loadUiType("DataAnalysisWindow.Ui")[0]
class DataAnalysisWindow(QMainWindow,form_class):
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(321, 527)
        self.setUI()
        
    def setUI(self):
        self.setupUi(self)
        self.label.setText(datetime.datetime.today().strftime('%m'))
        self.label_2.setText(datetime.datetime.today().strftime('%Y'))
        self.pushButton_2.clicked.connect(self.BackMainWindow)
        self.pushButton.clicked.connect(self.SubMonth)
        self.pushButton_3.clicked.connect(self.AddMonth)
        
    def AddMonth(self):
        if self.label.text() == '12':
            get_year = datetime.datetime.strptime(self.label_2.text(),'%Y')
            new_year = get_year + relativedelta(years= 1)
            new_year = new_year.strftime('%Y')
            self.label_2.setText(new_year)
            
        get_month = datetime.datetime.strptime(self.label.text(),'%m')
        new_month = get_month + relativedelta(months= 1)
        new_month = new_month.strftime('%m')
        self.label.setText(new_month)
        year = self.label_2.text()
        month = self.label.text()
        im.set_date(year,month)
        im.setting_database(self.label_4)
    def SubMonth(self):
        if self.label.text() == '01':
            get_year = datetime.datetime.strptime(self.label_2.text(),'%Y')
            new_year = get_year - relativedelta(years= 1)
            new_year = new_year.strftime('%Y')
            self.label_2.setText(new_year)
            
        get_month = datetime.datetime.strptime(self.label.text(),'%m')
        new_month = get_month - relativedelta(months= 1)
        new_month = new_month.strftime('%m')
        self.label.setText(new_month)
        year = self.label_2.text()
        month = self.label.text()
        im.set_date(year,month)
        im.setting_database(self.label_4)
    def BackMainWindow(self):
        from MainWindow import MainWindow
        self.MainWin = MainWindow()
        self.MainWin.show()
        self.hide()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = DataAnalysisWindow()
    myApp.show()
    app.exec()


# In[ ]:





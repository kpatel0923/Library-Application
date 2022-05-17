import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Signup(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def clear_text(self):
        self.lineEdit_firstname.clear()
        self.lineEdit_lastname.clear()
        self.lineEdit_username_signup.clear()
        self.lineEdit_password_signup.clear()
        self.lineEdit_password_signup_2.clear()
        self.lineEdit_email.clear()
        self.lineEdit_cc.clear()

    def validate(self):
        firstname = self.lineEdit_firstname.text()
        lastname = self.lineEdit_lastname.text()
        username = self.lineEdit_username_signup.text()
        password = self.lineEdit_password_signup.text()
        password_2 = self.lineEdit_password_signup_2.text()
        email = self.lineEdit_email.text()
        cc = self.lineEdit_cc.text()

        #Insert code here

        Signup.clear_text(self)
    
    def back(self):
        self.page_holder.setCurrentWidget(self.login)
        Signup.clear_text(self)
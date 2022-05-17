import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def clear_text(self):
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()

    def validate(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        self.label_welcome.setText(f'Welcome {username}')

        #This method will load all the reservations in the list widget
        Login.load_reservations(self)

        Login.modify_page(self)

        Login.clear_text(self)
        self.page_holder.setCurrentWidget(self.user)

    def modify_page(self):
        #Write code here for loading their account info into the account fields
        #Use the getters and put pass them as arguments in the setText
        self.lineEdit_firstname_change.setText()
        self.lineEdit_lastname_change.setText()
        self.lineEdit_username_change.setText()
        self.lineEdit_password_change.setText()
        self.lineEdit_password_change_2.setText()
        self.lineEdit_email_change.setText()
        self.lineEdit_cc_change.setText()

    def load_reservations(self):
        reservations = [[1, 'David', '09/23/2021', '09/28/2021'],[2, 'David', '10/23/2021', '10/28/2021'],[3, 'David', '11/23/2021', '11/28/2021']]
        self.listWidget_reservations.clear()
        for item in reservations:
            number = item[0]
            indate = item[2]
            outdate = item[3]

            string_input = f'ID: {number}, CheckIn Date: {indate}, CheckOut date: {outdate}'
            self.listWidget_reservations.addItem(string_input)

    def search_reservation(self, param):
        pass
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from reservation import *
from modifications import *

class User(QMainWindow):

    current_user = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def clear_text(self):
        self.listWidget_reservations.clear()

        self.lineEdit_firstname_change.clear()
        self.lineEdit_lastname_change.clear()
        self.lineEdit_username_change.clear()
        self.lineEdit_password_change.clear()
        self.lineEdit_password_change_2.clear()
        self.lineEdit_email_change.clear()
        self.lineEdit_cc_change.clear()

        Reservation.clear_text(self)
        Modification.clear_text_change(self)

    def change(self):
        selected_item = self.listWidget_reservations.currentItem().text()
        res_id = selected_item[0]

        #Change these to the dates according to the search
        self.label_indate.setText('Selected Date')
        self.label_outdate.setText('Selected Date')

    def cancel(self):
        selected_index = self.listWidget_reservations.currentRow()
        if selected_index < 0:
            print('try again')
        else:
            selected_item = self.listWidget_reservations.currentItem().text()
            print(selected_item)

            self.listWidget_reservations.takeItem(selected_index)
            print('removed')

    def checkinout(self):
        selected_index = self.listWidget_reservations.currentRow()
        if selected_index < 0:
            print('try again')
        else:
            selected_item = self.listWidget_reservations.currentItem().text()
            print(selected_item[0])

            self.listWidget_reservations.takeItem(selected_index)
            print('Checked In')
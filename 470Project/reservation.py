import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Reservation(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def clear_text(self):
        self.label_indate.setText('Selected Date')
        self.label_outdate.setText('Selected Date')
        self.comboBox_types.setCurrentIndex(0)
        #self.currentText()

    def reserve(self):
        type = self.comboBox_types.currentText()
        indate = self.label_indate.text()
        outdate = self.label_outdate.text()

        Reservation.clear_text(self)
        self.page_holder.setCurrentWidget(self.user)

    def back(self):
        Reservation.clear_text(self)
        self.page_holder.setCurrentWidget(self.user)


    def change_list(self):
        reservations = [[1, 'David', '09/23/2021', '09/28/2021'], [2, 'Sagar', '10/23/2021', '10/28/2021'],
                        [3, 'Eli', '11/23/2021', '11/28/2021']]
        self.listWidget_reservations.clear()
        for item in reservations:
            number = item[0]
            name = item[1]
            indate = item[2]
            outdate = item[3]

            string_input = f'{number}: Name: {name}, CheckIn Date: {indate}, CheckOut date: {outdate}'
            self.listWidget_reservations.addItem(string_input)
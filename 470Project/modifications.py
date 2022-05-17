import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Modification(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def clear_text_change(self):
        self.label_indate_change.setText('Selected Date')
        self.label_outdate_change.setText('Selected Date')

    def change(self):
        indate = self.label_indate.text()
        outdate = self.label_outdate.text()

        Modification.clear_text_change(self)
        self.page_holder.setCurrentWidget(self.user)

    def back(self):
        Modification.clear_text_change(self)
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
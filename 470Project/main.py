import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

# files
from buttonCommands import *

ui,_ = loadUiType('UI.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        title = "Reservations"
        self.setWindowTitle(title)

        Buttons.reservation_home(self)
        Buttons.login(self)
        Buttons.signup(self)

        #User page commands
        Buttons.user(self)
        Buttons.account(self) #User account modifications

        #Reservation page
        Buttons.reservation(self)
        self.calendarWidget_indate.selectionChanged.connect(self.dateSelectIn)
        self.calendarWidget_outdate.selectionChanged.connect(self.dateSelectInOut)

        #Change reservation
        Buttons.change(self)
        self.calendarWidget_indate_change.selectionChanged.connect(self.dateSelectIn_change)
        self.calendarWidget_outdate_change.selectionChanged.connect(self.dateSelectInOut_change)



    def dateSelectIn(self):
        date = self.calendarWidget_indate.selectedDate()
        date2 = str(date.toPyDate())
        self.label_indate.setText(date2)

    def dateSelectInOut(self):
        date = self.calendarWidget_outdate.selectedDate()
        date2 = str(date.toPyDate())
        self.label_outdate.setText(date2)

    def dateSelectIn_change(self):
        date = self.calendarWidget_indate_change.selectedDate()
        date2 = str(date.toPyDate())
        self.label_indate_change.setText(date2)

    def dateSelectInOut_change(self):
        date = self.calendarWidget_outdate_change.selectedDate()
        date2 = str(date.toPyDate())
        self.label_outdate_change.setText(date2)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()







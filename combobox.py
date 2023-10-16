import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import datetime

from_class = uic.loadUiType("Combobox.ui")[0]


class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ComboBox")
      
        for year in range(1910, 2023 + 1):
            self.cbYear.addItem(str(year))
        
        for month in range(1, 12 + 1):
            self.cbMonth.addItem(str(month))
        
        for day in range(1, 31 + 1):
            self.cbDay.addItem(str(day))
        
        self.cbYear.setCurrentText("1995")

        self.cbYear.currentIndexChanged.connect(self.printBirthday)
        self.cbMonth.currentIndexChanged.connect(self.printBirthday)
        self.cbDay.currentIndexChanged.connect(self.printBirthday)

        self.printBirthday()

        self.calendarWidget.clicked.connect(self.selectDate)

    
    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')

        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)
        date_obj = datetime.strptime(year + month.zfill(2) + day.zfill(2), "%Y%m%d")
        self.lineEdit.setText(date_obj.strftime("%Y-%m-%d"))

    
    def printBirthday(self):
        year = self.cbYear.currentText()
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        date_obj = datetime.strptime(year + month.zfill(2) + day.zfill(2), "%Y%m%d")
        self.lineEdit.setText(date_obj.strftime("%Y-%m-%d"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
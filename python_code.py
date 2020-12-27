#Scripted by: Laxier
#Importing libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_CurrencyConverter(object):
    #initialization
    def setupUi(self, CurrencyConverter):
        CurrencyConverter.setObjectName("CurrencyConverter")
        CurrencyConverter.setEnabled(True)
        CurrencyConverter.resize(384, 565)
        CurrencyConverter.setMinimumSize(QtCore.QSize(384, 565))
        CurrencyConverter.setMaximumSize(QtCore.QSize(384, 565))
        self.centralwidget = QtWidgets.QWidget(CurrencyConverter)
        self.centralwidget.setStyleSheet("background-color: #f5f5f5")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(-50, -20, 471, 311))
        self.frame.setMouseTracking(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #ADCCE3")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.name_of_th_programm = QtWidgets.QLabel(self.frame)
        self.name_of_th_programm.setGeometry(QtCore.QRect(70, 30, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.name_of_th_programm.setFont(font)
        self.name_of_th_programm.setStyleSheet("color: #263F52")
        self.name_of_th_programm.setObjectName("name_of_th_programm")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(160, 100, 331, 191))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("imgs/logo.png"))
        self.logo.setObjectName("logo")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-50, 290, 481, 401))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.input_text = QtWidgets.QLineEdit(self.frame_2)
        self.input_text.setGeometry(QtCore.QRect(70, 110, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("color: #082567;\n"
"border: 2px solid #082567;\n"
"borger radius: 3px;\n"
"")
        self.input_text.setAlignment(QtCore.Qt.AlignCenter)
        self.input_text.setObjectName("input_text")
        self.input_text.setMaxLength(10)
        self.do_duty = QtWidgets.QPushButton(self.frame_2)
        self.do_duty.setGeometry(QtCore.QRect(340, 110, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.do_duty.setFont(font)
        self.do_duty.setStyleSheet("")
        self.do_duty.setAutoDefault(False)
        self.do_duty.setFlat(False)
        self.do_duty.setObjectName("do_duty")
        self.do_duty.clicked.connect(self.convertion)
        self.to_currency = QtWidgets.QComboBox(self.frame_2)
        self.to_currency.setGeometry(QtCore.QRect(284, 40, 111, 31))
        self.to_currency.setObjectName("to_currency")
        self.from_currency = QtWidgets.QComboBox(self.frame_2)
        self.from_currency.setGeometry(QtCore.QRect(90, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.to_currency.setMaxVisibleItems(10)
        #updating the CURRENCY COST
        response = requests.get("https://api.exchangeratesapi.io/latest")
        #creating the gloabal var containing currency ang EUR-COST
        global a
        a = response.json()['rates']
        a.update({'EUR': 1})
        for key in a:
            i = str(key)
            self.from_currency.addItem(i)
            self.to_currency.addItem(i)
        self.from_currency.setFont(font)
        self.from_currency.setCurrentText("")
        self.from_currency.setObjectName("from_currency")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.from_currency.setMaxVisibleItems(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.output = QtWidgets.QLabel(self.frame_2)
        self.output.setGeometry(QtCore.QRect(110, 190, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.output.setFont(font)
        self.output.setStyleSheet(" color: grey; \n"
"border: 2px solid #082567;\n"
"borger radius: 3px;\n"
"")
        self.output.setTextFormat(QtCore.Qt.AutoText)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        CurrencyConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(CurrencyConverter)
        QtCore.QMetaObject.connectSlotsByName(CurrencyConverter)

    def retranslateUi(self, CurrencyConverter):
        _translate = QtCore.QCoreApplication.translate
        CurrencyConverter.setWindowTitle(_translate("CurrencyConverter", "MainWindow"))
        self.name_of_th_programm.setText(_translate("CurrencyConverter", "Currency Converter"))
        self.input_text.setPlaceholderText(_translate("CurrencyConverter", "enter the money"))
        self.do_duty.setText(_translate("CurrencyConverter", "CONVERT"))
        self.label.setText(_translate("CurrencyConverter", "from"))
        self.label_2.setText(_translate("CurrencyConverter", "to"))
        self.output.setText(_translate("CurrencyConverter", "you get:"))

    def convertion(self):
        # converts cost in 1current to 2current
        if(self.input_text.text()):
            to_do = int(self.input_text.text())
            to = self.to_currency.currentText()
            fro = self.from_currency.currentText()
            #getting cost from global var a created in 86 line
            out = (to_do / float(a[fro]) * float(a[to]))
            print(out)
            #changing output
            self.output.setText("tou get: {:.2f} {}".format(out, to))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyConverter = QtWidgets.QMainWindow()
    ui = Ui_CurrencyConverter()
    ui.setupUi(CurrencyConverter)
    CurrencyConverter.show()
    sys.exit(app.exec_())

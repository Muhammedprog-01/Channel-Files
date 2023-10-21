import wifimangement_linux as wifi

import PyQt6.QtWidgets as qtw

import sys

class A(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        # if you have low resolution screen the size of the window and GUI component must resize.
        self.setFixedSize(1000,700)
        self.te=qtw.QTextEdit(self)
        self.te.setStyleSheet('background-color:yellow;color:black;font-size:18pt;border-radius:20px 20px;border-width:20px;border:yellow radius 20px;')
        self.te.setGeometry(100,50,800,500)


        self.btn1=qtw.QPushButton("Info List",self)
        self.btn1.setGeometry(890,630,100, 60)
        self.btn1.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn1.clicked.connect(self.info_list)

        self.btn2 = qtw.QPushButton("Info IP", self)
        self.btn2.setGeometry(760,630,100, 60)
        self.btn2.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn2.clicked.connect(self.ip)

        self.btn3 = qtw.QPushButton("HotSpot", self)
        self.btn3.setGeometry(70, 630,100, 60)
        self.btn3.setStyleSheet(
            'background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')
        self.btn3.clicked.connect(self.hotspot)


        self.btn4 = qtw.QPushButton("Info Interface", self)
        self.btn4.setGeometry(610, 630,120, 60)
        self.btn4.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn4.clicked.connect(self.info_interface)

        self.btn5 = qtw.QPushButton("Info Interface_L", self)
        self.btn5.setGeometry(460, 630,120, 60)
        self.btn5.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:11pt;')

        self.btn5.clicked.connect(self.info_interface_l)

        self.btn6 = qtw.QPushButton("WiFi On", self)
        self.btn6.setGeometry(330, 630,100, 60)
        self.btn6.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn6.clicked.connect(self.wifi_on)

        self.btn7 = qtw.QPushButton("WiFi Off", self)
        self.btn7.setGeometry(200, 630,100, 60)
        self.btn7.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn7.clicked.connect(self.wifi_off)




        self.show()


    def info_list(self):

        a=wifi.list()

        self.te.setText(a)



    def ip(self):



            b=wifi.ip()
            self.te.setText(f'IP ==> {b}')




    def info_interface(self):
        i=wifi.interface_status()
        self.te.setText(i)

    def info_interface_l(self):
        i=wifi.interface_list()
        self.te.setText(str(i))
    def wifi_on(self):
        o=wifi.on()

    def wifi_off(self):
        off = wifi.off()

    def hotspot(self):
        hot_spot=wifi.hospot("SSS-1","12345678")




app=qtw.QApplication(sys.argv)
window=A()
window.show()
sys.exit(app.exec())
import sys
import os,time,pendulum
import serial ,csv
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from Interface.ui_mainwindow import Ui_MainWindow
from Util.Serial_connector import Serial_Interface
import threading

class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.device = Serial_Interface()

        self.is_connect = self.device.is_connected()

        
        self.ui.Connect.clicked.connect(self.serial_connect)

        self.ui.pushButton_2.clicked.connect(self.backpage)

        self.ui.pushButton.clicked.connect(self.nextpage)

        self.index = self.ui.stackedWidget.currentIndex()

        # print(self.index)
       
    
          
    def nextpage(self):
        # print(self.index)
        if self.index < 2:
            
           self.ui.stackedWidget.setCurrentIndex(self.index + 1)
           self.index = self.ui.stackedWidget.currentIndex()
        elif self.index ==2:
            self.index = self.ui.stackedWidget.currentIndex()
            self.ui.stackedWidget.setCurrentIndex(0)

    def backpage(self):
        # print(self.index)
        if self.index > 0:
            self.ui.stackedWidget.setCurrentIndex(self.index - 1)
            self.index = self.ui.stackedWidget.currentIndex()
        elif self.index == 0:
            self.index = self.ui.stackedWidget.currentIndex()
            self.ui.stackedWidget.setCurrentIndex(2)
        
    def serial_connect(self):
       
        select_port = self.ui.SelectComPort.currentText()

        try:
            serial_data = self.device.connect(select_port) 
            self.ui.Connect.setText("DISCONNECT")
            self.ui.Connect.clicked.connect(self.serial_disconnect)
            
            
            def show_dashbroad(csvfile):
                HEADER = ["TIME","NO","Temperature","Humtidity","Pressure","Altitude","Height","Velocity","NO2","NH3","CO","RSSI"]
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(HEADER)
                for i,data in enumerate(self.device.startread_data()):
                    if data != "Temperature,Humtidity,Pressure,Altitude,Height,Velocity,NO2,NH3,CO,RSSI":
                        raw_data = data.split(',')
                        print(raw_data)
                        temp = raw_data[0]
                        humid = raw_data[1]
                        pressure = raw_data[2]
                        altitude = raw_data[3]
                        height = raw_data[4]
                        velocity = raw_data[5]
                        no2 = raw_data[6]
                        nh3 = raw_data[7]
                        co = raw_data[8]
                        rssi = raw_data[9]
                        self.ui.label_3.setText(temp + "C°")
                        self.ui.label_9.setText(humid + "%")
                        self.ui.label_12.setText(pressure + "hPa")
                        self.ui.label_18.setText(velocity)
                        self.ui.label_21.setText(altitude + "m")
                        self.ui.label_15.setText(height + "m")
                        self.ui.label_40.setText(no2+"ppm")
                        self.ui.label_43.setText(nh3+"ppm")
                        self.ui.label_46.setText(co+"ppm")
                        self.ui.label_5.setText(rssi + "dB")
                        Time = str(pendulum.now("Asia/Bangkok"))
                        csv_writer.writerow([Time,i, temp,humid,pressure,altitude,height,velocity,no2,nh3,co,rssi])
                        csvfile.flush()
                        time.sleep(0.5)
                        QApplication.processEvents()
                    else:
                        print("Header")
            def processing():
                with open('results.csv', 'w') as csvfile:
                  show_dashbroad(csvfile)

            serial_thread = threading.Timer(1, processing())
            serial_thread.start()
            
           

        except Exception as error:
            print(error)
        
    def serial_disconnect(self):
        
        try:
            self.device.disconnect()
            self.ui.Connect.setText("CONNECT")
            self.ui.Connect.clicked.connect(self.serial_connect)
        except Exception as error:
                print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
import sys
import glob
import serial  ## Use PySerial Module
import pendulum
import time, threading ## Time Logger
import pandas as pd  ## Data frame create
sys.path

class Serial_Interface:
   
    def __init__(self):
        self.serial_state = serial.Serial()
        self.serial_state.baudrate = 115200
        self.timeout = 0
        
    def is_connected(self):
        return self.serial_state.isOpen()
       
    
    def connect(self, port):
        self.serial_state.port = port
        self.serial_state.open()
        print("Connected")

    def disconnect(self):
        self.serial_state.close()
        print("Disconnected")
    
    def startread_data(self):
        pack = []
        self.timeout += 1
        print (self.timeout)
        serial_thread = threading.Timer(1, self.startread_data)
        if self.serial_state.is_open == True:
            serial_thread.start()
            while True:
                try:
                    c = self.serial_state.readline()
                    c = str(c)[2:-5]
                    yield c
                except KeyboardInterrupt:
                    break
                    print("stop")

              
            self.timeout = 0
                

        if self.timeout >= 10:
            self.serial_state.close()
      
  



       
      
    

 
  

   
     
        

        
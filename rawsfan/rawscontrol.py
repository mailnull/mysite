#!/usr/bin/env python
import serial
 
class rawscontrol():
    def __init__(self,device='/dev/ttyAMA0',BAUD=9600):
        self.client = serial.Serial(device,BAUD,timeout=1)
    def command(self,CMD):
        try:
            self.client.write(CMD)
            self.client.close()
        except:
            pass


#!/usr/bin/env python
# coding=utf-8
import RPi.GPIO as gpio
class Control_light():
    def __init__(self,room):
        pins = {"KTzm":38,"ZWzm":37,"CWzm":36,"KFzm":32}
        self.room=room
        if self.room in pins:
            self.pin = pins[room]
        else:
            self.pin=38
        self.gp=gpio
        self.gp.setwarnings(False)
        self.gp.setmode(self.gp.BOARD)
        self.gp.setup(self.pin,self.gp.OUT)
    def command(self,CMD):
        self.gp.output(self.pin,CMD)

    def clean(self):
        self.gp.cleanup(self.pin)

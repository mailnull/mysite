#!/usr/bin/env python
# coding=utf-8
import RPi.GPIO as gpio
#二路继电器低电平（LOW)吸合，高电平（HIGH）断开
def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(15,gpio.OUT)
def on():
    gpio.output(15,gpio.LOW)
def off():
    gpio.output(15,gpio.HIGH)
def clean():
    gpio.cleanup()
def flagwriteon():
    fp=open("/var/run/deng.pid","w")
    fp.write("0")
    fp.close()
def flagwriteoff():
    fp=open("/var/run/deng.pid","w")
    fp.write("1")
    fp.close()

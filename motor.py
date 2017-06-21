# coding:utf-8

import time
import RPi.GPIO as GPIO
import sys

RmotorA = 12
RmotorB = 16
LmotorA = 20
LmotorB = 21

GPIO.cleanup

GPIO.setmode(GPIO.BCM)
GPIO.setup(RmotorA, GPIO.OUT)
GPIO.setup(RmotorB, GPIO.OUT)
GPIO.setup(LmotorA, GPIO.OUT)
GPIO.setup(LmotorB, GPIO.OUT)

args = sys.argv
GPIO.output(RmotorA,True)
GPIO.output(RmotorB,False)
GPIO.output(LmotorA,True)
GPIO.output(LmotorB,False)
time.sleep(3)
GPIO.output(RmotorA,True)
GPIO.output(RmotorB,False)
GPIO.output(LmotorA,False)
GPIO.output(LmotorB,False)
time.sleep(3)
GPIO.output(RmotorA,False)
GPIO.output(RmotorB,False)
GPIO.output(LmotorA,True)
GPIO.output(LmotorB,False)
time.sleep(3)
GPIO.output(RmotorA,False)
GPIO.output(RmotorB,True)
GPIO.output(LmotorA,False)
GPIO.output(LmotorB,True)
time.sleep(3)
GPIO.output(RmotorA,False)
GPIO.output(RmotorB,False)
GPIO.output(LmotorA,False)
GPIO.output(LmotorB,False)
GPIO.cleanup

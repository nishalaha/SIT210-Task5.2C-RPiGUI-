from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

redLed = LED(14)
greenLed = LED(15)
blueLed = LED(21)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size =12, weight = "bold")

def ledToggler():
    if redLed.is_lit:
        redLed.off()
        redLedButton["text"] = "Turn On RED Light"
    else :
        redLed.on()
        redLedButton["text"] = "Turn Off RED Light"
        
def gledToggler():
    if greenLed.is_lit:
        greenLed.off()
        greenLedButton["text"] = "Turn On GREEN Light"
    else :
        greenLed.on()
        greenLedButton["text"] = "Turn Off GREEN Light"
        
def bledToggler():
    if blueLed.is_lit:
        blueLed.off()
        blueLedButton["text"] = "Turn On BLUE Light"
    else :
        blueLed.on()
        blueLedButton["text"] = "Turn Off BLUE Light"
        
redLedButton = Button(win, text = 'Turn ON RED', font = myFont, command = ledToggler, bg = 'bisque2', height =1, width =24)
redLedButton.grid(row =0, column =1)

greenLedButton = Button(win, text = 'Turn ON GREEN', font = myFont, command = gledToggler, bg = 'bisque2', height =1, width =24)
greenLedButton.grid(row =2, column =1)

blueLedButton = Button(win, text = 'Turn ON BLUE', font = myFont, command = bledToggler, bg = 'bisque2', height =1, width =24)
blueLedButton.grid(row =3, column =1)
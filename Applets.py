import os
from tkinter import messagebox
from tkinter import *
from time import *
from datetime import *
import calendar
import psutil
import threading
import time

def system_shutdown():
    if messagebox.askyesno(title= "System Shutdown", 
                           message="Do you want to shutdown your PipBoy?"):
        print('works')
    else:
        print('nowork')


def checktime():
    return str(strftime('%H:%M:%S %p'))


def clndr():
    return calendar.month(datetime.now().year, datetime.now().month)
    
def takenotes(a):
    inp = str(a.get("1.0", "end-1c"))
    file = os.open('notes.txt', os.O_RDWR | os.O_APPEND)
    os.write(file, str.encode(inp + '\n'))
    os.close(file)
    a.delete('1.0', END)
    a.insert("insert", "Added '%s' to notes!" % inp)

def viewnotes(a):
    file = os.open('notes.txt', os.O_RDONLY)
    a.delete('1.0', END)
    if os.path.getsize('notes.txt') != 0:
        a.insert("insert", os.read(file, 4096))
    else:
        a.insert("insert", "Notes file is empty!")

def clearnotes(a):
    file = os.open('notes.txt', os.O_TRUNC)
    os.close(file)
    a.delete('1.0', END)
    a.insert("insert", "All notes erased!")

def showkeyboard(a):
    checker = True
    counter = 0
    previous = ''
    current = ''

    while checker:
        for process in psutil.process_iter():
            previous = 'dead'
            try:
                if "viewer" in process.name():
                    print("alive")
                    previous = 'alive'
                    break
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                continue
            
            if previous == 'dead' and current == 'dead':
                checker = False
                a.attributes("-fullscreen", True)
                break
        current = previous

def keyboardstart(a):
    multit = threading.Thread(target=showkeyboard, args=(a,))
    multit.start()

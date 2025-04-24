from tkinter import *
from Applets import *
from tkinter import ttk
import subprocess
import time
import threading

mainwindow = Tk()
wbg = PhotoImage(file = 'pipbg.png')
bglabel = Label(mainwindow, image = wbg)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)
mainwindow.geometry('480x360')
mainwindow.attributes("-fullscreen", True)


infobox = Text(mainwindow, height=9, width=21)
infobox.place(x=305, y=0)
cbox = ttk.Combobox(mainwindow, width = 11, height=20, values=["Take Note", "View Notes", "Clear Notepad"])
cbox.set('Notes')
cbox.place(x=0, y=250)
cbox.bind("<<ComboboxSelected>>", lambda event:
          takenotes(infobox) if cbox.get() == 'Take Note' else (viewnotes(infobox) if cbox.get() == "View Notes" else clearnotes(infobox)))
shutdownbutton = Button(mainwindow, text = 'Shutdown', command = system_shutdown, width = 10, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')
shutdownbutton.place(x=0, y=330)

checktimebutton = Button(mainwindow, text = 'Check Time', command= 
                         lambda: infobox.insert("insert", checktime()) if infobox.compare("end-1c", "==", "1.0") 
                         else (infobox.delete('1.0', END), infobox.insert("insert", checktime())), 
                         width = 10, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')
checktimebutton.place(x=0, y=300)
clearinfobutton = Button(mainwindow, text = 'Clear Infobox', command = lambda: infobox.delete('1.0', END), width = 10, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')
clearinfobutton.place(x=0, y=0)
checkcalendar = Button(mainwindow, text = 'Calendar', command= 
                         lambda: infobox.insert("insert", clndr()) if infobox.compare("end-1c", "==", "1.0") 
                         else (infobox.delete('1.0', END), infobox.insert("insert", clndr())), 
                         width = 10, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')
checkcalendar.place(x=0, y=270)
keyboardbutton = Button(mainwindow, text = 'Show Keyboard', command = lambda: (mainwindow.attributes("-fullscreen", False), time.sleep(1), threading.Thread(target=subprocess.call, daemon=True, args = (['vncviewer'], )).start(), keyboardstart(mainwindow))
                        , width = 10, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')
keyboardbutton.place(x=108, y=0)

mainwindow.mainloop()

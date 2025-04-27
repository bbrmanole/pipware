from depends.coredepends import *

mainmenu = Window(resolution='fullscreen')
mainmenu.update_idletasks()

infobox = Text(mainmenu, height=9, width=21)
cbox = ttk.Combobox(mainmenu, width = 11, height=20, 
                    values=["Take Note", "View Notes", 
                            "Clear Notepad"])
cbox.set("Notes")
cbox.bind("<<ComboboxSelected>>", 
          lambda event:
          takenotes(infobox) 
          if cbox.get() == 'Take Note' 
          else (viewnotes(infobox) 
            if cbox.get() == "View Notes" 
            else clearnotes(infobox)))

shutdownbutton = Button(mainmenu, text="Shutdown", command=system_shutdown)
checktimebutton = Button(mainmenu, text = "Check Time", command= 
                         lambda: infobox.insert("insert", checktime()) 
                         if infobox.compare("end-1c", "==", "1.0") 
                         else (infobox.delete('1.0', END), 
                            infobox.insert("insert", checktime())))
clearinfobutton = Button(mainmenu, text = 'Clear Infobox', command = 
                         lambda: infobox.delete('1.0', END))
checkcalendarbutton = Button(mainmenu, text = 'Calendar', command= 
                         lambda: infobox.insert("insert", clndr()) if infobox.compare("end-1c", "==", "1.0") 
                         else (infobox.delete('1.0', END), infobox.insert("insert", clndr())))
keyboardbutton = Button(mainmenu, text = 'Show Keyboard', command = lambda: (mainmenu.attributes("-fullscreen", False), time.sleep(1), 
                                                                               threading.Thread(target=subprocess.call, daemon=True, args = (['matchbox-keyboard'], )).start(), 
                                                                               keyboardstart(mainmenu)))

mainmenu.touch_widget(infobox, posx_override=1, posy_override=0, anchor=NE)
mainmenu.touch_widget(clearinfobutton, posx_override=0, posy_override=0.1, anchor=W)
mainmenu.touch_widget(shutdownbutton, posx_override=0, posy_override=1, anchor=SW)
mainmenu.bind("<Configure>", lambda event: 
              (mainmenu.touch_widget(checktimebutton, posx_override=0, posy_override=(mainmenu.winfo_height()-30)/mainmenu.winfo_height(), anchor=SW), 
               mainmenu.touch_widget(checkcalendarbutton, posx_override=0, posy_override=(mainmenu.winfo_height()-60)/mainmenu.winfo_height(), anchor=SW), 
               mainmenu.touch_widget(cbox, posx_override=0, posy_override=(mainmenu.winfo_height()-90)/mainmenu.winfo_height(), anchor=SW),
               mainmenu.touch_widget(clearinfobutton, posx_override=0, posy_override=(mainmenu.winfo_height()-(mainmenu.winfo_height()-30))/mainmenu.winfo_height(), anchor=SW),
               mainmenu.touch_widget(keyboardbutton, posx_override=(mainmenu.winfo_width()-(mainmenu.winfo_width()-107))/mainmenu.winfo_width(), 
                                     posy_override=(mainmenu.winfo_height()-(mainmenu.winfo_height()-30))/mainmenu.winfo_height(), anchor=SW)))

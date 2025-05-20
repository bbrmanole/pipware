from depends.utildepends import *




def system_shutdown():
    if messagebox.askyesno(title= "System Shutdown", 
                           message="Do you want to shutdown your PipBoy?"):
        os.system('systemctl poweroff')


def checktime():
    return str(strftime('%H:%M:%S %p'))


def clndr():
    return calendar.month(datetime.now().year, datetime.now().month)
    
def takenotes(textBox):
    inp = str(textBox.get("1.0", "end-1c"))
    file = os.open('assets/notes.txt', os.O_RDWR | os.O_APPEND)
    os.write(file, str.encode(inp + '\n'))
    os.close(file)
    textBox.delete('1.0', END)
    textBox.insert("insert", "Added '%s' to notes!" % inp)

def viewnotes(textBox):
    file = os.open('assets/notes.txt', os.O_RDONLY)
    textBox.delete('1.0', END)
    if os.path.getsize('assets/notes.txt') != 0:
        textBox.insert("insert", os.read(file, 4096))
    else:
        textBox.insert("insert", "Notes file is empty!")

def clearnotes(textBox):
    file = os.open('assets/notes.txt', os.O_TRUNC)
    os.close(file)
    textBox.delete('1.0', END)
    textBox.insert("insert", "All notes erased!")

def showkeyboard(textBox):
    checker = True
    previous = ''
    current = ''

    while checker:
        for process in psutil.process_iter():
            previous = 'dead'
            try:
                if "matchbox" in process.name():
                    previous = 'alive'
                    break
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                continue
            
            if previous == 'dead' and current == 'dead':
                checker = False
                textBox.attributes("-fullscreen", True)
                break
        current = previous

def keyboardstart(textBox):
    multit = threading.Thread(target=showkeyboard, args=(textBox,))
    multit.start()


    

    
   

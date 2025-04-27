from depends.objectdepends import *

class Window(Tk):
    def __init__(self, title=None, resolution=None):
        super(Window, self).__init__()
        self.title(title)

        resolutionvalue = re.compile(r"^(\d{3,4}x\d{3,4})")
        
        if type(resolution) is not str:
            raise TypeError("resolution must be str")
        elif resolution.lower() == 'fullscreen':
            self.geometry('480x360')
            self.attributes("-fullscreen", True)
        elif not resolutionvalue.match(resolution):
            raise ResolutionValueError("\nresolution must be str, set as either 'fullscreen' or 'WIDTHxHEIGHT'")
        else:
            self.geometry(resolution)

        self.image = Image.open('assets/pipbg.jpg')
        self.image_copy = self.image.copy()

        self.background_img = ImageTk.PhotoImage(self.image)
        self.background_img_label = Label(self, image = self.background_img)
        self.background_img_label.pack(fill=BOTH, expand=YES)

        self.background_img_label.bind('<Configure>', self.resizer)
    
    def resizer(self, event):
        new_width, new_height = event.width, event.height

        self.image = self.image_copy.resize((new_width, new_height))
        self.background_img = ImageTk.PhotoImage(self.image)
        self.background_img_label.configure(image=self.background_img)

    def touch_widget(self, widget, posx_override=None, posy_override=None, 
                     anchor=None, width_override=None, height_override=None):
        if posx_override:
            widget.place(relx=posx_override, anchor=anchor)
        
        if posy_override:
            widget.place(rely=posy_override, anchor=anchor)

        if posx_override and posy_override:
            widget.place(relx=posx_override, rely=posy_override, anchor=anchor)
        
        if not posx_override and not posy_override:
            widget.pack()
        
        if type(widget) is Button:
            widget.configure(width = width_override if width_override else 10, height = height_override if height_override else None, bg = 'black', fg = 'lime'
             , activebackground = 'green', activeforeground = 'lime')

    def run(self):
        self.mainloop()
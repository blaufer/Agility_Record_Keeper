import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class MessageBox():

    #------------------------------------------------------
    def __init__(self, main, msg):
        self.message_box = tk.Toplevel(main)
        self.message_box.transient()
        self.message_box.grab_set()

        self.message_box.title('Error')

        self.label = ttk.Label(self.message_box, text=msg, justify='center')
        self.label.pack(side='top', fill='x')
        
        self.sep = ttk.Separator(self.message_box)
        self.sep.pack(side='top', fill='x')

        self.ok = ttk.Button(self.message_box, text='OK',
            command=self.quit)
        self.ok.pack(side='top')

        self.message_box.bind('<Return>', self.enterQuit)

    #------------------------------------------------------
    def quit(self):
        self.message_box.destroy()

    #------------------------------------------------------
    def enterQuit(self, event):
        self.message_box.destroy()

#----------------------------------------------------------

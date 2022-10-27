import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class RegEntry():

    #------------------------------------------------------
    def __init__(self, main):
        self.reg_entry = tk.Toplevel(main)
        self.reg_entry.transient()
        self.reg_entry.wait_visibility()
        self.reg_entry.grab_set()
        self.reg_entry.title('Title')

        # Variable
        self.venue_entered = tk.StringVar()
        self.regnum_entered = tk.StringVar()
        self.height_entered = tk.StringVar()
        self.card_received_entered = tk.StringVar()
        self.reg_info = None

        # Setup
        self.setupEntry()

    #------------------------------------------------------
    def setupEntry(self):
        # Create the frames, entry boxes, and ok/cancel button
        
        # Setup each frame
        self.frame_one = ttk.Frame(self.reg_entry)
        self.frame_one.pack(side='top', fill='x')
        
        self.frame_two = ttk.Frame(self.reg_entry)
        self.frame_two.pack(side='top', fill='x')
        
        self.frame_three = ttk.Frame(self.reg_entry)
        self.frame_three.pack(side='top', fill='x')
        
        self.frame_four = ttk.Frame(self.reg_entry)
        self.frame_four.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.reg_entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.reg_entry)
        self.ok_cancel.pack(side='top', fill='both')

        #PLACEHOLDER
        self.venue_list = ['AKC']

        # Frame one
        self.venue_label = tk.Label(self.frame_one, text='Venue')
        self.venue_label.pack(side='left')
        self.venue_entry = ttk.Combobox(self.frame_one, value=self.venue_list,
            textvariable=self.venue_entered, state='readonly')
        self.venue_entry.pack(side='left')

        # Frame two
        self.regnum_label = tk.Label(self.frame_two, text='Registration Number')
        self.regnum_label.pack(side='left')
        self.regnum_entry = ttk.Entry(self.frame_two, textvariable=self.regnum_entered)
        self.regnum_entry.pack(side='left')

        # Frame three
        self.height_label = tk.Label(self.frame_three, text='Measured Height')
        self.height_label.pack(side='left')
        self.height_entry = ttk.Entry(self.frame_three, textvariable=self.height_entered)
        self.height_entry.pack(side='left')

        # Frame four
        self.recieved = ttk.Checkbutton(self.frame_four, text='Height Card Received',
            variable=self.card_received_entered)
        self.recieved.pack(side='left')

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.submit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the registration window
        self.reg_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        venue = self.venue_entered.get()
        regnum = self.regnum_entered.get()
        height = self.height_entered.get()
        card = self.card_received_entered.get()

        self.reg_info = [venue, regnum, height, card, '']
        self.quit()
        
#----------------------------------------------------------

class EditRegEntry(RegEntry):

    #------------------------------------------------------
    def __init__(self, main, reg_info):
        super().__init__(main)
        self.reg_info = reg_info

        self.addData()

    #------------------------------------------------------
    def addData(self):
        self.venue_entry.current(0)
        self.regnum_entry.insert('end', self.reg_info[1])
        self.height_entry.insert('end', self.reg_info[2])
        if self.reg_info == 1:
            self.recieved.select()

#----------------------------------------------------------

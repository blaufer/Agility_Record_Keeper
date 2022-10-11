import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class LocNotes():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.locs_entry = tk.Toplevel(main)
        self.locs_entry.transient()
        self.locs_entry.grab_set()
        self.locs_entry.title('Locations')
        self.AD = ad

        # Variable
        self.loc_entered = tk.StringVar()
        
        # Setup
        self.setupEntry()

    #------------------------------------------------------
    def setupEntry(self):
        # Create the frames, entry boxes, and ok/cancel button

        # Setup each frame
        self.frame_one = ttk.Frame(self.locs_entry)
        self.frame_one.pack(side='top', fill='x')
        
        self.frame_two = ttk.Frame(self.locs_entry)
        self.frame_two.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.locs_entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.locs_entry)
        self.ok_cancel.pack(side='top', fill='both')

        # Frame one
        self.loc_label = tk.Label(self.frame_one, text='Location')
        self.loc_label.pack(side='left')
        self.loc_entry = ttk.Combobox(self.frame_one,
            values=sorted(self.AD.locations.keys()), textvariable=self.loc_entered)
        self.loc_entry.pack(side='left')
        self.loc_entry.bind('<Return>', self.fillNotes)
        self.loc_entry.bind('<<ComboboxSelected>>', self.fillNotes)
        
        # Frame two
        self.notes_label = tk.Label(self.frame_two, text='Notes')
        self.notes_label.pack(side='top', anchor='nw')
        self.notes_entry = tk.Text(self.frame_two, height=10)
        self.notes_entry.pack(side='bottom', fill='both')

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.submit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def fillNotes(self, event):
        self.notes_entry.delete(1.0, 'end')
        self.notes_entry.insert('end', self.AD.locations[self.loc_entered.get()])

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the location notes window
        self.locs_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data and exit
        self.loc = self.loc_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')
        self.AD.addLocation(self.loc, self.note)

        self.quit()

#----------------------------------------------------------

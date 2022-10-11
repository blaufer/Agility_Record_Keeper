import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class ClubNotes():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.clubs_entry = tk.Toplevel(main)
        self.clubs_entry.transient()
        self.clubs_entry.grab_set()
        self.clubs_entry.title('Clubs')

        self.AD = ad

        # Variable
        self.club_entered = tk.StringVar()
        
        # Setup
        self.setupEntry()

    #------------------------------------------------------
    def setupEntry(self):
        # Create the frames, entry boxes, and ok/cancel button

        # Setup each frame
        self.frame_one = ttk.Frame(self.clubs_entry)
        self.frame_one.pack(side='top', fill='x')
        
        self.frame_two = ttk.Frame(self.clubs_entry)
        self.frame_two.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.clubs_entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.clubs_entry)
        self.ok_cancel.pack(side='top', fill='both')

        # Frame one
        self.club_label = tk.Label(self.frame_one, text='Club')
        self.club_label.pack(side='left')
        self.club_entry = ttk.Combobox(self.frame_one,
            values=sorted(self.AD.clubs.keys()), textvariable=self.club_entered)
        self.club_entry.pack(side='left')
        self.club_entry.bind('<Return>', self.fillNotes)
        self.club_entry.bind('<<ComboboxSelected>>', self.fillNotes)

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
        self.notes_entry.insert('end', self.AD.clubs[self.club_entered.get()])

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the club notes window
        self.clubs_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        self.club = self.club_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')
        self.AD.addClub(self.club, self.note)

        self.quit()

#----------------------------------------------------------

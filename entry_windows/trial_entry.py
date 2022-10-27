import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc

from msg_box.message_box import MessageBox

#----------------------------------------------------------

class TrialEntry():

    #------------------------------------------------------
    def __init__(self, main, ad, canine):
        self.trial_entry = tk.Toplevel(main)
        self.trial_entry.transient()
        self.trial_entry.wait_visibility()
        self.trial_entry.grab_set()

        self.trial_entry.title('Trial')
        self.trial_entry.geometry('400x250')

        self.AD = ad
        self.canine = canine

        # Variables
        self.venue_name = tk.StringVar()
        self.club_name = tk.StringVar()
        self.loc_name = tk.StringVar()

        # Setup
        self.frameSetup()
        self.entryBoxes()

    #------------------------------------------------------
    def frameSetup(self):
        # Create the frames for the entry boxes and the ok/cancel button
        self.te1 = ttk.Frame(self.trial_entry)
        self.te1.pack(side='top', fill='x')

        self.te2 = ttk.Frame(self.trial_entry)
        self.te2.pack(side='top', fill='x')

        self.te3 = ttk.Frame(self.trial_entry)
        self.te3.pack(side='top', fill='x')

        self.te4 = ttk.Frame(self.trial_entry)
        self.te4.pack(side='top', fill='x')
 
        self.separator = ttk.Separator(self.trial_entry, orient='horizontal')
        self.separator.pack(fill='x', pady=5)
        
        self.ok_cancel = ttk.Frame(self.trial_entry)
        self.ok_cancel.pack(side='top', fill='x')

    #------------------------------------------------------
    def entryBoxes(self):
        # Add the entry boxes and ok/cancel buttons

        # Frame one
        self.date_label = tk.Label(self.te1, text='Start Date')
        self.date_label.pack(side='left')
        self.date_entry = tkc.DateEntry(self.te1, firstweekday='sunday',
            showweeknumber=False)
        self.date_entry.pack(side='left', fill='x')
        self.date_entry.delete(0, 'end')

        # Frame two
        self.venues = ['AKC'] # PLACEHOLDER
        self.clubs = sorted(self.AD.clubs.keys()) # PLACEHOLDER

        self.venue_label = tk.Label(self.te2, text='Venue')
        self.venue_label.pack(side='left')
        self.venue_entry = ttk.Combobox(self.te2, values=self.venues,
            textvariable=self.venue_name, state='readonly')
        self.venue_entry.current(0)
        self.venue_entry.pack(side='left')
        
        self.club_label = tk.Label(self.te2, text='Club')
        self.club_label.pack(side='left')
        self.club_entry = ttk.Combobox(self.te2, values=self.clubs,
            textvariable=self.club_name)
        self.club_entry.pack(side='left')

        # Frame three
        self.locs = sorted(self.AD.locations.keys()) # PLACEHOLDER

        self.loc_label = tk.Label(self.te3, text='Location')
        self.loc_label.pack(side='left')
        self.loc_entry = ttk.Combobox(self.te3, values=self.locs,
            textvariable=self.loc_name)
        self.loc_entry.pack(side='left', fill='x')

        # Frame four
        self.notes_label = tk.Label(self.te4, text='Notes')
        self.notes_label.pack(side='top', anchor='nw')
        self.notes_entry = tk.Text(self.te4, height=10)
        self.notes_entry.pack(side='bottom', fill='both')
        
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
        # Exit the calendar entry window
        self.trial_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        uid = self.AD.uniqueTrialID()
        temp = self.date_entry.get_date()
        date = f'{temp.month}/{temp.day}/{temp.year}'
        if date in list(self.AD.canine[self.canine]['Trials'].keys()):
            MessageBox(self.trial_entry, 'This date already exists as another trial,\n' \
                'were you actually at two trials at the same time?')
            return

        venue = self.venue_name.get()
        if venue == '': venue = None
        club = self.club_name.get()
        if club == '': club = None
        loc = self.loc_name.get()
        if loc == '': loc == None
        note = self.notes_entry.get('1.0', 'end-1c')
        if note == '': note = None

        self.AD.addTrial(uid, self.canine, date, club, loc, venue, note)
        
        self.quit()

#----------------------------------------------------------

class EditTrialEntry(TrialEntry):

    #------------------------------------------------------
    def __init__(self, main, ad, canine, uid):
        self.uid = uid
        super().__init__(main, ad, canine)

        self.addData()

    #------------------------------------------------------
    def addData(self):
        tdata = self.AD.trials[self.uid]
        self.date_entry.set_date(tdata['Date'])
        self.venue_entry.current(0)
        for num, item in enumerate(self.club_entry['values']):
            if tdata['Club'] == item:
                self.club_entry.current(num)
                break
        for num, item in enumerate(self.loc_entry['values']):
            if tdata['Location'] == item:
                self.club_entry.current(num)
                break
        self.notes_entry.insert('end', tdata['Notes'])
    
    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        temp = self.date_entry.get_date()
        date = f'{temp.month}/{temp.day}/{temp.year}'
        
        venue = self.venue_name.get()
        if venue == '': venue = None
        club = self.club_name.get()
        if club == '': club = None
        loc = self.loc_name.get()
        if loc == '': loc == None
        note = self.notes_entry.get('1.0', 'end-1c')
        if note == '': note = None

        self.AD.trials[self.uid] = {'Date': date,
                                    'Club': club,
                                    'Location': loc,
                                    'Venue': venue,
                                    'Note': note
                                   }
        
        self.quit()

#----------------------------------------------------------

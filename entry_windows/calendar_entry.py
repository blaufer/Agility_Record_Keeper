import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc

#----------------------------------------------------------

class CalendarEntry():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.calendar_entry = tk.Toplevel(main)
        self.calendar_entry.transient()
        self.calendar_entry.wait_visibility()
        self.calendar_entry.grab_set()

        self.calendar_entry.title('Calendar')
        
        self.AD = ad

        # Variables
        self.tent_entered = tk.IntVar()
        self.entry_entered = tk.StringVar()
        self.venue_entered = tk.StringVar()
        self.loc_entered = tk.StringVar()
        self.club_entered = tk.StringVar()
        self.sec_email_entered = tk.StringVar()

        # Setup
        self.frameSetup()
        self.entryBoxes()
    
    #------------------------------------------------------
    def frameSetup(self):
        # Create the frames for the entry boxes and the ok/cancel button

        self.ce1 = ttk.Frame(self.calendar_entry)
        self.ce1.pack(side='top', fill='x')

        self.ce2 = ttk.Frame(self.calendar_entry)
        self.ce2.pack(side='top', fill='x')

        self.ce3 = ttk.Frame(self.calendar_entry)
        self.ce3.pack(side='top', fill='x')

        self.ce4 = ttk.Frame(self.calendar_entry)
        self.ce4.pack(side='top', fill='x')

        self.ce5 = ttk.Frame(self.calendar_entry)
        self.ce5.pack(side='top', fill='x')

        self.ce6 = ttk.Frame(self.calendar_entry)
        self.ce6.pack(side='top', fill='x')

        self.ce7 = ttk.Frame(self.calendar_entry)
        self.ce7.pack(side='top', fill='x')

        self.separator = ttk.Separator(self.calendar_entry, orient='horizontal')
        self.separator.pack(fill='x')

        self.ok_cancel = ttk.Frame(self.calendar_entry)
        self.ok_cancel.pack(side='top', fill='x')

    #------------------------------------------------------
    def entryBoxes(self):
        # Add the entry boxes and ok/cancel buttons

        # Frame one
        self.start_label = tk.Label(self.ce1, text='Start Date')
        self.start_label.pack(side='left')
        self.start_entry = tkc.DateEntry(self.ce1, firstweekday='sunday',
            showweeknumber=False)
        self.start_entry.pack(side='left')

        self.open_label = tk.Label(self.ce1, text='Open Date')
        self.open_label.pack(side='left')
        self.open_entry = tkc.DateEntry(self.ce1, firstweekday='sunday',
            showweeknumber=False)
        self.open_entry.pack(side='left')

        # Frame two
        self.end_label = tk.Label(self.ce2, text='End Date')
        self.end_label.pack(side='left')
        self.end_entry = tkc.DateEntry(self.ce2, firstweekday='sunday',
            showweeknumber=False)
        self.end_entry.pack(side='left')

        self.draw_label = tk.Label(self.ce2, text='Draw Date')
        self.draw_label.pack(side='left')
        self.draw_entry = tkc.DateEntry(self.ce2, firstweekday='sunday',
            showweeknumber=False)
        self.draw_entry.pack(side='left')

        # Frame three
        self.tent_label = ttk.Checkbutton(self.ce3, text='Tentative', 
            variable=self.tent_entered)
        self.tent_label.pack(side='left')

        self.close_label = tk.Label(self.ce3, text='Close Date')
        self.close_label.pack(side='left')
        self.close_entry = tkc.DateEntry(self.ce3, firstweekday='sunday',
            showweeknumber=False)
        self.close_entry.pack(side='left')

        # Frame four
        self.entry_values = ['Not Currently','Planning', 'Entered (Pending)',
            'Entered (Confirmed)']

        self.entry_label = tk.Label(self.ce4, text='Entry')
        self.entry_label.pack(side='left')
        self.entry_box = ttk.Combobox(self.ce4, values=self.entry_values,
            textvariable=self.entry_entered, state='readonly')
        self.entry_box.pack(side='left')
        
        # Frame five
        self.venues = ['AKC']
        self.locs = sorted(self.AD.locations.keys())
        
        self.venue_label = tk.Label(self.ce5, text='Venue')
        self.venue_label.pack(side='left')
        self.venue_entry = ttk.Combobox(self.ce5, values=self.venues,
                textvariable=self.venue_entered, state='readonly')
        self.venue_entry.pack(side='left')

        self.loc_label = tk.Label(self.ce5, text='Location')
        self.loc_label.pack(side='left')
        self.loc_entry = ttk.Combobox(self.ce5, values=self.locs,
                textvariable=self.loc_entered)
        self.loc_entry.pack(side='left')

        # Frame six
        self.clubs = sorted(self.AD.clubs.keys())
        
        self.club_label = tk.Label(self.ce6, text='Club')
        self.club_label.pack(side='left')
        self.club_entry = ttk.Combobox(self.ce6, values=self.clubs,
                textvariable=self.club_entered)
        self.club_entry.pack(side='left')

        self.sec_label = tk.Label(self.ce6, text='Sec Email')
        self.sec_label.pack(side='left')
        self.sec_entry = ttk.Entry(self.ce6, textvariable=self.sec_email_entered)
        self.sec_entry.pack(side='left')

        # Frame seven
        self.notes_label = tk.Label(self.ce7, text='Notes')
        self.notes_label.pack(side='top', anchor='nw')
        self.notes_entry = tk.Text(self.ce7, height=10)
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
        self.calendar_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        self.start = self.start_entry.get_date()
        self.start = f'{self.start.month}/{self.start.day}/{self.start.year}'
        self.open = self.open_entry.get_date()
        self.open = f'{self.open.month}/{self.open.day}/{self.open.year}'
        self.end = self.end_entry.get_date()
        self.end = f'{self.end.month}/{self.end.day}/{self.end.year}'
        self.draw = self.draw_entry.get_date()
        self.draw = f'{self.draw.month}/{self.draw.day}/{self.draw.year}'
        self.tent = self.tent_entered.get()
        self.close = self.close_entry.get_date()
        self.close = f'{self.close.month}/{self.close.day}/{self.close.year}'
        self.entry = self.entry_entered.get()
        self.venue = self.venue_entered.get()
        self.loc = self.loc_entered.get()
        self.club = self.club_entered.get()
        self.sec_email = self.sec_email_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')

        self.AD.addCalendar(self.start, self.club, self.end, self.open,
            self.end, self.draw, self.tent, self.entry, self.sec_email,
            self.venue, self.loc, self.note)

        self.quit()

#----------------------------------------------------------

class EditCalendarEntry(CalendarEntry):

    #------------------------------------------------------
    def __init__(self, main, ad, key):
        self.key = key
        super().__init__(main, ad)

        self.addData()

    #------------------------------------------------------
    def addData(self):
        cdata = self.AD.calendar[self.key]
        
        self.start_entry.set_date(cdata['SDate'])
        self.open_entry.set_date(cdata['ODate'])
        self.end_entry.set_date(cdata['EDate'])
        self.draw_entry.set_date(cdata['DDate'])
        if cdata['Tentative'] == 1:
            self.tent_label.select()
        self.close_entry.set_date(cdata['CDate'])
        for num, item in enumerate(self.entry_box['values']):
            if cdata['Entry'] == item:
                self.entry_box.current(num)
                break
        for num, item in enumerate(self.venue_entry['values']):
            if cdata['Venue'] == item:
                self.venue_entry.current(num)
                break
        for num, item in enumerate(self.loc_entry['values']):
            if cdata['Location'] == item:
                self.loc_entry.current(num)
                break
        for num, item in enumerate(self.club_entry['values']):
            if cdata['Club'] == item:
                self.club_entry.current(num)
                break        
        self.sec_entry.insert('end', cdata['SecEmail'])
        self.notes_entry.insert('end', cdata['Notes'])

#----------------------------------------------------------

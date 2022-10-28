import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc

#----------------------------------------------------------

class RunEntry():

    #------------------------------------------------------
    def __init__(self, main, ad, canine, tuid):
        self.run_entry = tk.Toplevel(main)
        self.run_entry.transient()
        self.run_entry.wait_visibility()
        self.run_entry.grab_set()

        self.run_entry.title('Title')
        self.run_entry.geometry('825x325')

        self.AD = ad
        self.canine = canine
        self.tuid = tuid
        self.date = self.AD.trials[tuid]['Date']

        # Variables
        self.division_entered = tk.StringVar()
        self.level_entered = tk.StringVar()
        self.event_entered = tk.StringVar()
        self.height_entered = tk.StringVar()
        self.judge_entered = tk.StringVar()
        self.handler_entered = tk.StringVar()
        self.sct_entered = tk.StringVar()
        self.time_entered = tk.StringVar()
        self.yards_entered = tk.StringVar()
        self.obst_entered = tk.StringVar()
        self.faults_entered = tk.StringVar()
        self.place_entered = tk.StringVar()
        self.place_of_entered = tk.StringVar()
        self.qd_entered = tk.StringVar()
        self.q_entered = tk.StringVar()

        # Setup
        self.frameSetup()
        self.entryBoxes()

    #------------------------------------------------------
    def frameSetup(self):
        # Create the frames for the entry boxes and the ok/cancel buttons

        self.re1 = ttk.Frame(self.run_entry)
        self.re1.pack(side='top', fill='x')

        self.re2 = ttk.Frame(self.run_entry)
        self.re2.pack(side='top', fill='x')

        self.re3 = ttk.Frame(self.run_entry)
        self.re3.pack(side='top', fill='x')

        self.re4 = ttk.Frame(self.run_entry)
        self.re4.pack(side='top', fill='x')

        self.re5 = ttk.Frame(self.run_entry)
        self.re5.pack(side='top', fill='x')

        self.re6 = ttk.Frame(self.run_entry)
        self.re6.pack(side='top', fill='x')

        self.re7 = ttk.Frame(self.run_entry)
        self.re7.pack(side='top', fill='x')

        self.re8 = ttk.Frame(self.run_entry)
        self.re8.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.run_entry, orient='horizontal')
        self.separator.pack(fill='x', pady=5)
        
        self.ok_cancel = ttk.Frame(self.run_entry)
        self.ok_cancel.pack(side='top', fill='x')

    #------------------------------------------------------
    def entryBoxes(self):
        # Add the entry boxes and ok/cancel buttons

        # Frame one
        self.date_label = tk.Label(self.re1, text='Date')
        self.date_label.pack(side='left')
        self.date_entry = tkc.DateEntry(self.re1, firstweekday='sunday',
            showweeknumber=False)
        self.date_entry.set_date(self.date)
        self.date_entry.pack(side='left', fill='x')

        self.trial_entry = ttk.Entry(self.re1)
        self.trial_entry.insert('end',
            f"[{self.AD.trials[self.tuid]['Venue']}] {self.AD.trials[self.tuid]['Club']}")
        self.trial_entry.config(state='disabled')
        self.trial_entry.pack(side='left')

        # Only have AKC so far
        self.division_selection = ['Regular', 'Preferred']
        self.level_selection = {'Novice A': ['Standard', 'JWW', 'FAST'], 
                                'Novice B': ['Standard', 'JWW', 'FAST'], 
                                'Open': ['Standard', 'JWW', 'FAST'], 
                                'Excellent': ['Standard', 'JWW', 'FAST'],
                                'Master': ['Standard', 'JWW', 'FAST'], 
                                'T2B': ['T2B'], 
                                'Premier': ['Standard', 'JWW'], 
                                'Nationals': ['Standard', 'JWW', 'National Rounds']
                               }

        # Frame two
        self.division_label = tk.Label(self.re2, text='Division')
        self.division_label.pack(side='left')
        self.division_entry = ttk.Combobox(self.re2, value=self.division_selection,
            textvariable=self.division_entered, state='readonly')
        self.division_entry.pack(side='left')

        self.level_label = tk.Label(self.re2, text='Level')
        self.level_label.pack(side='left')
        self.level_entry = ttk.Combobox(self.re2, value=list(self.level_selection.keys()),
            textvariable=self.level_entered, state='readonly')
        self.level_entry.pack(side='left')
        
        self.event_label = tk.Label(self.re2, text='Event')
        self.event_label.pack(side='left')
        self.event_entry = ttk.Combobox(self.re2, textvariable=self.event_entered,
            state='readonly')
        self.event_entry.pack(side='left')

        self.level_entry.bind('<<ComboboxSelected>>', self.getEventData)

        # Frame three
        self.height_selection = [4, 8, 12, 16, 20, 24]
        self.judge_selection = sorted(self.AD.judges.keys())

        self.height_label = tk.Label(self.re3, text='Height')
        self.height_label.pack(side='left')
        self.height_entry = ttk.Combobox(self.re3, value=self.height_selection,
            textvariable=self.height_entered, state='readonly')
        self.height_entry.pack(side='left')

        self.judge_label = tk.Label(self.re3, text='Judge')
        self.judge_label.pack(side='left')
        self.judge_entry = ttk.Combobox(self.re3, value=self.judge_selection,
            textvariable=self.judge_entered)
        self.judge_entry.pack(side='left')

        self.handler_label = tk.Label(self.re3, text='Handler')
        self.handler_label.pack(side='left')
        self.handler_entry = ttk.Entry(self.re3, textvariable=self.handler_entered)
        self.handler_entry.pack(side='left')

        # Frame four
        self.sct_label = tk.Label(self.re4, text='Opening Time (SCT)')
        self.sct_label.pack(side='left')
        self.sct_entry = ttk.Entry(self.re4, textvariable=self.sct_entered)
        self.sct_entry.pack(side='left')

        self.time_label = tk.Label(self.re4, text='Time')
        self.time_label.pack(side='left')
        self.time_entry = ttk.Entry(self.re4, textvariable=self.time_entered)
        self.time_entry.pack(side='left')

        self.yards_label = tk.Label(self.re4, text='Yards')
        self.yards_label.pack(side='left')
        self.yards_entry = ttk.Entry(self.re4, textvariable=self.yards_entered)
        self.yards_entry.pack(side='left')

        self.obst_label = tk.Label(self.re4, text='Obstacles')
        self.obst_label.pack(side='left')
        self.obst_entry = ttk.Entry(self.re4, textvariable=self.obst_entered)
        self.obst_entry.pack(side='left')

        # Frame five
        self.faults_label = tk.Label(self.re5, text='Faults')
        self.faults_label.pack(side='left')
        self.faults_entry = ttk.Entry(self.re5, textvariable=self.faults_entered)
        self.faults_entry.pack(side='left')

        self.place_label = tk.Label(self.re5, text='Place')
        self.place_label.pack(side='left')
        self.place_entry = ttk.Entry(self.re5, textvariable=self.place_entered)
        self.place_entry.pack(side='left')
        self.place_of_label = tk.Label(self.re5, text='of')
        self.place_of_label.pack(side='left')
        self.place_of_entry = ttk.Entry(self.re5, textvariable=self.place_of_entered)
        self.place_of_entry.pack(side='left')

        # Frame six
        self.q_selection = ['Q', 'NQ', 'E', 'FEO', 'DNR', 'NA']

        self.qd_label = tk.Label(self.re6, text='Dogs Q\'d')
        self.qd_label.pack(side='left')
        self.qd_entry = ttk.Entry(self.re6, textvariable=self.qd_entered)
        self.qd_entry.pack(side='left')

        self.q_label = tk.Label(self.re6, text='Q?')
        self.q_label.pack(side='left')
        self.q_entry = ttk.Combobox(self.re6, value=self.q_selection,
            textvariable=self.q_entered, state='readonly')
        self.q_entry.pack(side='left')
        
        # Frame seven
        self.min_yps_label = tk.Label(self.re7, text='Min YPS')
        self.min_yps_label.pack(side='left')
        self.min_yps = ttk.Entry(self.re7, state='disabled')
        self.min_yps.pack(side='left')

        self.yps_label = tk.Label(self.re7, text='YPS')
        self.yps_label.pack(side='left')
        self.yps = ttk.Entry(self.re7, state='disabled')
        self.yps.pack(side='left')
        
        # NOTE: Deal with auto adding text by finding when 
        # focus changes I think

        # Frame eight
        self.notes_label = tk.Label(self.re8, text='Notes')
        self.notes_label.pack(side='top', anchor='nw')
        self.notes_entry = tk.Text(self.re8, height=10)
        self.notes_entry.pack(side='bottom', fill='both')

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.submit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def getEventData(self, event):
        # Once the level is entered, event becomes available 
        # with the correct choices
        self.event_entry['values'] = self.level_selection[self.level_entered.get()]

    #------------------------------------------------------
    def calculateMinYPS(self, event):
        # NEED TO FIGURE OUT BINDING
        # Calculates the minimum yards per second once sct
        # and yards is filled in
        try:
            self.yps['text'] = float(self.yards_entered.get()) / float(self.sct_entered.get())
        except: pass

    #------------------------------------------------------
    def calculateYPS(self, event):
        # NEED TO FIGURE OUT BINDING
        # Calculates the yards per second once actual time
        # and yards is filled in
        try:
            self.yps['text'] = float(self.yards_entered.get()) / float(self.time_entered.get())
        except: pass

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the run entry window
        self.run_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD COLLECTION DATA STUFF
        ruid = self.AD.uniqueRunID(self.canine, self.tuid)
        # Grab all the entered data then exit
        self.date = self.date_entry.get_date()
        self.date = f'{self.date.month}/{self.date.day}/{self.date.year}'
        self.division = self.division_entered.get()
        self.level = self.level_entered.get()
        self.event = self.event_entered.get()
        self.height = self.height_entered.get()
        self.judge = self.judge_entered.get()
        self.handler = self.handler_entered.get()
        self.sct = self.sct_entered.get()
        self.time = self.time_entered.get()
        self.yards = self.yards_entered.get()
        self.obst = self.obst_entered.get()
        self.faults = self.faults_entered.get()
        self.place = self.place_entered.get()
        self.place_of = self.place_of_entered.get()
        self.qd = self.qd_entered.get()
        self.q = self.q_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')

        # Needs to be calculated
        self.tpoints = None
        self.score = None

        self.AD.addRun(self.canine, self.tuid, ruid, self.date, self.event,
            self.division, self.level, self.height, self.judge, self.handler,
            self.sct, self.yards, self.obst, self.time, self.faults,
            self.place, self.place_of, self.qd, self.q, self.tpoints,
            self.score, self.note)

        self.quit()

#----------------------------------------------------------

class EditRunEntry(RunEntry):

    #------------------------------------------------------
    def __init__(self, main, ad, canine, tuid, ruid):
        self.ruid = ruid
        #print(tuid, ruid)
        super().__init__(main, ad, canine, tuid)

        self.addData()

    #------------------------------------------------------
    def addData(self):
        pass#print(self.AD.canine[self.canine]['Trials'][self.tuid])
        #rdata = self.AD.canine[self.canine]['Trials'][self.tuid][self.ruid]
        #print(rdata)

        '''
        self.date_entry

        self.date_entry = tkc.DateEntry(self.re1, firstweekday='sunday',
            showweeknumber=False)

        # Only have AKC so far
        self.division_selection = ['Regular', 'Preferred']
        self.level_selection = {'Novice A': ['Standard', 'JWW', 'FAST'], 
                                'Novice B': ['Standard', 'JWW', 'FAST'], 
                                'Open': ['Standard', 'JWW', 'FAST'], 
                                'Excellent': ['Standard', 'JWW', 'FAST'],
                                'Master': ['Standard', 'JWW', 'FAST'], 
                                'T2B': ['T2B'], 
                                'Premier': ['Standard', 'JWW'], 
                                'Nationals': ['Standard', 'JWW', 'National Rounds']
                               }

        self.division_entry = ttk.Combobox(self.re2, value=self.division_selection,
            textvariable=self.division_entered, state='readonly')
        self.level_entry = ttk.Combobox(self.re2, value=list(self.level_selection.keys()),
            textvariable=self.level_entered, state='readonly')
        self.event_entry = ttk.Combobox(self.re2, textvariable=self.event_entered,
            state='readonly')
        
        self.height_selection = [4, 8, 12, 16, 20, 24]
        self.judge_selection = sorted(self.AD.judges.keys())

        self.height_entry = ttk.Combobox(self.re3, value=self.height_selection,
            textvariable=self.height_entered, state='readonly')
        self.judge_entry = ttk.Combobox(self.re3, value=self.judge_selection,
            textvariable=self.judge_entered)
        self.handler_entry = ttk.Entry(self.re3, textvariable=self.handler_entered)
        self.sct_entry = ttk.Entry(self.re4, textvariable=self.sct_entered)
        self.time_entry = ttk.Entry(self.re4, textvariable=self.time_entered)
        self.yards_entry = ttk.Entry(self.re4, textvariable=self.yards_entered)
        self.obst_entry = ttk.Entry(self.re4, textvariable=self.obst_entered)
        self.faults_entry = ttk.Entry(self.re5, textvariable=self.faults_entered)
        self.place_entry = ttk.Entry(self.re5, textvariable=self.place_entered)
        self.place_of_entry = ttk.Entry(self.re5, textvariable=self.place_of_entered)
        # Frame six
        self.q_selection = ['Q', 'NQ', 'E', 'FEO', 'DNR', 'NA']

        self.qd_entry = ttk.Entry(self.re6, textvariable=self.qd_entered)

        self.q_entry = ttk.Combobox(self.re6, value=self.q_selection,
            textvariable=self.q_entered, state='readonly')
        self.min_yps = ttk.Entry(self.re7, state='disabled')
        self.yps = ttk.Entry(self.re7, state='disabled')
        self.notes_entry = tk.Text(self.re8, height=10)
        '''

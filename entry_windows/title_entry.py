import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc

#----------------------------------------------------------

class TitleEntry():

    #------------------------------------------------------
    def __init__(self, main, ad, canine):
        self.titles_entry = tk.Toplevel(main)
        self.titles_entry.transient()
        self.titles_entry.grab_set()
        self.titles_entry.title('Title')

        self.AD = ad
        self.canine = canine

        self.titlePossibilities()

        # Variable
        self.venue_entered = tk.StringVar()
        self.title_entered = tk.StringVar()
        
        # Setup
        self.setupEntry()

    #------------------------------------------------------
    def setupEntry(self):
        # Create the frames, entry boxes, and ok/cancel button
        
        # Setup each frame
        self.frame_one = ttk.Frame(self.titles_entry)
        self.frame_one.pack(side='top', fill='x')
        
        self.frame_two = ttk.Frame(self.titles_entry)
        self.frame_two.pack(side='top', fill='x')
        
        self.frame_three = ttk.Frame(self.titles_entry)
        self.frame_three.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.titles_entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.titles_entry)
        self.ok_cancel.pack(side='top', fill='both')

        # Frame one
        self.date_label = tk.Label(self.frame_one, text='Date')
        self.date_label.pack(side='left')
        self.date_entry = tkc.DateEntry(self.frame_one, firstweekday='sunday',
            showweeknumber=False)
        self.date_entry.pack(side='left')

        # Frame two
        self.venue_label = tk.Label(self.frame_two, text='Venue')
        self.venue_label.pack(side='left')
        self.venue_entry = ttk.Combobox(self.frame_two, value=list(self.venue_titles.keys()),
            textvariable=self.venue_entered, state='readonly')
        self.venue_entry.pack(side='left')

        # Frame three
        self.title_label = tk.Label(self.frame_three, text='Title')
        self.title_label.pack(side='left')
        self.title_entry = ttk.Combobox(self.frame_three, textvariable=self.title_entered,
            state='readonly')
        self.title_entry.pack(side='left')

        self.venue_entry.bind('<<ComboboxSelected>>', self.getEventData)

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.submit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def getEventData(self, event):
        # Once the venue is entered, title becomes available
        # with the correct choices
        self.title_entry['values'] = self.venue_titles[self.venue_entered.get()]

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the title entry window
        self.titles_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        venue = self.venue_entered.get()
        if venue == '': venue = None
        title = self.title_entered.get()
        if title == '': venue = None
        temp = self.date_entry.get_date()
        date = f'{temp.month}/{temp.day}/{temp.year}'

        self.AD.addTitle(self.canine, date, venue, title)

        self.quit()
        
    #------------------------------------------------------
    def titlePossibilities(self):
        # Titles by venue
        self.venue_titles = {'AKC': ['[NA] Novice Agility',
                                     '[OA] Open Agility',
                                     '[AX] Agility Excellent',
                                     '[MX] Master Agility Excellent',
                                     '[NAJ] Novice JWW',
                                     '[OAJ] Open JWW',
                                     '[AXJ] Agility Excellent JWW',
                                     '[MXJ] Master Excellent JWW',
                                     '[MACH] Master Agility Champion',
                                     '[NAP] Novice Agility Preferred',
                                     '[OAP] Open Agility Preferred',
                                     '[AXP] Agility Excellent Preferred',
                                     '[MXP] Master Agility Excellent Preferred',
                                     '[NJP] Novice JWW Preferred',
                                     '[OJP] Open JWW Preferred',
                                     '[AJP] Agility Excellent JWW Preferred',
                                     '[MJP] Master Excellent JWW Preferred',
                                     '[PAX] Preferred Agility Excellent',
                                     '[PACH] Preferred Agility Champion',
                                     '[NF] Novice FAST Title',
                                     '[OF] Open FAST Title',
                                     '[XF] Excellent FAST Title',
                                     '[MXF] Master Excellent FAST Title',
                                     '[TQX] Triple Q Excellent',
                                     '[FTC] FAST Century Title',
                                     '[NFP] Novice Preferred FAST Title',
                                     '[OFP] Open Preferred FAST Title',
                                     '[XFP] Excellent Preferred FAST Title',
                                     '[MFP] Master Preferred Excellent FAST Title',
                                     '[TQXP] Triple Q Excellent Preferred',
                                     '[FTCP] FAST Century Preferred Title',
                                     '[T2B] Time 2 Beat',
                                     '[T2BP] Time 2 Beat Preferred',
                                     '[MXB] Master Bronze Agility Title',
                                     '[MXS] Master Silver Agility Title',
                                     '[MXG] Master Gold Agility Title',
                                     '[MXC] Master Century Agility Title',
                                     '[MJB] Master Bronze JWW Title',
                                     '[MJS] Master Silver JWW Title',
                                     '[MJG] Master Gold JWW Title',
                                     '[MJC] Master Century JWW Title',
                                     '[MFB] Master Bronze FAST Title',
                                     '[MFS] Master Silver FAST Title',
                                     '[MFG] Master Gold FAST Title',
                                     '[MFC] Master Century FAST Title',
                                     '[MXPB] Master Bronze Agility Preferred Title',
                                     '[MXPS] Master Silver Agility Preferred Title',
                                     '[MXPG] Master Gold Agility Preferred Title',
                                     '[MXPC] Master Century Agility Preferred Title',
                                     '[MJPB] Master Bronze JWW Preferred Title',
                                     '[MJPS] Master Silver JWW Preferred Title',
                                     '[MJPG] Master Gold JWW Preferred Title',
                                     '[MJPC] Master Century JWW Preferred Title',
                                     '[MFPB] Master Bronze FAST Preferred Title',
                                     '[MFPS] Master Silver FAST Preferred Title',
                                     '[MFPG] Master Gold FAST Preferred Title',
                                     '[MFPC] Master Century FAST Preferred Title',
                                     '[PAD] Premier Agility Dog',
                                     '[PDB] Bronze Premier Agility Dog',
                                     '[PDS] Silver Premier Agility Dog',
                                     '[PDG] Gold Premier Agility Dog',
                                     '[PDC] Century Premier Agility Dog',
                                     '[PJD] Premier Jumpers Dog',
                                     '[PJB] Bronze Premier Jumpers Dog',
                                     '[PJS] Silver Premier Jumpers Dog',
                                     '[PJG] Gold Premier Jumpers Dog',
                                     '[PJC] Century Premier Jumpers Dog',
                                     '[PADP] Premier Agility Dog Preferred',
                                     '[PDBP] Bronze Premier Agility Dog Preferred',
                                     '[PDSP] Silver Premier Agility Dog Preferred',
                                     '[PDGP] Gold Premier Agility Dog Preferred',
                                     '[PDCP] Century Premier Agility Dog Preferred',
                                     '[PJDP] Premier Jumpers Dog Preferred',
                                     '[PJBP] Bronze Premier Jumpers Dog Preferred',
                                     '[PJSP] Silver Premier Jumpers Dog Preferred',
                                     '[PJGP] Gold Premier Jumpers Dog Preferred',
                                     '[PJCP] Century Premier Jumpers Dog Preferred',
                                     '[AGCH] Agility Grand Champion',
                                     '[ACT1] Agility Course Test 1',
                                     '[ACT2] Agility Course Test 2'
                                    ]
                                }

#----------------------------------------------------------

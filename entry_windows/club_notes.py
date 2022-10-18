import tkinter as tk
import tkinter.ttk as ttk

# My imports
from entry_windows.general_window import generalEntry

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
        #self.club_entered = tk.StringVar()
        
        # Setup
        self.infoPopup()

        # Bindings
        self.tree_clubs.bind('<ButtonRelease-1>', self.clubTreeBind)

    #------------------------------------------------------
    def infoPopup(self):
        # Create the frames, treeview, and buttons

        # Setup each frame
        self.frame_one = ttk.Frame(self.clubs_entry)
        self.frame_one.pack(side='top')

        self.sep = ttk.Separator(self.clubs_entry, orient='horizontal')
        self.sep.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.clubs_entry)
        self.ok_cancel.pack(side='bottom', fill='both')

        # Frame one
        self.clubTree() # Adds the tree to frame one

        self.n_button = ttk.Button(self.frame_one, text='New',
            command=self.newClub)
        self.n_button.pack()
        
        self.e_button = ttk.Button(self.frame_one, text='Edit',
                command=self.editClub, state='disable')
        self.e_button.pack()

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.quit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def clubTree(self):
        columns = ('1', '2')
        self.tree_clubs = ttk.Treeview(self.frame_one, columns=columns,
            show='headings')
        self.tree_clubs.pack(side='left')

        col_names = ['Club', 'Notes']
        for num, item in enumerate(col_names):
            self.tree_clubs.heading(columns[num], text=item)

        for k, v in self.AD.clubs.items():
            if v == None:
                v = ''
            self.tree_clubs.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def updateClubTree(self):
        self.tree_clubs.delete(*self.tree_clubs.get_children())

        for k, v in self.AD.clubs.items():
            if v == None:
                v = ''
            self.tree_clubs.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def clubTreeBind(self, event):
        # Enables Edit button if a club is selected
        foc = self.tree_clubs.focus()
        tree_item = self.tree_clubs.item

        self.club_sel = tree_item(foc)['values'][0]
        if self.club_sel in self.AD.clubs.keys():
            self.e_button['state'] = 'normal'

    #------------------------------------------------------
    def newClub(self):
        ge = generalEntry(self.clubs_entry, self.AD, 'Club')
        ge.entry.wait_window(ge.entry)
        self.updateClubTree()

    #------------------------------------------------------
    def editClub(self):
        ge = generalEntry(self.clubs_entry, self.AD, 'Club',
            self.club_sel, self.AD.clubs[self.club_sel])
        ge.entry.wait_window(ge.entry)
        self.updateClubTree()

    #------------------------------------------------------
    def quit(self):
        # Exit the club notes window
        self.clubs_entry.destroy()

#----------------------------------------------------------

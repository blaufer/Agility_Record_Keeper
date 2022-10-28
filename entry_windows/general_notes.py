import tkinter as tk
import tkinter.ttk as ttk

# My imports
from entry_windows.general_notes_sub \
    import ClubNotesSub, JudgeNotesSub, LocNotesSub

#----------------------------------------------------------

class GeneralNotes():

    #------------------------------------------------------
    def __init__(self, main, ad, title):
        self.entry = tk.Toplevel(main)
        self.entry.transient()
        self.entry.wait_visibility()
        self.entry.grab_set()
        self.title = title
        self.entry.title(self.title)
        self.entry.geometry('475x245')

        self.AD = ad

        # Setup
        self.infoPopup()

        # Bindings
        self.tree_gen.bind('<ButtonRelease-1>', self.genTreeBind)
    
    #------------------------------------------------------
    def infoPopup(self):
        # Create the frames, treeview, and buttons

        # Setup each frame
        self.frame_one = ttk.Frame(self.entry)
        self.frame_one.pack(side='top')

        self.sep = ttk.Separator(self.entry, orient='horizontal')
        self.sep.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.entry)
        self.ok_cancel.pack(side='bottom', fill='both')

        # Frame one
        self.genTree() # Adds the tree to frame one

        self.n_button = ttk.Button(self.frame_one, text='New',
            command=self.newGen)
        self.n_button.pack()
        
        self.e_button = ttk.Button(self.frame_one, text='Edit',
                command=self.editGen, state='disable')
        self.e_button.pack()

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.quit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def newGen(self):
        ge = generalNotesSub(self.entry, self.AD, self.title[:-1])
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

    #------------------------------------------------------
    def quit(self):
        # Exit the gen window
        self.entry.destroy()

#----------------------------------------------------------

class ClubNotes(GeneralNotes):
    
    #------------------------------------------------------
    def __init__(self, main, ad):
        self.title = 'Clubs'
        
        super().__init__(main, ad, self.title)

    #------------------------------------------------------
    def genTree(self):
        columns = ('1', '2')
        self.tree_gen = ttk.Treeview(self.frame_one, columns=columns,
            show='headings')
        self.tree_gen.pack(side='left')

        col_names = ['Clubs', 'Notes']
        for num, item in enumerate(col_names):
            self.tree_gen.heading(columns[num], text=item)

        for k, v in self.AD.clubs.items():
            if v == None:
                v = ''
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def updateGenTree(self):
        self.tree_gen.delete(*self.tree_gen.get_children())

        for k, v in self.AD.clubs.items():
            if v == None:
                v = ''
            elif '\n' in v:
                v = v.split('\n')[0]
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def genTreeBind(self, event):
        # Enables Edit button if a selection is made
        foc = self.tree_gen.focus()
        tree_item = self.tree_gen.item

        self.gen_sel = tree_item(foc)['values'][0]
        
        if self.gen_sel in self.AD.clubs.keys():
            self.e_button['state'] = 'normal'

    #------------------------------------------------------
    def newGen(self):
        ge = ClubNotesSub(self.entry, self.AD)
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

    #------------------------------------------------------
    def editGen(self):
        ge = ClubNotesSub(self.entry, self.AD,
            self.gen_sel, self.AD.clubs[self.gen_sel])
        
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

#----------------------------------------------------------

class JudgeNotes(GeneralNotes):

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.title = 'Judges'
        
        super().__init__(main, ad, self.title)

    #------------------------------------------------------
    def genTree(self):
        columns = ('1', '2')
        self.tree_gen = ttk.Treeview(self.frame_one, columns=columns,
            show='headings')
        self.tree_gen.pack(side='left')

        col_names = ['Judges', 'Notes']
        for num, item in enumerate(col_names):
            self.tree_gen.heading(columns[num], text=item)

        for k, v in self.AD.judges.items():
            if v == None:
                v = ''
            elif '\n' in v:
                v = v.split('\n')[0]
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def updateGenTree(self):
        self.tree_gen.delete(*self.tree_gen.get_children())

        for k, v in self.AD.judges.items():
            if v == None:
                v = ''
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def genTreeBind(self, event):
        # Enables Edit button if a selection is made
        foc = self.tree_gen.focus()
        tree_item = self.tree_gen.item

        self.gen_sel = tree_item(foc)['values'][0]
        
        if self.gen_sel in self.AD.judges.keys():
            self.e_button['state'] = 'normal'

    #------------------------------------------------------
    def newGen(self):
        ge = JudgeNotesSub(self.entry, self.AD)
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

    #------------------------------------------------------
    def editGen(self):
        ge = JudgeNotesSub(self.entry, self.AD,
            self.gen_sel, self.AD.judges[self.gen_sel])
        
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

#----------------------------------------------------------

class LocNotes(GeneralNotes):

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.title = 'Locations'
        
        super().__init__(main, ad, self.title)

    #------------------------------------------------------
    def genTree(self):
        columns = ('1', '2')
        self.tree_gen = ttk.Treeview(self.frame_one, columns=columns,
            show='headings')
        self.tree_gen.pack(side='left')

        col_names = ['Locations', 'Notes']
        for num, item in enumerate(col_names):
            self.tree_gen.heading(columns[num], text=item)

        for k, v in self.AD.locations.items():
            if v == None:
                v = ''
            elif '\n' in v:
                v = v.split('\n')[0]
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def updateGenTree(self):
        self.tree_gen.delete(*self.tree_gen.get_children())

        for k, v in self.AD.locations.items():
            if v == None:
                v = ''
            self.tree_gen.insert('', 'end', values=(k, v))
    
    #------------------------------------------------------
    def genTreeBind(self, event):
        # Enables Edit button if a selection is made
        foc = self.tree_gen.focus()
        tree_item = self.tree_gen.item

        self.gen_sel = tree_item(foc)['values'][0]
        
        if self.gen_sel in self.AD.locations.keys():
            self.e_button['state'] = 'normal'

    #------------------------------------------------------
    def newGen(self):
        ge = LocNotesSub(self.entry, self.AD)
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

    #------------------------------------------------------
    def editGen(self):
        ge = LocNotesSub(self.entry, self.AD,
            self.gen_sel, self.AD.locations[self.gen_sel])
        
        ge.entry.wait_window(ge.entry)
        self.updateGenTree()

#----------------------------------------------------------

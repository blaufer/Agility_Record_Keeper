import tkinter as tk
import tkinter.ttk as ttk

# My imports
from entry_windows.title_entry import TitleEntry

#----------------------------------------------------------

class TitleReg():

    #------------------------------------------------------
    def __init__(self, main, ad, title):
        self.entry = tk.Toplevel(main)
        self.entry.transient()
        self.entry.grab_set()
        self.title = title
        self.entry.title(self.title)

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
        
        self.e_button = ttk.Button(self.frame_one, text='Delete',
                command=self.deleteGen, state='disable')
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

class Titles(TitleReg):
    
    #------------------------------------------------------
    def __init__(self, main, ad, name):
        self.title = 'Titles'
        self.name = name
        
        super().__init__(main, ad, self.title)

    #------------------------------------------------------
    def genTree(self):
        columns = ('1', '2', '3')
        self.tree_gen = ttk.Treeview(self.frame_one, columns=columns,
            show='headings')
        self.tree_gen.pack(side='left')

        col_names = ['Venue', 'Title', 'Date']
        for num, item in enumerate(col_names):
            self.tree_gen.heading(columns[num], text=item)

        for item in self.AD.canine[self.name]['Titles']:
            self.tree_gen.insert('', 'end', values=(item['Venue'], \
                item['Title'], item['Date']))
    
    #------------------------------------------------------
    def updateGenTree(self):
        self.tree_gen.delete(*self.tree_gen.get_children())

        for item in self.AD.canine[self.name]['Titles']:
            self.tree_gen.insert('', 'end', values=(item['Venue'], \
                item['Title'], item['Date']))
    
    #------------------------------------------------------
    def genTreeBind(self, event):
        # Enables Delete button if a selection is made
        foc = self.tree_gen.focus()
        tree_item = self.tree_gen.item

        self.gen_sel = tree_item(foc)['values']
        for item in self.AD.canine[self.name]['Titles']:
            if self.gen_sel[1] == item['Title']:
                self.e_button['state'] = 'normal'
                break

    #------------------------------------------------------
    def newGen(self):
        te = TitleEntry(self.entry, self.AD, self.name)
        te.titles_entry.wait_window(te.titles_entry)
        self.updateGenTree()

    #------------------------------------------------------
    def deleteGen(self):
        for num, item in enumerate(self.AD.canine[self.name]['Titles']):
            if self.gen_sel[1] == item['Title']:
                del self.AD.canine[self.name]['Titles'][num]
                break
        
        self.updateGenTree()

#----------------------------------------------------------

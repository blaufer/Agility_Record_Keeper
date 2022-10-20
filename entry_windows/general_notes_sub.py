import tkinter as tk
import tkinter.ttk as ttk

#------------------------------------------------------
class GeneralNotesSub():

    #------------------------------------------------------
    def __init__(self, main, ad, title, name=None, notes=None):
        self.entry = tk.Toplevel(main)
        self.entry.transient()
        self.entry.grab_set()
        self.title = title
        self.entry.title(self.title)

        #self.title = title
        self.name = name
        self.notes = notes
        self.AD = ad

        # Variable
        self.gen_entered = tk.StringVar()

        # Setup
        self.genPopup()

    #------------------------------------------------------
    def genPopup(self):
        # Create the frames
        self.frame_one = ttk.Frame(self.entry)
        self.frame_one.pack(side='top', fill='x')

        self.frame_two = ttk.Frame(self.entry)
        self.frame_two.pack(side='top', fill='x')

        self.separator = ttk.Separator(self.entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.entry)
        self.ok_cancel.pack(side='top', fill='both')

        # Frame one
        self.gen_entry = tk.Entry(self.frame_one, textvariable=self.gen_entered)
        self.gen_entry.pack(fill='x')
        if self.name is not None:
            self.gen_entry.insert('end', self.name)
            self.gen_entry.config(state='disabled')

        # Frame two
        self.gen_text = tk.Text(self.frame_two, height=10)
        self.gen_text.pack(fill='x')
        if self.notes is not None:
            self.gen_text.insert('end', self.notes)

        # OK/Cancel Buttons
        self.c_button = ttk.Button(self.ok_cancel, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')

        self.ok_button = ttk.Button(self.ok_cancel, text='Ok',
            command=self.submit)
        self.ok_button.pack(side='right')

    #------------------------------------------------------
    def quit(self):
        self.entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # Grab and return stuff
        self.gen = self.gen_entry.get()
        self.text = self.gen_text.get('1.0', 'end-1c')

        if self.gen == '':
            self.quit()
            return

        if self.title == 'Club':
            self.AD.clubs[self.gen] = self.text
        elif self.title == 'Judge':
            self.AD.judges[self.gen] = self.text
        elif self.title == 'Location':
            self.AD.locations[self.gen] = self.text

        self.quit()

#----------------------------------------------------------

class ClubNotesSub(GeneralNotesSub):

    #------------------------------------------------------
    def __init__(self, main, ad, name=None, notes=None):
        self.title = 'Club'
        self.name = name
        self.notes = notes

        super().__init__(main, ad, self.title, self.name, self.notes)

    #------------------------------------------------------
    def submit(self):
        # Grab and return stuff
        self.gen = self.gen_entry.get()
        self.text = self.gen_text.get('1.0', 'end-1c')

        if self.gen == '':
            self.quit()
            return

        self.AD.clubs[self.gen] = self.text

        self.quit()
        
#----------------------------------------------------------

class JudgeNotesSub(GeneralNotesSub):

    #------------------------------------------------------
    def __init__(self, main, ad, name=None, notes=None):
        self.title = 'Judge'
        self.name = name
        self.notes = notes

        super().__init__(main, ad, self.title, self.name, self.notes)

    #------------------------------------------------------
    def submit(self):
        # Grab and return stuff
        self.gen = self.gen_entry.get()
        self.text = self.gen_text.get('1.0', 'end-1c')

        if self.gen == '':
            self.quit()
            return

        self.AD.judges[self.gen] = self.text

        self.quit()
        
#----------------------------------------------------------

class LocNotesSub(GeneralNotesSub):

    #------------------------------------------------------
    def __init__(self, main, ad, name=None, notes=None):
        self.title = 'Location'
        self.name = name
        self.notes = notes

        super().__init__(main, ad, self.title, self.name, self.notes)

    #------------------------------------------------------
    def submit(self):
        # Grab and return stuff
        self.gen = self.gen_entry.get()
        self.text = self.gen_text.get('1.0', 'end-1c')

        if self.gen == '':
            self.quit()
            return

        self.AD.locations[self.gen] = self.text

        self.quit()
        
#----------------------------------------------------------

import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class TrainingEntry():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.training_entry = tk.Toplevel(main)
        self.training_entry.transient()
        self.training_entry.wait_visibility()
        self.training_entry.grab_set()
        self.training_entry.geometry('300x205')

        self.training_entry.title('Training')

        self.AD = ad

        # Variable
        self.name_entered = tk.StringVar()
        self.subname_entered = tk.StringVar()

        # Setup
        self.frameSetup()
        self.entryBoxes()

    #------------------------------------------------------
    def frameSetup(self):
        # Create the frames for the entry boxes and the ok/cancel button

        self.te1 = ttk.Frame(self.training_entry)
        self.te1.pack(side='top', fill='x')

        self.te2 = ttk.Frame(self.training_entry)
        self.te2.pack(side='top', fill='x')

        self.te3 = ttk.Frame(self.training_entry)
        self.te3.pack(side='top', fill='x')

        # Adss a separator before the ok/cancel buttons
        self.separator = ttk.Separator(self.training_entry, orient='horizontal')
        self.separator.pack(fill='x', pady=5)

        self.ok_cancel = ttk.Frame(self.training_entry)
        self.ok_cancel.pack(side='top', fill='x')

    #------------------------------------------------------
    def entryBoxes(self):
        # Add the entry boxes and ok/cancel buttons

        # Frame one
        self.name_label = tk.Label(self.te1, text='Name')
        self.name_label.pack(side='left')
        self.name_entry = ttk.Entry(self.te1, textvariable=self.name_entered)
        self.name_entry.pack(side='left')

        # Frame two
        self.subname_label = tk.Label(self.te2, text='Subname')
        self.subname_label.pack(side='left')
        self.subname_entry = ttk.Entry(self.te2, textvariable=self.subname_entered)
        self.subname_entry.pack(side='left')

        # Frame three
        self.notes_entry = tk.Text(self.te3, height=10)
        self.notes_entry.pack(side='left', fill='both')
        
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
        # Exit the training entry window
        self.training_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        self.name = self.name_entered.get()
        self.subname = self.subname_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')
        
        self.AD.addTraining(self.name, self.subname, self.note)

        self.quit()

#----------------------------------------------------------

class EditTrainingEntry(TrainingEntry):

    #------------------------------------------------------
    def __init__(self, main, ad, key):
        self.key = key
        super().__init__(main, ad)

        self.addData()

    #------------------------------------------------------
    def addData(self):
        tdata = self.AD.training[self.key]

        self.name_entry.insert('end', self.key)
        self.subname_entry.insert('end', tdata['Subname'])
        self.notes_entry.insert('end', tdata['Notes'])

#----------------------------------------------------------



import tkinter as tk
import tkinter.ttk as ttk

#----------------------------------------------------------

class JudgeNotes():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.judges_entry = tk.Toplevel(main)
        self.judges_entry.transient()
        self.judges_entry.grab_set()
        self.judges_entry.title('Judges')
        self.AD = ad

        # Variable
        self.judge_entered = tk.StringVar()
        
        # Setup
        self.setupEntry()

    #------------------------------------------------------
    def setupEntry(self):
        # Create the frames, entry boxes, and ok/cancel button
        
        # Setup each frame
        self.frame_one = ttk.Frame(self.judges_entry)
        self.frame_one.pack(side='top', fill='x')
        
        self.frame_two = ttk.Frame(self.judges_entry)
        self.frame_two.pack(side='top', fill='x')
        
        self.separator = ttk.Separator(self.judges_entry, orient='horizontal')
        self.separator.pack(fill='x', padx=5)

        self.ok_cancel = ttk.Frame(self.judges_entry)
        self.ok_cancel.pack(side='top', fill='both')

        # Frame one
        self.judge_label = tk.Label(self.frame_one, text='Judge')
        self.judge_label.pack(side='left')
        self.judge_entry = ttk.Combobox(self.frame_one,
            values=sorted(self.AD.judges.keys()), textvariable=self.judge_entered)
        self.judge_entry.pack(side='left')
        self.judge_entry.bind('<Return>', self.fillNotes)
        self.judge_entry.bind('<<ComboboxSelected>>', self.fillNotes)

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
        self.notes_entry.insert('end', self.AD.judges[self.judge_entered.get()])

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the judge notes window
        self.judges_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        self.judge = self.judge_entered.get()
        self.note = self.notes_entry.get('1.0', 'end-1c')
        if self.judge != '':
            self.AD.addJudge(self.judge, self.note)

        self.quit()

#----------------------------------------------------------

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk

# My Imports
from data.agility_data import AgilityData
from data.settings import AgilitySettings

from tabs.canine_runs import CanineRuns
from tabs.calendar_tab import CalendarTab
from tabs.training_tab import TrainingTab

from entry_windows.canine_entry import CanineEntry, EditCanineEntry
from entry_windows.trial_entry import TrialEntry, EditTrialEntry
from entry_windows.run_entry import RunEntry, EditRunEntry
from entry_windows.calendar_entry import CalendarEntry, EditCalendarEntry
from entry_windows.training_entry import TrainingEntry, EditTrainingEntry
from entry_windows.general_notes \
    import GeneralNotes, ClubNotes, JudgeNotes, LocNotes

#----------------------------------------------------------

class AgilityApp(tk.Tk):

    #------------------------------------------------------
    def __init__(self):
        # Initialize super class
        super().__init__()

        # Start data and settings
        self.AD = AgilityData()
        self.AS = AgilitySettings()
        
        # Read in last open file
        if 'file' in self.AS.settings.keys():
            self.AD.readJSON(self.AS.settings['file'])
        self.save = None

        # Set font and text size
        self.styleSettings()

        # Add title and set geometry of initial window
        self.title('Agility App')
        self.geometry('1000x600')

        # Add dropdown menus and buttons
        # Not in it's own file for ease of passing
        # selected arguments (i.e. which canine for
        # title entry)
        self.menu_bar = self.menuBar()
        self.fileMenu()
        self.agilityMenu()
        self.notesMenu()
        self.buttonGrid()
        
        # Add separator
        self.sep = ttk.Separator(self, orient='horizontal')
        self.sep.pack(fill='x')
        
        # Add notebooks
        self.addNotebooks()

        # Runs tab setup
        self.canine_runs = CanineRuns(self, self.runs_notebook,
            self.AD)
        self.calendar_tab = CalendarTab(self, self.cal_notebook,
            self.AD)
        self.training_tab = TrainingTab(self.train_notebook,
            self.AD)

        # Run tabs classes
        self.canine_runs.runsTab()
        self.calendar_tab.calendarTab()
        self.training_tab.trainingTab()

        # Bindings
        self.protocol('WM_DELETE_WINDOW', self.quit) # Saves settings when X is clicked on
        
        self.canine_runs.tree_canine.bind('<ButtonRelease-1>',
            self.canineTreeBind)
        self.canine_runs.tree_runs.bind('<ButtonRelease-1>',
            self.canineTreeRunBind)
        # Left Tree
        self.canine_runs.tree_canine.bind('<Double-Button-1>', self.doubleClickCanineTrial)
        # Right Tree
        self.canine_runs.tree_runs.bind('<Double-Button-1>', self.doubleClickRun)

        self.calendar_tab.calendar_list.bind('<Double-Button-1>', self.doubleClickCalendar)
        self.calendar_tab.e_button.configure(command=self.doubleClickCalendar)
        self.calendar_tab.d_button.configure(command=self.deleteCalendarItem)

        self.training_tab.tree_training.bind('<Double-Button-1>', self.doubleClickTraining)
        self.training_tab.e_button.configure(command=self.doubleClickTraining)
        self.training_tab.d_button.configure(command=self.deleteTrainingItem)

    #------------------------------------------------------
    def styleSettings(self):
        # Add any settings needed to style the windows
        ttk.Style().configure('.', font=('TkDefaultFont', 12))
        ttk.Style().configure('Treeview', font=('TkDefaultFont', 10))
        ttk.Style().configure('TNotebook.Tab', font=('TkDefaultFont', 10))
        ttk.Style().configure('TButton', font=('TkDefaultFont', 10))
        ttk.Style().configure('TCheckbutton', font=('TkDefaultFont', 10))
        ttk.Style().configure('TRadiobutton', font=('TkDefaultFont', 10))

    #------------------------------------------------------
    def menuBar(self):
        # Create the general menu method
        self.menu = tk.Menu(self, bg='lightgrey', fg='black')
        self.config(menu=self.menu)

        # Add the buttons bar
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill='x')

    #------------------------------------------------------
    def fileMenu(self):
        # Setup the file dropdown

        # NOT CURRENTLY WORKING
        # File menu images
        #add_png = Image.open('add.png')
        #add_tk = ImageTk.PhotoImage(add_png)

        # Add the items to the File Menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label='New', command=self.newFile)
            #image=add_tk, compound='left', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.openFile)
        self.file_menu.add_command(label='Save', command=self.saveFile)
        self.file_menu.add_command(label='Save As', command=self.saveAs)

        # Add a seperator before Exit
        self.file_menu.add_separator()

        # Add Exit
        self.file_menu.add_command(label='Exit', command=self.quit)

        # Add to the general menu
        self.menu.add_cascade(label='File', menu=self.file_menu)

    #------------------------------------------------------
    def agilityMenu(self):
        # Setup the agility dropdown

        # Add items to the Agility Menu
        self.agility_menu = tk.Menu(self.menu, tearoff=0)
        self.agility_menu.add_command(label='Canine', command=self.addCanine)
        self.agility_menu.add_command(label='Trial', command=self.addTrial,
            state='disabled')
        self.agility_menu.add_command(label='Run', command=self.addRun,
            state='disabled')

        # Add to the general menu
        self.menu.add_cascade(label='Agility', menu=self.agility_menu)

    #------------------------------------------------------
    def notesMenu(self):
        # Setup the notes dropdown

        # Add items to the Notes Menu
        self.notes_menu = tk.Menu(self.menu, tearoff=0)
        self.notes_menu.add_command(label='Clubs', command=self.clubNotes)
        self.notes_menu.add_command(label='Judges', command=self.judgeNotes)
        self.notes_menu.add_command(label='Locations', command=self.locNotes)

        # ADD to the general menu
        self.menu.add_cascade(label='Notes', menu=self.notes_menu)

    #------------------------------------------------------
    def buttonGrid(self):
        # Setup the grid of buttons below the dropdowns
        self.canine_button = ttk.Button(self.button_frame, text='Canine',
            command=self.addCanine)
        self.canine_button.pack(side='left')

        self.separator1 = ttk.Separator(self.button_frame, orient='vertical')
        self.separator1.pack(side='left', fill='y', padx=5)

        self.reg_button = ttk.Button(self.button_frame, text='Registration',
            command=self.buttonReg, state='disable')
        self.reg_button.pack(side='left')

        self.title_button = ttk.Button(self.button_frame, text='Title',
            command=self.buttonTitles, state='disable')
        self.title_button.pack(side='left')

        self.trial_button = ttk.Button(self.button_frame, text='Trial',
            command=self.addTrial, state='disable')
        self.trial_button.pack(side='left')

        self.run_button = ttk.Button(self.button_frame, text='Run',
            command=self.addRun, state='disable')
        self.run_button.pack(side='left')

        self.separator2 = ttk.Separator(self.button_frame, orient='vertical')
        self.separator2.pack(side='left', fill='y', padx=5)

        self.calendar_button = ttk.Button(self.button_frame, text='Calendar',
            command=self.addCalendar)
        self.calendar_button.pack(side='left')

        self.training_button = ttk.Button(self.button_frame, text='Training',
            command=self.addTraining)
        self.training_button.pack(side='left')

    #------------------------------------------------------
    def addNotebooks(self):
        # Create the notebook tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=1)

        self.runs_notebook = ttk.Notebook(self)
        self.notebook.add(self.runs_notebook, text='Runs')
        
        self.points_notebook = ttk.Notebook(self)
        self.notebook.add(self.points_notebook, text='Points')

        self.cal_notebook = ttk.Notebook(self)
        self.notebook.add(self.cal_notebook, text='Calendar')
        
        self.train_notebook = ttk.Notebook(self)
        self.notebook.add(self.train_notebook, text='Training Log')

    #------------------------------------------------------
    def quit(self):
        # ADD AUTOSAVE OR ASK USER
        
        # Writes the settings file
        self.AS.writeSettings()
        self.saveFile()
        # Exits the program
        self.destroy()

    #------------------------------------------------------
    def newFile(self):
        # Creates a new file
        self.AS.removeFilename()
        self.canine_runs.clearCanineTree()

    #------------------------------------------------------
    def openFile(self):
        # Opens an existing file
        self.open = filedialog.askopenfilename(title='Open File',
            filetypes=(('json', '*.json'),('all', '*.*')))
        self.AD.readJSON(self.open)
        self.canine_runs.updateCanineTree()
        self.AS.settings['file'] = self.open

    #------------------------------------------------------
    def saveFile(self):
        # Saves to the current file
        if 'file' not in self.AS.settings.keys():
            self.saveAs()
        else:
            self.AD.writeJSON(self.AS.settings['file'])

    #------------------------------------------------------
    def saveAs(self):
        # Saves the currenct data to a new file
        self.save = filedialog.asksaveasfile(defaultextension='.json')
        self.AD.writeJSON(self.save.name)
        self.AS.settings['file'] = self.save.name

    #------------------------------------------------------
    def addCanine(self):
        # Opens the canine entry form
        ce = CanineEntry(self, self.AD)
        ce.canine_entry.wait_window(ce.canine_entry)
        self.canine_runs.updateCanineTree()

    #------------------------------------------------------
    def buttonReg(self):
        # Open canine entry at the registration tab
        ce = EditCanineEntry(self, self.AD, self.canine_runs.canine_selected)
        ce.notebook.select(ce.reg_nums)
        ce.canine_entry.wait_window(ce.canine_entry)

    #------------------------------------------------------
    def buttonTitles(self):
        # Open canine entry at the titles tab 
        ce = EditCanineEntry(self, self.AD, self.canine_runs.canine_selected)
        ce.notebook.select(ce.titles)
        ce.canine_entry.wait_window(ce.canine_entry)

    #------------------------------------------------------
    def addTrial(self):
        # Opens the trial entry form
        te = TrialEntry(self, self.AD, self.canine_runs.canine_selected)
        te.trial_entry.wait_window(te.trial_entry)
        self.canine_runs.updateCanineTree()

    #------------------------------------------------------
    def addRun(self):
        # Opens the run entry form
        re = RunEntry(self, self.AD, self.canine_runs.canine_selected,
            self.canine_runs.trial_selected)
        re.run_entry.wait_window(re.run_entry)
        self.canine_runs.runCanineData(None)

    #------------------------------------------------------
    def clubNotes(self):
        # Opens the club notes entry form
        gn = ClubNotes(self, self.AD)
        gn.entry.wait_window(gn.entry)
        
    #------------------------------------------------------
    def judgeNotes(self):
        # Opens the judge notes entry form
        gn = JudgeNotes(self, self.AD)
        gn.entry.wait_window(gn.entry)

    #------------------------------------------------------
    def locNotes(self):
        # Opens the location notes entry form
        gn = LocNotes(self, self.AD)
        gn.entry.wait_window(gn.entry)

    #------------------------------------------------------
    def addCalendar(self):
        # Opens the calendar entry form
        ce = CalendarEntry(self, self.AD)
        ce.calendar_entry.wait_window(ce.calendar_entry)
        self.calendar_tab.calendarListData()
        self.calendar_tab.calendarData()

    #------------------------------------------------------
    def addTraining(self):
        # Opens the training entry form
        te = TrainingEntry(self, self.AD)
        te.training_entry.wait_window(te.training_entry)
        self.training_tab.trainingData()

    # WORKING ON DISABLING/ENABLING BUTTONS
    #------------------------------------------------------
    def canineTreeBind(self, event):
        # Enables/diasables title, trial, and run
        # buttons/menu items
        self.canine_runs.runCanineData(event)
        self.regItem(event)
        self.titleItem(event)
        self.trialItem(event)
        self.runItem(event)

    #------------------------------------------------------
    def canineTreeRunBind(self, event):
        self.canine_runs.runSelected()

    #------------------------------------------------------
    def regItem(self, event):
        # Enables title button when a canine is selected
        self.reg_button['state'] = 'normal'
        
    #------------------------------------------------------
    def titleItem(self, event):
        # Enables title button when a canine is selected
        self.title_button['state'] = 'normal'
        
    #------------------------------------------------------
    def trialItem(self, event):
        # Enables trial button/menu item when a canine
        # is selected
        self.trial_button['state'] = 'normal'
        self.agility_menu.entryconfig('Trial', state='normal')

    #------------------------------------------------------
    def runItem(self, event):
        # Enables/diasbles run button/menu item when
        # a trial is selectd
        if self.canine_runs.trial_selected is not None:
            self.run_button['state'] = 'normal'
            self.agility_menu.entryconfig('Run', state='normal')
        else:
            self.run_button['state'] = 'disabled'
            self.agility_menu.entryconfig('Run', state='disabled')

    #------------------------------------------------------
    def doubleClickCanineTrial(self, event):
        if self.canine_runs.trial_selected is not None:
            te = EditTrialEntry(self, self.AD, self.canine_runs.canine_selected, \
                self.canine_runs.trial_selected)
            te.trial_entry.wait_window(te.trial_entry)
            self.canine_runs.updateCanineTree()
        else:
            ce = EditCanineEntry(self, self.AD, self.canine_runs.canine_selected)
            ce.canine_entry.wait_window(ce.canine_entry)
    
    #------------------------------------------------------
    def doubleClickRun(self, event):
        self.canine_runs.runSelected()
        re = EditRunEntry(self, self.AD, self.canine_runs.canine_selected,
            self.canine_runs.trial_selected, self.canine_runs.run_selected)
        re.run_entry.wait_window(re.run_entry)
        self.canine_runs.runCanineData(event)
        
    #------------------------------------------------------
    def doubleClickCalendar(self, event=None):
        self.calendar_tab.calendarItemSelected()
        ce = EditCalendarEntry(self, self.AD, self.calendar_tab.calendar_item)
        ce.calendar_entry.wait_window(ce.calendar_entry)
        self.calendar_tab.calendarListData()
        self.calendar_tab.calendarData()

    #------------------------------------------------------
    def deleteCalendarItem(self):
        self.calendar_tab.calendarItemSelected()
        self.calendar_tab.deleteCalendar()
        self.calendar_tab.calendarListData()
        self.calendar_tab.calendarData()

    #------------------------------------------------------
    def doubleClickTraining(self, event=None):
        self.training_tab.trainingSelectedItem()
        te = EditTrainingEntry(self, self.AD, self.training_tab.training_item)
        te.training_entry.wait_window(te.training_entry)
        self.training_tab.trainingData()

    #------------------------------------------------------
    def deleteTrainingItem(self):
        self.training_tab.trainingSelectedItem()
        self.training_tab.deleteTraining()
        self.training_tab.trainingData()

#----------------------------------------------------------

if __name__ == '__main__':
    app = AgilityApp()
    app.mainloop()

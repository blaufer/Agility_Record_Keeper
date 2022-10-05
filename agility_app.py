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

from entry_windows.canine_entry import CanineEntry
from entry_windows.title_entry import TitleEntry
from entry_windows.trial_entry import TrialEntry
from entry_windows.run_entry import RunEntry
from entry_windows.calendar_entry import CalendarEntry
from entry_windows.training_entry import TrainingEntry
from entry_windows.judge_notes import JudgeNotes
from entry_windows.club_notes import ClubNotes
from entry_windows.loc_notes import LocNotes

#----------------------------------------------------------

class AgilityApp(tk.Tk):

    #------------------------------------------------------
    def __init__(self):
        # Initialize super class
        super().__init__()

        # Start data
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
        # selected arguments (ie which canine for
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
        self.canine_runs.tree_canine.bind('<ButtonRelease-1>',
            self.canineTreeBind)
        self.protocol('WM_DELETE_WINDOW', self.quit)

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

        self.title_button = ttk.Button(self.button_frame, text='Title',
            command=self.addTitle, state='disable')
        self.title_button.pack(side='left')

        self.trial_button = ttk.Button(self.button_frame, text='Trial',
            command=self.addTrial, state='disable')
        self.trial_button.pack(side='left')

        self.run_button = ttk.Button(self.button_frame, text='Run',
            command=self.addRun, state='disable')
        self.run_button.pack(side='left')

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
        self.AS.writeSettings()
        # Exits the program
        self.destroy()

    #------------------------------------------------------
    def newFile(self):
        # PLACEHOLDER
        # Creates a new file
        print('New')

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
        # PLACEHOLDER
        # Saves to the current file
        if self.save == None:
            self.saveAs()
            print(self.save)
        else:
            print('Save')

    #------------------------------------------------------
    def saveAs(self):
        # PLACEHOLDER
        # Saves the currenct data to a new file
        self.save = filedialog.asksaveasfile(defaultextension='.json')
        self.AD.writeJSON(self.save.name)
        self.AS.settings['file'] = self.save.name

    #------------------------------------------------------
    # DONE
    def addCanine(self):
        # Opens the canine entry form
        ce = CanineEntry(self, self.AD)
        ce.canine_entry.wait_window(ce.canine_entry)
        self.canine_runs.updateCanineTree()

    #------------------------------------------------------
    # DONE
    def addTitle(self):
        # Opens the title entry form
        TitleEntry(self, self.AD, self.canine_runs.canine_selected)

    #------------------------------------------------------
    # DONE
    def addTrial(self):
        # Opens the trial entry form
        TrialEntry(self, self.AD, self.canine_runs.canine_selected)

    #------------------------------------------------------
    def addRun(self):
        # Opens the run entry form
        RunEntry(self)

    #------------------------------------------------------
    def clubNotes(self):
        # Opens the club notes entry form
        ClubNotes(self)

    #------------------------------------------------------
    def judgeNotes(self):
        # Opens the judge notes entry form
        JudgeNotes(self)

    #------------------------------------------------------
    def locNotes(self):
        # Opens the location notes entry form
        LocNotes(self)

    #------------------------------------------------------
    def addCalendar(self):
        # Opens the calendar entry form
        CalendarEntry(self)

    #------------------------------------------------------
    def addTraining(self):
        # Opens the training entry form
        TrainingEntry(self)
    
    # WORKING ON DISABLING/ENABLING BUTTONS
    #------------------------------------------------------
    def canineTreeBind(self, event):
        # Enables/diasables title, trial, and run
        # buttons/menu items
        self.canine_runs.runCanineData(event)
        self.titleItem(event)
        self.trialItem(event)
        self.runItem(event)

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
        if self.canine_runs.trial_selected != None:
            self.run_button['state'] = 'normal'
            self.agility_menu.entryconfig('Run', state='normal')
        else:
            self.run_button['state'] = 'disabled'
            self.agility_menu.entryconfig('Run', state='disabled')


#----------------------------------------------------------

if __name__ == '__main__':
    app = AgilityApp()
    app.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import tkcalendar as tkc

from entry_windows.title_entry import TitleEntry
from entry_windows.registration_entry import RegEntry
from msg_box.message_box import MessageBox

#----------------------------------------------------------

class CanineEntry():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.canine_entry = tk.Toplevel(main)
        self.canine_entry.transient()
        self.canine_entry.grab_set()

        self.canine_entry.title('Canine')

        self.AD = ad

        # Variables
        self.call_entry = tk.StringVar()
        self.breed_entry = tk.StringVar()
        self.reg_name_entry = tk.StringVar()
        self.deceased_entry = tk.IntVar()
        
        # Setup
        self.addNotebooks()

        # Add the separator and the ok/cancel buttons
        # Different from other forms because of the notebooks
        self.separator = ttk.Separator(self.canine_entry, orient='horizontal')
        self.separator.pack(fill='x')

        self.c_button = ttk.Button(self.canine_entry, text='Cancel',
            command=self.quit)
        self.c_button.pack(side='right')
        
        self.ok_button = ttk.Button(self.canine_entry, text='OK',
            command=self.submit)
        self.ok_button.pack(side='right')

        # Populate the notebooks
        self.properties_tab()
        self.titles_tab()
        self.reg_tab()

    #------------------------------------------------------
    def addNotebooks(self):
        # Add the tabs
        self.notebook = ttk.Notebook(self.canine_entry)
        self.notebook.pack(fill='both', expand=1)

        self.properties = ttk.Notebook(self.canine_entry)
        self.notebook.add(self.properties, text='Properties')
        
        self.titles = ttk.Notebook(self.canine_entry)
        self.notebook.add(self.titles, text='Titles')
        
        self.reg_nums = ttk.Notebook(self.canine_entry)
        self.notebook.add(self.reg_nums, text='Registration Numbers')

        # May add in later
        #self.exist_pts = ttk.Notebook(self.canine_entry)
        #self.notebook.add(self.exist_pts, text='Existing Points')

    #------------------------------------------------------
    def properties_tab(self):
        # Setup the properties tab

        # Frame one
        self.ce1 = ttk.Frame(self.properties)
        self.ce1.pack(side='top', fill='x')

        self.call_label = tk.Label(self.ce1, text='Call Name')
        self.call_label.pack(side='left')
        self.call = ttk.Entry(self.ce1, textvariable=self.call_entry)
        self.call.pack(side='left')
        
        self.breed_label = tk.Label(self.ce1, text='Breed')
        self.breed_label.pack(side='left')
        self.breed = ttk.Entry(self.ce1, textvariable=self.breed_entry)
        self.breed.pack(side='left', fill='x')

        # Frame two
        self.ce2 = ttk.Frame(self.properties)
        self.ce2.pack(side='top', fill='x')

        self.reg_label = tk.Label(self.ce2, text='Registered Name')
        self.reg_label.pack(side='left')
        self.reg = ttk.Entry(self.ce2, textvariable=self.reg_name_entry)
        self.reg.pack(fill='x')

        # Frame three
        self.ce3 = ttk.Frame(self.properties)
        self.ce3.pack(side='top', fill='x')

        self.birthday_label = tk.Label(self.ce3, text='Birthday')
        self.birthday_label.pack(side='left')
        self.birthday_entry = tkc.DateEntry(self.ce3, firstweekday='sunday',
            showweeknumbers=False)
        self.birthday_entry.pack(side='left')
        self.dec = ttk.Checkbutton(self.ce3, text='Deceased',
            variable=self.deceased_entry)
        self.dec.pack(side='left')

        # Frame four
        self.ce4 = ttk.Frame(self.properties)
        self.ce4.pack(side='top', fill='x')

        self.notes_label = tk.Label(self.ce4, text='Notes')
        self.notes_label.pack(side='top', anchor='nw')
        self.notes = tk.Text(self.ce4,
            height=10)
        self.notes.pack(side='bottom', fill='both', anchor='sw')

    #------------------------------------------------------
    def titles_tab(self):
        # Setup the titles tab

        # Create the treeview
        columns = ('1', '2', '3', '4')

        self.titles_tree = ttk.Treeview(self.titles,
            columns=columns, show='headings')
        self.titles_tree.pack(side='top', fill='both')

        # MAY NEED OTHER COLUMNS
        col_names = ['Date', 'Venue', 'Title', 'Name']

        for num, item in enumerate(col_names):
            mwidth = Font().measure(item)
            if num == len(col_names) - 1:
                self.titles_tree.column(columns[num],
                    stretch='yes', anchor='w')
            else:
                self.titles_tree.column(columns[num], width=mwidth+20,
                    stretch='no', anchor='w')
            self.titles_tree.heading(columns[num], text=item,
                anchor='w')

        # PLACEHOLDER
        self.titles_tree.insert('', 'end', values=('10/8/2021',
            'AKC', 'NA', 'Novice Agility'))
        
        # Add the buttons
        self.tt1 = ttk.Frame(self.titles)
        self.tt1.pack(side='top', fill='x')

        self.new_title = ttk.Button(self.tt1, text='New',
            command=self.addTitle)
        self.new_title.pack(side='left')

        self.edit_title = ttk.Button(self.tt1, text='Edit',
            command=self.editTitle)
        self.edit_title.pack(side='left')

        self.del_title = ttk.Button(self.tt1, text='Delete',
            command=self.delTitle)
        self.del_title.pack(side='left')

    #------------------------------------------------------
    def reg_tab(self):
        # Setup the registrations tab

        # Create the treeview
        columns = ('1', '2', '3', '4', '5')

        self.reg_tree = ttk.Treeview(self.reg_nums,
            columns=columns, show='headings')
        self.reg_tree.pack(side='top', fill='both')

        # MAY NEED OTHER COLUMNS
        col_names = ['Venue', 'Number', 'Height', 'Received', 'Note']

        for num, item in enumerate(col_names):
            mwidth = Font().measure(item)
            if num == len(col_names) - 1:
                self.reg_tree.column(columns[num],
                    stretch='yes', anchor='w')
            else:
                self.reg_tree.column(columns[num], width=mwidth+20,
                    stretch='no', anchor='w')
            self.reg_tree.heading(columns[num], text=item,
                anchor='w')

        # PLACEHOLDER
        self.reg_tree.insert('', 'end', values=('AKC', 
            'DN5458547', 18, '', ''))
        
        # Add the buttons
        self.rt1 = ttk.Frame(self.reg_nums)
        self.rt1.pack(side='top', fill='x')

        self.new_reg = ttk.Button(self.rt1, text='New',
            command=self.addReg)
        self.new_reg.pack(side='left')

        self.edit_reg = ttk.Button(self.rt1, text='Edit',
            command=self.editReg)
        self.edit_reg.pack(side='left')

        self.del_reg = ttk.Button(self.rt1, text='Delete',
            command=self.delReg)
        self.del_reg.pack(side='left')

    #------------------------------------------------------
    def quit(self):
        # ASK ABOUT SAVING BEFORE QUITTING
        # Exit the canine entry window
        self.canine_entry.destroy()

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        call_name = self.call_entry.get()
        if call_name == '':
            MessageBox(self.canine_entry, 
                'You must enter at\nleast a call name')
            return

        breed = self.breed_entry.get()
        if breed == '': breed = None
        reg_name = self.reg_name_entry.get()
        if reg_name == '': reg_name = None
        deceased = self.deceased_entry.get()
        note = self.notes.get('1.0', 'end-1c')
        if note == '': note = None
        temp = self.birthday_entry.get_date()
        birthday = f'{temp.month}/{temp.day}/{temp.year}'

        self.AD.addCanine(call_name, birthday, deceased, breed,
            reg_name, note)

        self.canine_entry.destroy()

    #------------------------------------------------------
    def addTitle(self):
        # Open the add title entry window
        TitleEntry(self.canine_entry)

    #------------------------------------------------------
    def editTitle(self):
        # Open the add title entry window?
        # PLACEHOLDER
        print('Edit Title')

    #------------------------------------------------------
    def delTitle(self):
        # Delete an entered title
        # PLACEHOLDER
        print('Delete Title')

    #------------------------------------------------------
    def addReg(self):
        # Open the add registration entry window
        RegEntry(self.canine_entry)

    #------------------------------------------------------
    def editReg(self):
        # Open the add registration entry window?
        # PLACEHOLDER
        print('Edit Reg')

    #------------------------------------------------------
    def delReg(self):
        # Delete an entered registration
        # PLACEHOLDER
        print('Delete Reg')

#----------------------------------------------------------

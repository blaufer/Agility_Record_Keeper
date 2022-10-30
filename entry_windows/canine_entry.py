import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
import tkcalendar as tkc

from entry_windows.title_entry import TitleEntry, EditTitleEntry
from entry_windows.registration_entry import RegEntry, EditRegEntry
from msg_box.message_box import MessageBox

#----------------------------------------------------------

class CanineEntry():

    #------------------------------------------------------
    def __init__(self, main, ad):
        self.canine_entry = tk.Toplevel(main)
        self.canine_entry.transient()
        self.canine_entry.wait_visibility()
        self.canine_entry.grab_set()

        self.canine_entry.title('Canine')

        self.AD = ad

        # Variables
        self.call_entry = tk.StringVar()
        self.breed_entry = tk.StringVar()
        self.reg_name_entry = tk.StringVar()
        self.deceased_entry = tk.IntVar()
        self.title_info = []
        self.reg_info = []

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
        self.propertiesTab()
        self.titlesTab()
        self.regTab()

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
    def propertiesTab(self):
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
        self.reg.pack(side='left')

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
    def titlesTab(self):
        # Setup the titles tab
        
        # Create the treeview
        columns = ('1', '2', '3')

        self.titles_tree = ttk.Treeview(self.titles,
            columns=columns, show='headings')
        self.titles_tree.pack(side='left')

        # MAY NEED OTHER COLUMNS
        col_names = ['Venue', 'Title', 'Date']
        for num, item in enumerate(col_names):
            self.titles_tree.heading(columns[num], text=item)
        self.titles_tree.column('1', width=Font().measure(col_names[0]),
            stretch='no')
        
        '''
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
        '''

        # Add Buttons
        self.new_title = ttk.Button(self.titles, text='New',
            command=self.addTitle)
        self.new_title.pack()

        self.edit_title = ttk.Button(self.titles, text='Edit',
            command=self.editTitle)
        self.edit_title.pack()

        self.del_title = ttk.Button(self.titles, text='Delete',
            command=self.delTitle)
        self.del_title.pack()
    
    #------------------------------------------------------
    def updateTitlesTree(self):
        self.titles_tree.delete(*self.titles_tree.get_children())
        for item in self.title_info:
            self.titles_tree.insert('', 'end', values=(item[1],
                item[2], item[0]))

    #------------------------------------------------------
    def regTab(self):
        # Setup the registrations tab

        # Create the treeview
        columns = ('1', '2', '3', '4', '5')

        self.reg_tree = ttk.Treeview(self.reg_nums,
            columns=columns, show='headings')
        self.reg_tree.pack(side='left')

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

        # Add Buttons
        self.new_reg = ttk.Button(self.reg_nums, text='New',
            command=self.addReg)
        self.new_reg.pack()

        self.edit_reg = ttk.Button(self.reg_nums, text='Edit',
            command=self.editReg)
        self.edit_reg.pack()

        self.del_reg = ttk.Button(self.reg_nums, text='Delete',
            command=self.delReg)
        self.del_reg.pack()

    #------------------------------------------------------
    def updateRegTree(self):
        self.reg_tree.delete(*self.reg_tree.get_children())
        for item in self.reg_info:
            self.reg_tree.insert('', 'end', values=(item[0],
                item[1], item[2], item[3], item[4]))

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
        
        # Check that call name is entered
        if call_name == '':
            MessageBox(self.canine_entry, 
                'You must enter at\nleast a call name')
            return
        
        # Check if call name already exists
        if call_name in self.AD.canine:
            MessageBox(self.canine_entry,
                'This canine already exists')
            return

        breed = self.breed_entry.get()
        if breed == '': breed = None
        reg_name = self.reg_name_entry.get()
        if reg_name == '': reg_name = None
        deceased = self.deceased_entry.get()
        note = self.notes.get('1.0', 'end-1c')
        temp = self.birthday_entry.get_date()
        birthday = f'{temp.month}/{temp.day}/{temp.year}'
        
        self.AD.addCanine(call_name, birthday, deceased, breed,
            reg_name, note)
        if len(self.title_info) > 0:
            for item in self.title_info:
                self.AD.addTitle(call_name, item[0], item[1],
                    item[2])
        if len(self.reg_info) > 0:
            for item in self.reg_info:
                self.AD.addReg(call_name, item[0], item[1], item[2],
                    item[3], item[4])

        self.canine_entry.destroy()

    #------------------------------------------------------
    def addTitle(self):
        # Open the add title entry window
        te = TitleEntry(self.canine_entry)
        te.titles_entry.wait_window(te.titles_entry)
        self.title_info.append(te.title_info)
        self.updateTitlesTree()

    #------------------------------------------------------
    def editTitle(self):
        # Open the add title entry window?
        # PLACEHOLDER
        print('Edit Title')

    #------------------------------------------------------
    def delTitle(self):
        # Delete an entered title
        foc = self.titles_tree.focus()
        tree_item = self.titles_tree.item

        vals = tree_item(foc)['values']
        match = [vals[2], vals[0], vals[1]]
        for num, item in enumerate(self.title_info):
            if item == match:
                del self.title_info[num]
                break
        self.updateTitlesTree()
    
    #------------------------------------------------------
    def addReg(self):
        # Open the add registration entry window
        re = RegEntry(self.canine_entry)
        re.reg_entry.wait_window(re.reg_entry)
        self.reg_info.append(re.reg_info)
        self.updateRegTree()

    #------------------------------------------------------
    def editReg(self):
        # Open the add registration entry window?
        # PLACEHOLDER
        print('Edit Reg')

    #------------------------------------------------------
    def delReg(self):
        # Delete an entered registration
        foc = self.reg_tree.focus()
        tree_item = self.reg_tree.item

        vals= tree_item(foc)['values']
        vals[2] = str(vals[2])
        for num, item in enumerate(self.reg_info):
            if item == vals:
                del self.reg_info[num]
                break
        self.updateRegTree()

#----------------------------------------------------------

class EditCanineEntry(CanineEntry):

    #------------------------------------------------------
    def __init__(self, main, ad, canine):
        self.canine = canine
        super().__init__(main, ad)
        
        self.addData()
        self.updateTitlesTree()
        self.updateRegTree()

    #------------------------------------------------------
    def addData(self):
        # Add the already entered info
        canine_info = self.AD.canine[self.canine]
        self.call.insert('end', self.canine)
        self.call.config(state='disabled')
        self.breed.insert('end', canine_info['Breed'])
        self.reg.insert('end', canine_info['Registered Name'])
        self.birthday_entry.set_date(canine_info['DOB'])
        if canine_info['Deceased']:
            self.dec.select()
        self.notes.insert('end', canine_info['Notes'])

    #------------------------------------------------------
    def updateTitlesTree(self):
        self.titles_tree.delete(*self.titles_tree.get_children())
        for item in self.AD.canine[self.canine]['Titles']:
            self.titles_tree.insert('', 'end', values=(item['Venue'],
                item['Title'], item['Date']))

    #------------------------------------------------------
    def updateRegTree(self):
        self.reg_tree.delete(*self.reg_tree.get_children())
        for item in self.AD.canine[self.canine]['Registration']:
            self.reg_tree.insert('', 'end', values=(item['Venue'],
                item['Number'], item['Height'], item['HC Recieved'],
                item['Note']))

    #------------------------------------------------------
    def submit(self):
        # ADD DATA COLLECTION STUFF
        # Grab all the entered data then exit
        breed = self.breed_entry.get()
        if breed == '': breed = None
        reg_name = self.reg_name_entry.get()
        if reg_name == '': reg_name = None
        deceased = self.deceased_entry.get()
        note = self.notes.get('1.0', 'end-1c')
        temp = self.birthday_entry.get_date()
        birthday = f'{temp.month}/{temp.day}/{temp.year}'
        
        self.AD.addCanine(self.canine, birthday, deceased, breed,
            reg_name, note)
        

        # FIX POSSIBLE DOUBLING
        if len(self.title_info) > 0:
            for item in self.title_info:
                self.AD.addTitle(self.canine, item[0], item[1],
                    item[2])
        if len(self.reg_info) > 0:
            for item in self.reg_info:
                self.AD.addReg(self.canine, item[0], item[1], item[2],
                    item[3], item[4])

        self.canine_entry.destroy()
    
    #------------------------------------------------------
    def addTitle(self):
        # Open the add title entry window
        te = TitleEntry(self.canine_entry)
        te.titles_entry.wait_window(te.titles_entry)
        if te.title_info is not None:
            self.AD.canine[self.canine]['Titles'].append(
                {'Date': te.title_info[0],
                 'Venue': te.title_info[1],
                 'Title': te.title_info[2]
                })
        self.updateTitlesTree()

    #------------------------------------------------------
    def editTitle(self):
        # Open the add title entry window with data filled
        foc = self.titles_tree.focus()
        tree_item = self.titles_tree.item

        vals = tree_item(foc)['values']
        match = {'Venue': vals[0], 'Title': vals[1], 'Date': vals[2]}
        for num, item in enumerate(self.AD.canine[self.canine]['Titles']):
            if item == match:
                te = EditTitleEntry(self.canine_entry, vals)
                te.titles_entry.wait_window(te.titles_entry)
                self.AD.canine[self.canine]['Titles'][num] = \
                    {'Date': te.title_info[0],
                     'Venue': te.title_info[1],
                     'Title': te.title_info[2]
                    }
                break
        self.updateTitlesTree()

    #------------------------------------------------------
    def delTitle(self):
        # Delete an entered title
        foc = self.titles_tree.focus()
        tree_item = self.titles_tree.item

        vals = tree_item(foc)['values']
        match = {'Venue': vals[0], 'Title': vals[1], 'Date': vals[2]}
        for num, item in enumerate(self.AD.canine[self.canine]['Titles']):
            if item == match:
                del self.AD.canine[self.canine]['Titles'][num]
                break
        self.updateTitlesTree()
    
    #------------------------------------------------------
    def addReg(self):
        # Open the add registration entry window
        re = RegEntry(self.canine_entry)
        re.reg_entry.wait_window(re.reg_entry)
        if re.reg_info is not None:
            self.AD.canine[self.canine]['Registration'].append(
                {'Venue': re.reg_info[0],
                 'Number': re.reg_info[1],
                 'Height': re.reg_info[2],
                 'HC Recieved': re.reg_info[3],
                 'Note': re.reg_info[4]
                })
        self.updateRegTree()

    #------------------------------------------------------
    def editReg(self):
        # Open the add registration entry window with data filled
        foc = self.reg_tree.focus()
        tree_item = self.reg_tree.item

        vals = tree_item(foc)['values']
        for num, item in enumerate(self.AD.canine[self.canine]['Registration']):
            if item['Number'] == vals[1]:
                re = EditRegEntry(self.canine_entry, vals)
                re.reg_entry.wait_window(re.reg_entry)
                self.AD.canine[self.canine]['Registration'][num] = \
                    {'Venue': re.reg_info[0],
                     'Number': re.reg_info[1],
                     'Height': re.reg_info[2],
                     'HC Recieved': re.reg_info[3],
                     'Note': re.reg_info[4]
                    }
                break
        self.updateRegTree()

    #------------------------------------------------------
    def delReg(self):
        # Delete an entered registration
        foc = self.reg_tree.focus()
        tree_item = self.reg_tree.item

        vals = tree_item(foc)['values']
        for num, item in enumerate(self.AD.canine[self.canine]['Registration']):
            if item['Number'] == vals[1]:
                del self.AD.canine[self.canine]['Registration'][num]
                break
        self.updateRegTree()

#----------------------------------------------------------

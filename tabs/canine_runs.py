import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

#----------------------------------------------------------

class CanineRuns():
    #------------------------------------------------------
    def __init__(self, main, parent, ad):
        self.main = main
        self.parent = parent
        self.AD = ad

        self.canine_selected = None
        self.trial_selected = None
        self.run_selected = None

    #------------------------------------------------------
    def runsTab(self):
        # Setup paned window with left and right
        self.runs_pane = ttk.PanedWindow(self.parent,
            orient='horizontal')

        self.canineLeft()
        self.runs_pane.add(self.tree_canine)

        self.canineRight()
        self.runs_pane.add(self.tree_runs)

        self.runs_pane.pack(fill='both', expand=1)

    #------------------------------------------------------
    def canineLeft(self):
        # Setup the canine tree which has the dog as the main tree,
        # trials under that, and then each run within the trials

        # Start the treeview
        self.tree_canine = ttk.Treeview(self.main, show='tree')
        self.tree_canine.pack(side='left')

        # NOT CURRENTLY WORKING
        # Add scrollbars
        self.tree_canine_ybar = ttk.Scrollbar(self.runs_pane,
            orient='vertical', command=self.tree_canine.yview)
        self.tree_canine_xbar = ttk.Scrollbar(self.runs_pane,
            orient='horizontal', command=self.tree_canine.xview)

        self.tree_canine.configure(yscroll=self.tree_canine_ybar.set,
            xscroll=self.tree_canine_xbar.set)

        self.tree_canine_ybar.pack(side='right', fill='y')
        self.tree_canine_ybar.pack(side='bottom', fill='x')

        # Add items to the tree
        self.treeCanineData()

    #------------------------------------------------------
    def canineRight(self):
        # Setup the runs tree which will show all runs by the dog when
        # selected or the runs for the selected trial

        # Start the treeview
        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
            '12', '13', '14', '15')
        self.tree_runs = ttk.Treeview(self.main, columns=columns, show='headings')
        self.tree_runs.pack(side='left')

        # ADD OTHERS
        col_names = ['Q', 'Title Points', 'Score', 'Date', 'Venue', 'Event',
            'Division', 'Level', 'Height', 'Judge', 'Time', 'Place',
            'In Class', 'Q\'d', 'Comments']

        for num, item in enumerate(col_names):
            mwidth = Font().measure(item)
            if num == len(col_names)-1:
                self.tree_runs.column(columns[num], width=mwidth+20,
                    stretch='yes', anchor='w')
            else:
                self.tree_runs.column(columns[num], width=mwidth+20,
                    stretch='no', anchor='center')
            self.tree_runs.heading(columns[num], text=item)
        
    #------------------------------------------------------
    def treeCanineData(self):
        # Add data to the left tree (Canine, Trial, Runs)
        
        # Holds the tree item references
        self.canine_items = {}
        # Loop through the canines
        for kc in self.AD.canine.keys():
            key = self.tree_canine.insert('', 'end', text=kc)
            self.tree_canine.item(key, open=True)
            self.canine_items[key] = {}
            # Loop through the trials
            for kt in self.AD.canine[kc]['Trials'].keys():
                keyt = self.tree_canine.insert(key, 'end', iid=kt,
                    text=f'{self.AD.trials[kt]["Date"]} {self.AD.trials[kt]["Club"]}')
                self.canine_items[key][keyt] = {}

    #------------------------------------------------------
    def runCanineData(self, event):
        # Add data to the right tree based upon which canine, or trial is selected
        foc = self.tree_canine.focus()
        tree_item = self.tree_canine.item
        tree_par = self.tree_canine.parent

        # Deletes current items in right tree
        self.tree_runs.delete(*self.tree_runs.get_children())
        
        # Canine Selected
        if tree_item(foc)['text'] in self.AD.canine.keys():
            k9 = tree_item(foc)['text']
            # Loop through trials for the selected canine
            # k is the tuid, v is the dictionary
            for k, v in self.AD.canine[k9]['Trials'].items():
                # Loop through runs
                # r is run data
                for k1, r in v.items():
                    self.tree_runs.insert('', 'end', tags=(k1, k),
                        values=(r['Q?'], r['Title Pts'], r['Score'],
                        r['Date'], self.AD.trials[k]['Venue'], r['Event'],
                        r['Division'], r['Level'], r['Height'],
                        r['Judge'], r['Time'], r['Place'],
                        r['Total Dogs'], r['Qd'], r['Notes']))
            self.canine_selected = k9
            self.trial_selected = None
        # Canine and Trial Selected
        else:
            k9 = tree_item(tree_par(foc))['text']
            tri = foc 
            # Loop through runs
            for k, r in self.AD.canine[k9]['Trials'][tri].items():
                self.tree_runs.insert('', 'end', tags=(k, tri),
                    values=(r['Q?'], r['Title Pts'], r['Score'],
                    r['Date'], self.AD.trials[tri]['Venue'], r['Event'],
                    r['Division'], r['Level'], r['Height'],
                    r['Judge'], r['Time'], r['Place'],
                    r['Total Dogs'], r['Qd'], r['Notes']))
            self.canine_selected = k9
            self.trial_selected = tri

    #------------------------------------------------------
    def updateCanineTree(self):
        self.clearCanineTree()
        for kc in self.AD.canine.keys():
            key = self.tree_canine.insert('', 'end', text=kc)
            self.tree_canine.item(key, open=True)
            self.canine_items[key] = {}
            # Loop through the trials
            for kt in self.AD.canine[kc]['Trials'].keys():
                keyt = self.tree_canine.insert(key, 'end', iid=kt,
                    text=f'{self.AD.trials[kt]["Date"]} {self.AD.trials[kt]["Club"]}')
                self.canine_items[key][keyt] = {}

    #------------------------------------------------------
    def clearCanineTree(self):
        self.tree_canine.delete(*self.tree_canine.get_children())
    
    #------------------------------------------------------
    def runSelected(self):
        foc = self.tree_runs.focus()
        tree_item = self.tree_runs.item
        self.run_selected = tree_item(foc)['tags'][0]
        self.trial_selected = tree_item(foc)['tags'][1]

#----------------------------------------------------------

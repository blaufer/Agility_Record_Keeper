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

        # Used to turn buttons/menu items
        # (title/trial/run) on or off
        self.trial_selected = False

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
            self.canine_items[key] = {}
            # Loop through the trials
            for kt in self.AD.canine[kc]['Trials'].keys():
                keyt = self.tree_canine.insert(key,
                    'end', text=f'{kt} {self.AD.canine[kc]["Trials"][kt]["Club"]}')
                self.canine_items[key][keyt] = {}
                # Loop through the runs
                for kr in self.AD.canine[kc]['Trials'][kt]['Runs'].keys():
                    keyc = self.tree_canine.insert(keyt, 'end',
                        text=f'{self.AD.canine[kc]["Trials"][kt]["Runs"][kr]["Division"]} {kr}')
                    self.canine_items[key][keyt][keyc] = {}
    
    #------------------------------------------------------
    def runCanineData(self, event):
        # Add data to the right tree based upon which canine, or trial is selected
        foc = self.tree_canine.focus()
        tree_item = self.tree_canine.item
        tree_par = self.tree_canine.parent

        # Deletes current items in right tree
        self.tree_runs.delete(*self.tree_runs.get_children())

        # Get selected item and its parents (if any)
        t1 = tree_item(foc)['text']
        p1 = tree_item(tree_par(foc))['text']
        if p1 != '':
            p2 = tree_item(tree_par(tree_par(foc)))['text']
            # If two parents, then a run is selected    
            if p2 != '':
                t1 = t1.split()[-1]
                p1 = p1.split()[0]
                runs = self.AD.canine[p2]['Trials'][p1]
                for k, v in runs['Runs'].items():
                    temp = v
                    for k1, v1 in temp.items():
                        if v1 == None:
                            temp[k1] = ''
                    self.tree_runs.insert('', 'end',
                        values=(temp['Q?'], temp['Title Pts'], temp['Score'],
                        p1, self.AD.canine[p2]['Trials'][p1]['Venue'], k,
                        temp['Division'], temp['Level'], temp['Height'],
                        temp['Judge'], temp['Time'], temp['Place'],
                        temp['Total Dogs'], temp['Qd'], temp['Notes']))
                self.canine_selected = p2
                self.trial_selected = p1
                self.run_selected = t1
                # Highlight selected run
                self.highlightRun()
            # If one parent, then a trial is selected
            else:
                t1 = t1.split()[0]
                p1 = p1.split()[-1]
                runs = self.AD.canine[p1]['Trials'][t1]
                for k, v in runs['Runs'].items():
                    temp = v
                    for k1, v1 in temp.items():
                        if v1 == None:
                            temp[k1] = ''
                    self.tree_runs.insert('', 'end',
                        values=(temp['Q?'], temp['Title Pts'], temp['Score'],
                        t1, self.AD.canine[p1]['Trials'][t1]['Venue'], k,
                        temp['Division'], temp['Level'], temp['Height'],
                        temp['Judge'], temp['Time'], temp['Place'],
                        temp['Total Dogs'], temp['Qd'], temp['Notes']))
                self.canine_selected = p1
                self.trial_selected = t1
                self.run_selected = None
        # If no parents, then it is a canine selected
        else:
            trials = self.AD.canine[t1]['Trials']
            for k2, v2 in trials.items():
                runs = v2
                for k, v in runs['Runs'].items():
                    temp = v
                    for k1, v1 in temp.items():
                        if v1 == None:
                            temp[k1] = ''
                    self.tree_runs.insert('', 'end',
                        values=(temp['Q?'], temp['Title Pts'], temp['Score'],
                        k2, self.AD.canine[t1]['Trials'][k2]['Venue'], k,
                        temp['Division'], temp['Level'], temp['Height'],
                        temp['Judge'], temp['Time'], temp['Place'],
                        temp['Total Dogs'], temp['Qd'], temp['Notes']))
            self.canine_selected = t1
            self.trial_selected = None
            self.run_selected = None

    #------------------------------------------------------
    def highlightRun(self):
        children = self.tree_runs.get_children()
        for item in children:
            if self.run_selected in self.tree_runs.item(item)['values']:
                self.tree_runs.selection_set(item)

    #------------------------------------------------------
    def updateCanineTree(self):
        self.tree_canine.delete(*self.tree_canine.get_children())
        for kc in self.AD.canine.keys():
            key = self.tree_canine.insert('', 'end', text=kc)
            self.canine_items[key] = {}
            # Loop through the trials
            for kt in self.AD.canine[kc]['Trials'].keys():
                keyt = self.tree_canine.insert(key,
                    'end', text=f'{kt} {self.AD.canine[kc]["Trials"][kt]["Club"]}')
                self.canine_items[key][keyt] = {}
                # Loop through the runs
                for kr in self.AD.canine[kc]['Trials'][kt]['Runs'].keys():
                    keyc = self.tree_canine.insert(keyt, 'end',
                        text=f'{self.AD.canine[kc]["Trials"][kt]["Runs"][kr]["Division"]} {kr}')
                    self.canine_items[key][keyt][keyc] = {}

#----------------------------------------------------------

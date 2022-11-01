import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

#----------------------------------------------------------

class TrainingTab():

    #------------------------------------------------------
    def __init__(self, parent, ad):
        self.parent = parent
        self.AD = ad

    #------------------------------------------------------
    def trainingTab(self):
        # Setup the tree that will be in the training tab
        columns = ('1', '2', '3')
        self.tree_training = ttk.Treeview(self.parent, columns=columns,
            show='headings')
        self.tree_training.pack(side='top', fill='both', expand=1)

        col_names = ['Name', 'Subname', 'Notes']

        for num, item in enumerate(col_names):
            mwidth = Font().measure(item)
            if num == len(col_names)-1:
                self.tree_training.column(columns[num], width=mwidth+20,
                    stretch='yes', anchor='w')
            else:
                self.tree_training.column(columns[num], width=mwidth+20,
                    stretch='no', anchor='center')
            self.tree_training.heading(columns[num], text=item)

        self.d_button = ttk.Button(self.parent, text='Delete')
        self.d_button.pack(side='right')

        self.e_button = ttk.Button(self.parent, text='Edit')
        self.e_button.pack(side='right')

        # Add items to the tree
        self.trainingData()

    #------------------------------------------------------
    def trainingData(self):
        self.tree_training.delete(*self.tree_training.get_children())
        for k, v in self.AD.training.items():
            self.tree_training.insert('', 'end', iid=k, values=(k,
                v['Subname'], v['Notes']))

    #------------------------------------------------------
    def trainingSelectedItem(self):
        # Find which item is selected
        self.training_item = self.tree_training.selection()[0]
        
    #------------------------------------------------------
    def deleteTraining(self):
        del self.AD.training[self.training_item]

#----------------------------------------------------------

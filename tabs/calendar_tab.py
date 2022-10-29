import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

import calendar
from datetime import datetime

#----------------------------------------------------------

class CalendarTab():
    #------------------------------------------------------
    def __init__(self, main, parent, ad):
        self.main = main
        self.parent = parent

        self.AD = ad
        
        self.month = None
        self.year = None

    #------------------------------------------------------
    def calendarTab(self):
        # Setup the paned window with left and right
        self.calendar_pane = ttk.PanedWindow(self.parent,
            orient='horizontal')

        self.calendarList()
        self.calendar_pane.add(self.calendar_list)

        self.Calendar()
        self.calendar_pane.add(self.calendar_frame)

        self.calendar_pane.pack(fill='both', expand=1)

        self.calendarListData()

    #------------------------------------------------------
    def calendarList(self):
        # Setup the left side which is the list of entered or
        # intending to enter trials

        # Start the treeview
        columns = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.calendar_list = ttk.Treeview(self.main, column=columns,
            show='headings')
        self.calendar_list.pack(side='left')

        col_names = ['Start Date', 'End Date', 'Venue', 'Club', 'Location', 'Opens', 'Closes',
            'Draws', 'Notes']

        for num, item in enumerate(col_names):
            mwidth = Font().measure(item)
            if num == len(col_names)-1:
                self.calendar_list.column(columns[num], width=mwidth+20,
                    stretch='yes', anchor='w')
            else:
                self.calendar_list.column(columns[num], width=mwidth+20,
                    stretch='no', anchor='center')
            self.calendar_list.heading(columns[num], text=item)

        # Add items to the tree
        self.calendarListData()

    #------------------------------------------------------
    def calendarListData(self):
        # Add data to the left tree
        self.calendar_list.delete(*self.calendar_list.get_children())
        for k, v in self.AD.calendar.items():
            temp = {}
            for k1, v1 in v.items():
                if v1 == None:
                    temp[k1] = ''
                else:
                    temp[k1] = v1
            self.calendar_list.insert('', 'end', tags=(k), 
                values=(temp['SDate'], temp['EDate'], temp['Venue'],
                temp['Club'], temp['Location'], temp['ODate'], 
                temp['CDate'], temp['DDate'], temp['Notes']))

    #------------------------------------------------------
    def Calendar(self):
        # Setup the right side which is an actual calendar
        # that will display the trials entered or intending
        # to enter

        self.calendar_frame = ttk.Frame(self.main)
        self.calendar_frame.pack(fill='both', expand=1)

        self.calendar_buttons = ttk.Frame(self.calendar_frame)
        self.calendar_buttons.pack(fill='x', padx=(0,5))

        # Add prev and next month buttons
        self.prev_month = ttk.Button(self.calendar_buttons,
            text='Prev Month', command=self.prevMonth)
        self.prev_month.pack(side='left')

        self.next_month = ttk.Button(self.calendar_buttons,
            text='Next Month', command=self.nextMonth)
        self.next_month.pack(side='right')

        # Start the calendar grid for the title, days, etc.
        self.calendar_grid = ttk.Frame(self.calendar_frame)
        self.calendar_grid.pack(fill='both', expand=1, padx=(0,5))

        # Get the enitre width and set each column to the 
        # same size
        title_width = self.calendar_frame.winfo_width()
        day_width = title_width / 7
        for i in range(7):
            self.calendar_grid.columnconfigure(i, minsize=day_width, weight=1,
                uniform='one')

        # Weight the rows so that the title and weekdays don't
        # expand but the days do
        for i in range(2,8):
            self.calendar_grid.rowconfigure(i, weight=3)

        # Add calendar title (month year)
        self.calendar_title = ttk.Label(self.calendar_grid,anchor='center', 
            background='white', font=('TkDefaultFont', 20))
        self.calendar_title.grid(row=0, column=0, columnspan=7, sticky='nsew')
        
        # Add days of the week
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday']
        for num, item in enumerate(days):
            ttk.Label(self.calendar_grid, text=item, relief='solid', anchor='center',
                background='white').grid(row=1, column=num, sticky='nsew')

        # Get the current month/year calendar
        self.getCalendar()

        # Set the days for the current month/year
        self.setCalendar()

        # Add events for the current month/year
        self.calendarData()

    #------------------------------------------------------
    def calendarData(self):
        # Add items to the calendar
        for k, v in self.AD.calendar.items():
            d = v['SDate'].split('/')
            if int(d[0]) == self.month and int(d[2]) == self.year:
                for k1, v1, in self.calendar_dict.items():
                    if v1.cget('text') == d[1]:
                        v1['text'] += f'\n\n{v["Club"]}'

    #------------------------------------------------------
    def getCalendar(self):
        # Use the calendar package to get the days for the wanted 
        # month/year

        # Set the month/year to the current month/year if not
        # otherwise set
        if self.month == None:
            self.month = datetime.now().month
        if self.year == None:
            self.year = datetime.now().year

        # Use calendar to get the month name from the number
        self.month_name = calendar.month_name[self.month]

        # Set the first day of the week to Sunday
        calendar.setfirstweekday(6)

        # Use calendar to get an array of the days and then
        # find the lengths of that array
        self.calendar_array = calendar.monthcalendar(self.year, self.month)
        self.cal_size = (len(self.calendar_array), len(self.calendar_array[0]))
    
    #------------------------------------------------------
    def setCalendar(self):
        # Set the days for the wanted month

        # Set the calendar title to Month YEAR
        self.calendar_title['text'] = f'{self.month_name} {self.year}'

        # Create the days in the correct spots and set them
        # to a dictionary for use to put the events in
        self.calendar_dict = {}
        for i in range(self.cal_size[1]):
            for j in range(self.cal_size[0]):
                if self.calendar_array[j][i] == 0:
                    self.calendar_dict[f'{j},{i}'] = ttk.Label(self.calendar_grid, 
                        text='', relief='solid')
                else:
                    self.calendar_dict[f'{j},{i}'] = ttk.Label(self.calendar_grid,
                        text=f'{self.calendar_array[j][i]}', relief='solid',
                        anchor='ne', background='white', justify='right')
                self.calendar_dict[f'{j},{i}'].grid(row=j+2, column=i, sticky='nsew')

    #------------------------------------------------------
    def destroyCalendar(self):
        # Remove the current calendar day settings before
        # making the next one
        for v in self.calendar_dict.values():
            v.destroy()

    #------------------------------------------------------
    def prevMonth(self):
        # Setup what to do when the Prev Month button is clicked
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        self.destroyCalendar()
        self.getCalendar()
        self.setCalendar()
        self.calendarData()

    #------------------------------------------------------
    def nextMonth(self):
        # Setup what to do when the Next Month button is clicked
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

        self.destroyCalendar()
        self.getCalendar()
        self.setCalendar()
        self.calendarData()

#----------------------------------------------------------

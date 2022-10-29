import json
import os, shutil
from uuid import uuid4
from pprint import pprint

#----------------------------------------------------------

class AgilityData():

    #------------------------------------------------------
    def __init__(self):
        # Variables
        self.canine = {}
        self.calendar = {}
        self.trials = {}
        self.training = {}
        self.venues = ['AKC']
        self.judges = {}
        self.locations = {}
        self.clubs = {}

        # Keys to the saved JSON
        self.keys = ['validate', 'canine', 'calendar', 'trials', 'training',
                     'venues', 'judges', 'clubs', 'locations']

        # Run to get blank entries
        self.blankEntries()

    #------------------------------------------------------
    def addCanine(self, name, dob, deceased, breed,
        reg_name, notes):
        # Add a new canine
        if name not in self.canine:
            self.canine[name] = self.canine_entry

        self.canine[name]['DOB'] = dob
        self.canine[name]['Deceased'] = deceased
        self.canine[name]['Breed'] = breed
        self.canine[name]['Registered Name'] = reg_name
        self.canine[name]['Notes'] = notes
    
    #------------------------------------------------------
    def addTitle(self, name, date, venue, title):
        # Add a title to the given canine
        self.canine[name]['Titles'].append(self.title_entry)

        self.canine[name]['Titles'][-1]['Date'] = date
        self.canine[name]['Titles'][-1]['Venue'] = venue
        self.canine[name]['Titles'][-1]['Title'] = title
    
    #------------------------------------------------------
    def addReg(self, name, venue, number, height,
        hc, note):
        
        # Add a registration to the given canine
        self.canine[name]['Registration'].append(self.reg_entry)

        self.canine[name]['Registration'][-1]['Venue'] = venue
        self.canine[name]['Registration'][-1]['Number'] = number
        self.canine[name]['Registration'][-1]['Height'] = height
        self.canine[name]['Registration'][-1]['HC Recieved'] = hc
        self.canine[name]['Registration'][-1]['Note'] = note
    
    #------------------------------------------------------
    def addTrial(self, uid, name, date, club, loc, venue, notes):
        # Add a trial to the given canine
        if uid not in self.trials.keys():
            self.trials[uid] = self.trials_entry
        
        self.trials[uid]['Date'] = date
        self.trials[uid]['Club'] = club
        self.addClub(club)
        self.trials[uid]['Location'] = loc
        self.addLocation(loc)
        self.trials[uid]['Venue'] = venue
        self.trials[uid]['Notes'] = notes

        self.canine[name]['Trials'][uid] = {}

    #------------------------------------------------------
    def addRun(self, name, tuid, ruid, date, event, division, level,
        height, judge, handler, sct, yards, obstacles, time, faults,
        place, tdogs, qd, q, tpoints, score, notes):
        
        # Add a run to given canine and trial
        if ruid not in self.canine[name]['Trials'][tuid].keys():
            self.canine[name]['Trials'][tuid][ruid] = self.run_entry
        
        self.canine[name]['Trials'][tuid][ruid]['Event'] = event
        self.canine[name]['Trials'][tuid][ruid]['Date'] = date
        self.canine[name]['Trials'][tuid][ruid]['Division'] = division
        self.canine[name]['Trials'][tuid][ruid]['Level'] = level
        self.canine[name]['Trials'][tuid][ruid]['Height'] = height
        self.canine[name]['Trials'][tuid][ruid]['Judge'] = judge
        self.addJudge(judge)
        self.canine[name]['Trials'][tuid][ruid]['Handler'] = handler
        self.canine[name]['Trials'][tuid][ruid]['SCT'] = sct
        self.canine[name]['Trials'][tuid][ruid]['Yards'] = yards
        self.canine[name]['Trials'][tuid][ruid]['Obstacles'] = obstacles
        self.canine[name]['Trials'][tuid][ruid]['Time'] = time
        self.canine[name]['Trials'][tuid][ruid]['Faults'] = faults
        self.canine[name]['Trials'][tuid][ruid]['Place'] = place
        self.canine[name]['Trials'][tuid][ruid]['Total Dogs'] = tdogs
        self.canine[name]['Trials'][tuid][ruid]['Qd'] = qd
        self.canine[name]['Trials'][tuid][ruid]['Q?'] = q
        self.canine[name]['Trials'][tuid][ruid]['Title Pts'] = tpoints
        self.canine[name]['Trials'][tuid][ruid]['Score'] = score
        self.canine[name]['Trials'][tuid][ruid]['Notes'] = notes

    #------------------------------------------------------
    def addCalendar(self, sdate, club, edate, odate, cdate,
        ddate, tent, entry, email, venue,
        loc, notes):

        # Add a calendar entry, start date and club are necessary
        k = f'{sdate} {club}'
        if k not in self.calendar.keys():
            self.calendar[k] = self.calendar_entry

        self.calendar[k]['SDate'] = sdate
        self.calendar[k]['Club'] = club
        self.addClub(club)
        self.calendar[k]['EDate'] = edate
        self.calendar[k]['ODate'] = edate
        self.calendar[k]['CDate'] = edate
        self.calendar[k]['DDate'] = edate
        self.calendar[k]['Tentative'] = tent
        self.calendar[k]['Entry'] = entry
        self.calendar[k]['SecEmail'] = email
        self.calendar[k]['Venue'] = venue
        self.calendar[k]['Location'] = loc
        self.addLocation(loc)
        self.calendar[k]['Notes'] = notes

    #------------------------------------------------------
    def addTraining(self, name, sname, notes):

        # Add training entry, name is necessary
        self.training[name] = self.training_entry

        self.training[name]['Subname'] = sname
        self.training[name]['Notes'] = notes

    #------------------------------------------------------
    def writeJSON(self, filename):
        # Write the JSON
        if os.path.isfile(filename):
            self.writeBackup(filename)

        # Combine all the data
        all_data = {'validate': 'Written by this program',
                    'canine': self.canine,
                    'calendar': self.calendar,
                    'trials': self.trials,
                    'training': self.training,
                    'venues': self.venues,
                    'judges': self.judges,
                    'clubs': self.clubs,
                    'locations': self.locations
                   }

        with open(filename, 'w') as f:
            json.dump(all_data, f, indent=4)

    #------------------------------------------------------
    def writeBackup(self, filename):
        # Write a backup just in case the writing a new
        # JSON fails
        shutil.copyfile(filename, f'{filename}.bck')

    #------------------------------------------------------
    def readJSON(self, filename):
        # Read in a JSON file but first check to make sure
        # it's a file and if it was written by this program
        if not os.path.isfile(filename):
            return 'Not a valid file'

        with open(filename, 'r') as f:
            all_data = json.load(f)

        try:
            if self.keys == list(all_data.keys()):
                # EDIT VALIDATION TEXT
                if all_data['validate'] == 'Written by this program':
                    pass
                else:
                    return 'Not a valid file'
            else:
                return 'Not a valid file'
        except KeyError:
            return 'Not a valid file'

        # Split up the JSON into the components
        self.canine = all_data['canine']
        self.calendar = all_data['calendar']
        self.trials = all_data['trials']
        self.training = all_data['training']
        self.venues = all_data['venues']
        self.judges = all_data['judges']
        self.clubs = all_data['clubs']
        self.locations = all_data['locations']

    #------------------------------------------------------
    def addJudge(self, judge, note=''):
        # If a judge is added to a run entry, check if
        # it's in the judges list and add if not
        if judge not in self.judges:
            self.judges[judge] = ''

        self.judges[judge] = note

    #------------------------------------------------------
    def addClub(self, club, note=''):
        # If a club is added to a trial entry, check if
        # it's in the clubs list and add if not
        if club not in self.clubs:
            self.clubs[club] = ''

        self.clubs[club] = note
    
    #------------------------------------------------------
    def addLocation(self, loc, note=''):
        # If a location is added to a trial entry, check if
        # it's in the locations list and add if not
        if loc not in self.locations:
            self.locations[loc] = ''

        self.locations[loc] = note

    #------------------------------------------------------
    def blankEntries(self):
        # Add dictionaries for each type of entry so that
        # all items will be present even if blank
        self.canine_entry = {'DOB': '',
                             'Deceased': '',
                             'Breed': '',
                             'Registered Name': '',
                             'Notes': '',
                             'Titles': [],
                             'Registration': [],
                             'Trials': {}
                            }
        self.title_entry = {'Date': '',
                            'Venue': '',
                            'Title': '',
                           }
        self.reg_entry = {'Venue': '',
                          'Number': '',
                          'Height': '',
                          'HC Recieved': '',
                          'Note': ''
                         }
        self.trials_entry = {'Date': '',
                            'Club': '',
                            'Location': '',
                            'Venue': '',
                            'Notes': ''
                           }
        self.run_entry = {'Event': '',
                          'Division': '',
                          'Date': '',
                          'Level': '',
                          'Height': '',
                          'Judge': '',
                          'Handler': '',
                          'SCT': '',
                          'Yards': '',
                          'Obstacles': '',
                          'Time': '',
                          'Faults': '',
                          'Place': '',
                          'Total Dogs': '',
                          'Qd': '',
                          'Q?': '',
                          'Title Pts': '',
                          'Score': '',
                          'Notes': ''
                         }
        self.calendar_entry = {'SDate': '',
                               'EDate': '',
                               'ODate': '',
                               'CDate': '',
                               'DDate': '',
                               'Tentative': '',
                               'Entry': '',
                               'SecEmail': '',
                               'Venue': '',
                               'Club': '',
                               'Location': '',
                               'Notes': ''
                              }
        self.training_entry = {'Subname': '',
                               'Notes': ''
                              }

    #------------------------------------------------------
    def uniqueTrialID(self):
        while True:
            uid = str(uuid4())
            if uid not in self.trials.keys():
                break
        
        return uid

    #------------------------------------------------------
    def uniqueRunID(self, canine, tuid):
        while True:
            uid = str(uuid4())
            if uid not in self.canine[canine]['Trials'][tuid].keys():
                break
        
        return uid

#----------------------------------------------------------

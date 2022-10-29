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
    def addCanine(self, name, dob=None, deceased=None, breed=None,
        reg_name=None, notes=None, titles=None):
        # Add a new canine
        if name not in self.canine:
            self.canine[name] = self.canine_entry

        if dob != None:
            self.canine[name]['DOB'] = dob
        if deceased != None:
            self.canine[name]['Deceased'] = deceased
        if breed != None:
            self.canine[name]['Breed'] = breed
        if reg_name != None:
            self.canine[name]['Registered Name'] = reg_name
        if notes != None:
            self.canine[name]['Notes'] = notes
        if titles != None:
            self.canine[name]['Titles'].append(titles)
    
    #------------------------------------------------------
    def addTitle(self, name, date=None, venue=None, title=None):
        # Add a title to the given canine
        self.canine[name]['Titles'].append(self.title_entry)

        self.canine[name]['Titles'][-1]['Date'] = date
        self.canine[name]['Titles'][-1]['Venue'] = venue
        self.canine[name]['Titles'][-1]['Title'] = title
    
    #------------------------------------------------------
    def addReg(self, name, venue=None, number=None, height=None,
        hc=None, note=None):
        
        # Add a registration to the given canine
        self.canine[name]['Registration'].append(self.reg_entry)

        self.canine[name]['Registration'][-1]['Venue'] = venue
        self.canine[name]['Registration'][-1]['Number'] = number
        self.canine[name]['Registration'][-1]['Height'] = height
        self.canine[name]['Registration'][-1]['HC Recieved'] = hc
        self.canine[name]['Registration'][-1]['Note'] = note
    
    #------------------------------------------------------
    def addTrial(self, uid, name, date=None, club=None, loc=None, venue=None, notes=None):
        # Add a trial to the given canine
        if uid not in self.trials.keys():
            self.trials[uid] = self.trials_entry
        if date != None:
            self.trials[uid]['Date'] = date
        if club != None:
            self.trials[uid]['Club'] = club
            self.addClub(club)
        if loc != None:
            self.trials[uid]['Location'] = loc
            self.addLocation(loc)
        if venue != None:
            self.trials[uid]['Venue'] = venue
        if notes != None:
            self.trials[uid]['Notes'] = notes

        self.canine[name]['Trials'][uid] = {}

    #------------------------------------------------------
    def addRun(self, name, tuid, ruid, date, event, division=None, level=None, height=None,
        judge=None, handler=None, sct=None, yards=None, obstacles=None, time=None, faults=None,
        place=None, tdogs=None, qd=None, q=None, tpoints=None, score=None, notes=None):
        
        # Add a run to given canine and trial
        if ruid not in self.canine[name]['Trials'][tuid].keys():
            self.canine[name]['Trials'][tuid][ruid] = self.run_entry
        self.canine[name]['Trials'][tuid][ruid]['Event'] = event
        self.canine[name]['Trials'][tuid][ruid]['Date'] = date
        if division is not None:
            self.canine[name]['Trials'][tuid][ruid]['Division'] = division
        if level is not None:
            self.canine[name]['Trials'][tuid][ruid]['Level'] = level
        if height is not None:
            self.canine[name]['Trials'][tuid][ruid]['Height'] = height
        if judge is not None:
            self.canine[name]['Trials'][tuid][ruid]['Judge'] = judge
            self.addJudge(judge)
        if handler is not None:
            self.canine[name]['Trials'][tuid][ruid]['Handler'] = handler
        if sct is not None:
            self.canine[name]['Trials'][tuid][ruid]['SCT'] = sct
        if yards is not None:
            self.canine[name]['Trials'][tuid][ruid]['Yards'] = yards
        if obstacles is not None:
            self.canine[name]['Trials'][tuid][ruid]['Obstacles'] = obstacles
        if time is not None:
            self.canine[name]['Trials'][tuid][ruid]['Time'] = time
        if faults is not None:
            self.canine[name]['Trials'][tuid][ruid]['Faults'] = faults
        if place is not None:
            self.canine[name]['Trials'][tuid][ruid]['Place'] = place
        if tdogs is not None:
            self.canine[name]['Trials'][tuid][ruid]['Total Dogs'] = tdogs
        if qd is not None:
            self.canine[name]['Trials'][tuid][ruid]['Qd'] = qd
        if q is not None:
            self.canine[name]['Trials'][tuid][ruid]['Q?'] = q
        if tpoints is not None:
            self.canine[name]['Trials'][tuid][ruid]['Title Pts'] = tpoints
        if score is not None:
            self.canine[name]['Trials'][tuid][ruid]['Score'] = score
        if notes is not None:
            self.canine[name]['Trials'][tuid][ruid]['Notes'] = notes

    #------------------------------------------------------
    def addCalendar(self, sdate, club, edate=None, odate=None, cdate=None,
        ddate=None, tent=None, entry=None, email=None, venue=None,
        loc=None, notes=None):

        # Add a calendar entry, start date and club are necessary
        k = f'{sdate} {club}'
        if k not in self.calendar.keys():
            self.calendar[k] = self.calendar_entry

        self.calendar[k]['SDate'] = sdate
        self.calendar[k]['Club'] = club

        if edate != None:
            self.calendar[k]['EDate'] = edate
        if odate != None:
            self.calendar[k]['ODate'] = edate
        if cdate != None:
            self.calendar[k]['CDate'] = edate
        if ddate != None:
            self.calendar[k]['DDate'] = edate
        if tent != None:
            self.calendar[k]['Tentative'] = tent
        if entry != None:
            self.calendar[k]['Entry'] = entry
        if email != None:
            self.calendar[k]['SecEmail'] = email
        if venue != None:
            self.calendar[k]['Venue'] = venue
        if loc != None:
            self.calendar[k]['Location'] = loc
        if notes != None:
            self.calendar[k]['Notes'] = notes

    #------------------------------------------------------
    def addTraining(self, name, sname='', notes=''):

        # Add training entry, name is necessary
        self.training[name] = self.training_entry

        if sname != '':
            self.training[name]['Subname'] = sname
        if notes != '':
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

        if note != '':
            self.judges[judge] = note

    #------------------------------------------------------
    def addClub(self, club, note=''):
        # If a club is added to a trial entry, check if
        # it's in the clubs list and add if not
        if club not in self.clubs:
            self.clubs[club] = ''

        if note != '':
            self.clubs[club] = note
    
    #------------------------------------------------------
    def addLocation(self, loc, note=''):
        # If a location is added to a trial entry, check if
        # it's in the locations list and add if not
        if loc not in self.locations:
            self.locations[loc] = ''

        if note != '':
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

    #------------------------------------------------------
    def tempPrint(self):
        print(self.canine)

#----------------------------------------------------------

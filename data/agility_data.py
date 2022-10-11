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
        reg_name=None, notes=None, titles=None, reg_no=None):
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
        if reg_no != None:
            self.canine[name]['Registration Number'].append(reg_no)

    #------------------------------------------------------
    def addTitle(self, name, date=None, venue=None, title=None):
        # Add a title to the given canine
        self.canine[name]['Titles'].append(self.title_entry)

        self.canine[name]['Titles'][-1]['Date'] = date
        self.canine[name]['Titles'][-1]['Venue'] = venue
        self.canine[name]['Titles'][-1]['Title'] = title
    
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

        self.canine[name]['Trials'][uid] = {'Runs': {}}

    #------------------------------------------------------
    def addRun(self, name, uid, date, event, division=None, level=None, height=None, judge=None, 
        handler=None, sct=None, yards=None, obstacles=None, time=None, faults=None,
        place=None, tdogs=None, qd=None, q=None, tpoints=None, score=None, notes=None):
        
        # Add a run to given canine and trial
        if event not in self.canine[name]['Trials'][uid]['Runs']:
            self.canine[name]['Trials'][uid]['Runs'][event] = self.run_entry
        self.canine[name]['Trials'][uid]['Runs'][event]['Date'] = date
        if division != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Division'] = division
        if level != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Level'] = level
        if height != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Height'] = height
        if judge != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Judge'] = judge
            self.addJudge(judge)
        if handler != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Handler'] = handler
        if sct != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['SCT'] = sct
        if yards != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Yards'] = yards
        if obstacles != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Obstacles'] = obstacles
        if time != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Time'] = time
        if faults != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Faults'] = faults
        if place != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Place'] = place
        if tdogs != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Total Dogs'] = tdogs
        if qd != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Qd'] = qd
        if q != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Q?'] = q
        if tpoints != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Title Pts'] = tpoints
        if score != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Score'] = score
        if notes != None:
            self.canine[name]['Trials'][uid]['Runs'][event]['Notes'] = notes

    #------------------------------------------------------
    def addCalendar(self, sdate, club, edate=None, odate=None, cdate=None,
        ddate=None, tent=None, entry=None, email=None, venue=None,
        loc=None, notes=None):

        # Add a calendar entry, start date and club are necessary
        k = f'{sdate} {club}'
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
        self.run_entry = {'Division': '', # Event will be the key within self.canine[name]['Trials'][uid]
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
    def tempPrint(self):
        print(self.canine)

#----------------------------------------------------------

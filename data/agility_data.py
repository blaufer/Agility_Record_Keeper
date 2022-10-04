import json
import os, shutil
from pprint import pprint

#----------------------------------------------------------

class AgilityData():

    #------------------------------------------------------
    def __init__(self):
        # Variables
        self.canine = {}
        self.calendar = {}
        self.training = {}
        self.venues = ['AKC']
        self.judges = {}
        self.locations = {}
        self.clubs = {}
        
        # Keys to the saved JSON
        self.keys = ['validate', 'canine', 'calendar', 'training',
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
    def addTrial(self, name, date, club=None, loc=None, venue=None, notes=None):
        # Add a trial to the given canine
        if date not in self.canine[name]['Trials']:
            self.canine[name]['Trials'][date] = self.trial_entry

        if club != None:
            self.canine[name]['Trials'][date]['Club'] = club
            self.addClub(club)
        if loc != None:
            self.canine[name]['Trials'][date]['Location'] = loc
            self.addLocation(loc)
        if venue != None:
            self.canine[name]['Trials'][date]['Venue'] = venue
        if notes != None:
            self.canine[name]['Trials'][date]['Notes'] = notes

    #------------------------------------------------------
    def addRun(self, name, date, event, division=None, level=None, height=None, judge=None, 
        handler=None, sct=None, yards=None, obstacles=None, time=None, faults=None,
        place=None, tdogs=None, qd=None, q=None, tpoints=None, score=None, notes=None):
        
        # Add a run to given canine and trial
        if event not in self.canine[name]['Trials'][date]['Runs']:
            self.canine[name]['Trials'][date]['Runs'][event] = self.run_entry

        if division != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Division'] = division
        if level != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Level'] = level
        if height != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Height'] = height
        if judge != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Judge'] = judge
            self.add_judge(judge)
        if handler != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Handler'] = handler
        if sct != None:
            self.canine[name]['Trials'][date]['Runs'][event]['SCT'] = sct
        if yards != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Yards'] = yards
        if obstacles != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Obstacles'] = obstacles
        if time != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Time'] = time
        if faults != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Faults'] = faults
        if place != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Place'] = place
        if tdogs != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Total Dogs'] = tdogs
        if qd != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Qd'] = qd
        if q != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Q?'] = q
        if tpoints != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Title Pts'] = tpoints
        if score != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Score'] = score
        if notes != None:
            self.canine[name]['Trials'][date]['Runs'][event]['Notes'] = notes

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
    def addTraining(self, name, sname=None, notes=None):

        # Add training entry, name is necessary
        self.training[name] = self.training_entry

        if sname != None:
            self.training[name]['Subname'] = sname
        if notes != None:
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
        self.training = all_data['training']
        self.venues = all_data['venues']
        self.judges = all_data['judges']
        self.clubs = all_data['clubs']
        self.locations = all_data['locations']

    #------------------------------------------------------
    def addJudge(self, judge, note=None):
        # If a judge is added to a run entry, check if
        # it's in the judges list and add if not
        if judge not in self.judges:
            self.judges[judge] = None

        if note != '':
            self.judges[judge] = note

    #------------------------------------------------------
    def addClub(self, club, note=None):
        # If a club is added to a trial entry, check if
        # it's in the clubs list and add if not
        if club not in self.clubs:
            self.clubs[club] = None

        if note != '':
            self.clubs[club] = note
    
    #------------------------------------------------------
    def addLocation(self, loc, note=None):
        # If a location is added to a trial entry, check if
        # it's in the locations list and add if not
        if loc not in self.locations:
            self.locations[loc] = None

        if note != '':
            self.locations[loc] = note

    #------------------------------------------------------
    def blankEntries(self):
        # Add dictionaries for each type of entry so that
        # all items will be present even if blank
        self.canine_entry = {'DOB': None,
                             'Deceased': None,
                             'Breed': None,
                             'Registered Name': None,
                             'Notes': None,
                             'Titles': [],
                             'Registration': [],
                             'Trials': {}
                            }
        self.title_entry = {'Date': None,
                            'Venue': None,
                            'Title': None,
                           }
        self.reg_entry = {'Venue': None,
                          'Number': None,
                          'Height': None,
                          'HC Recieved': None,
                          'Note': None
                         }
        self.trial_entry = {'Club': None, # Date will be the key within self.canine[name]['Trials']
                            'Location': None,
                            'Venue': None,
                            'Notes': None,
                            'Runs': {}
                           }
        self.run_entry = {'Division': None, # Event will be the key within self.canine[name]['Trials'][date]
                          'Level': None,
                          'Height': None,
                          'Judge': None,
                          'Handler': None,
                          'SCT': None,
                          'Yards': None,
                          'Obstacles': None,
                          'Time': None,
                          'Faults': None,
                          'Place': None,
                          'Total Dogs': None,
                          'Qd': None,
                          'Q?': None,
                          'Title Pts': None,
                          'Score': None,
                          'Notes': None
                         }
        self.calendar_entry = {'SDate': None,
                               'EDate': None,
                               'ODate': None,
                               'CDate': None,
                               'DDate': None,
                               'Tentative': None,
                               'Entry': None,
                               'SecEmail': None,
                               'Venue': None,
                               'Club': None,
                               'Location': None,
                               'Notes': None
                              }
        self.training_entry = {'Subname': None,
                               'Notes': None
                              }

    #------------------------------------------------------
    def tempPrint(self):
        print(self.canine)

#----------------------------------------------------------

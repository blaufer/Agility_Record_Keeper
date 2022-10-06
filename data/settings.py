import json
import os

#----------------------------------------------------------
class AgilitySettings():

    #------------------------------------------------------
    def __init__(self):
        self.filename = 'settings.json'
        self.settings = {}
        self.openLast()

    #------------------------------------------------------
    def openLast(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, 'r') as f:
            self.settings = json.load(f)

    #------------------------------------------------------
    def writeSettings(self):
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f, indent=4)

    #------------------------------------------------------
    def removeFilename(self):
        # Used when the new button is clicked in the
        # file dropdown
        if 'file' in self.settings.keys():
            del self.settings['file']

#----------------------------------------------------------

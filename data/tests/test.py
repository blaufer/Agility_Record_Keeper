import agility_data as ad

a = ad.AgilityData()
a.addCanine('Remy', '6/24/2019', 'Sheltie')
a.addTrial('Remy', '1/12/2019','WAG')
a.addRun('Remy', '1/12/2019', 'JWW', 'Novice B')
a.addTrial('Remy', '10/8/2021', 'GSDCA')
a.addRun('Remy', '1/12/2019', 'STD', 'Novice B')

a.addCanine('Remy', reg_name='Celebration Remy Etienne LeBeau')

a.addCalendar('1/10/2010', 'GSDCA', venue='AKC')

a.writeJSON('test.json')

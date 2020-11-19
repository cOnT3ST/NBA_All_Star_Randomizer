import random

db = [{"name": "Stephen Curry", "pos": ["point guard"], "team": "Golden State Warriors", "pic": "", "status": "not_picked"},
	  {"name": "Kobe Bryant", "pos": ["small forward", "shooting guard"], "team": "Los Angeles Lakers", "pic": "", "status": "not_picked"},
	  {"name": "Kevin Durant", "pos": ["power forward", "small forward", "shooting guard"], "team": "Oklahoma City Thunder", "pic": "", "status": "not_picked"},
	  {"name": "Blake Griffin", "pos": ["power forward"], "team": "Los Angeles Clippers", "pic": "", "status": "not_picked"},
	  {"name": "Kevin Love", "pos": ["center", "power forward"], "team": "Minnesota Timberwolves", "pic": "", "status": "not_picked"},
	  {"name": "Kyrie Irving", "pos": ["point guard"], "team": "Cliveland Cavaliers", "pic": "", "status": "not_picked"},
	  {"name": "Dwyane Wade", "pos": ["point guard", "shooting guard"], "team": "Miami Heat", "pic": "", "status": "not_picked"},
	  {"name": "Paul George", "pos": ["small forward", "shooting guard"], "team": "Indiana Pacers", "pic": "", "status": "not_picked"},
	  {"name": "LeBron James", "pos": ["power forward", "small forward", "point guard", "shooting guard"], "team": "Miami Heat", "pic": "", "status": "not_picked"},
	  {"name": "Carmelo Anthony", "pos": ["power forward", "small forward"], "team": "New York Knicks", "pic": "", "status": "not_picked"},
	  {"name": "Chris Paul", "pos": ["point guard"], "team": "Los Angeles Clippers", "pic": "", "status": "not_picked"},
	  {"name": "Dwight Howard", "pos": ["center", "power forward"], "team": "Houston Rockets", "pic": "", "status": "not_picked"},
	  {"name": "Dirk Nowitzki", "pos": ["center", "power forward"], "team": "Dallas Mavericks", "pic": "", "status": "not_picked"},
	  {"name": "LaMarcus Aldridge", "pos": ["center", "power forward"], "team": "Portland Trail Blazers", "pic": "", "status": "not_picked"},
	  {"name": "Damian Lillard", "pos": ["point guard"], "team": "Portland Trail Blazers", "pic": "", "status": "not_picked"},
	  {"name": "James Harden", "pos": ["point guard", "shooting guard"], "team": "Houston Rockets", "pic": "", "status": "not_picked"},
	  {"name": "John Wall", "pos": ["point guard"], "team": "Washington Wizards", "pic": "", "status": "not_picked"},
	  {"name": "DeMar DeRozan", "pos": ["small forward", "shooting guard"], "team": "Toronto Raptors", "pic": "", "status": "not_picked"},
	  {"name": "Paul Millsap", "pos": ["power forward"], "team": "Atlanta Hawks", "pic": "", "status": "not_picked"},
	  {"name": "Joakim Noah", "pos": ["center"], "team": "Chicago Bulls", "pic": "", "status": "not_picked"},
	  {"name": "Roy Hibbert", "pos": ["center"], "team": "Indiana Pacers", "pic": "", "status": "not_picked"},
	  {"name": "Chris Bosh", "pos": ["center", "power forward"], "team": "Miami Heat", "pic": "", "status": "not_picked"},
	  {"name": "Joe Johnson", "pos": ["small forward", "shooting guard"], "team": "Brooklyn Nets", "pic": "", "status": "not_picked"}]

class Player:
	def __init__(self, pl_dict):
		self.name = pl_dict['name']
		self.pos = pl_dict['pos']
		self.team = pl_dict['team']
		self.pic = pl_dict['pic']

	def __str__(self):
		return f'{self.name} from {self.team} to be playing as a {random.choice(self.pos)}'

class Team:
	formation = ("point guard", "shooting guard", "small forward", "power forward", "center")

	def __init__(self, name, roster = []):
		self.name = name
		self.roster = roster

	def randomize(self):
		for pos in self.formation:
			copy_db = db[:]
			suitable_players = certain_pos(copy_db,pos)
			random_player = Player(random.choice(suitable_players))
			random_player.pos = pos
			self.roster.append(random_player)

	def __str__(self):
		str_team = f'{self.name} \n'
		for player in self.roster:
			str_team += f'{player.pos}: {player.name} \n'
		str_team = str_team[:-1]
		return str_team

def certain_pos(pl_list, pos):
	pos_list = []
	for player in pl_list:
		if pos in player['pos']:
			pos_list.append(player)
	return pos_list

tm1 = Team("Team West")
tm1.randomize()
print(tm1)
tm2 = Team("Team East")
tm2.randomize()
print(tm2)
class Girl:
	girls_count = 0
	def __init__(self, name, attractiveness, intelligence, budget):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.budget = budget
		self.relationshipStatus = 'single'
		self.boyFriendName = ''
		self.type = ''
		self.happinessLevel = 0
		Girl.girls_count += 1
	def checkElligible(self, boy):
		if self.budget <= boy.budget and self.relationshipStatus == 'single':
			return True
		return False
		
'''g = []
g.append(Girl('df', 1, 1, 0))'''
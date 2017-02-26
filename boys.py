class Boy:
	boys_count = 0
	def __init__(self, name, attractiveness, intelligence, min_attractionreq, budget):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.min_attractionreq = min_attractionreq
		self.budget = budget
		self.relationshipStatus = 'single'
		self.girlFriendName = ''
		self.type = ''
		self.happinessLevel = 0
		Boy.boys_count += 1;
	def checkElligible(self, girl):
		if self.budget >= girl.budget and self.min_attractionreq <= girl.attractiveness and self.relationshipStatus == 'single':
			return True
		return False
		
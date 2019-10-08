'''
Game model
'''

class Game:
	def __init__(self):
		self.playerPos = (0, 0)
		self.nbLife = 3
		self.level = 0

		self.key = (0, 0)

		self.monsters = []

		self.generateMap()

		# create timer

		self.draw()

	# Map element generation

	def generateRooms(self):

	def generateKey(self):

	def generateMonsters(self):

	def generateCorridors(self):

	def generateMap(self):

	
	# Movement

	def move(self, pos):
		self.playerPos = pos

	def draw(self):



'''
score model
'''

class Score:
	def __init__(self, username, nbKey, time):
		self.username = username
		self.nbKey = nbKey
		self.time = time

	def __str__(self):
		return "{}: {} key(s) in {} sec".format(self.username, self.nbKey, self.time)
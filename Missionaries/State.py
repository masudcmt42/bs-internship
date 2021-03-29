from Constants import Direction



class State(object):

	def __init__(self, missionaries, cannibals, dir, missionariesPassed, cannibalsPassed, level,moves):
		self.missionaries = missionaries
		self.cannibals = cannibals
		self.dir = dir
		self.action = ""
		self.level = level
		self.missionariesPassed = missionariesPassed
		self.cannibalsPassed = cannibalsPassed
		self.moves = moves

	def successors(self):
		listChild = []
		if not self.isValid() or self.isGoalState():
			return listChild
		if self.dir == Direction.RIGHT:
			sgn = -1
			direction = "Send RIGHT To LEFT"
		else:
			sgn = 1
			direction = "back LEFT To RIGHT"
		for i in self.moves:
			(m, c) = i
			self.addValidSuccessors(listChild, m, c, sgn, direction)
		return listChild

	def addValidSuccessors(self, listChild, m, c, sgn, direction):
		newState = State(self.missionaries + sgn * m, self.cannibals + sgn * c, self.dir + sgn * 1,
							self.missionariesPassed - sgn * m, self.cannibalsPassed - sgn * c, self.level + 1,self.moves)
		if newState.isValid():
			newState.action = " take %d missionaries and %d cannibals %s." % (m, c, direction)
			listChild.append(newState)

	def isValid(self):
		# obvious
		if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 30 or self.cannibals > 30 or (
				self.dir != 0 and self.dir != 1):
			return False

		if (self.cannibals > self.missionaries > 0) or (
				self.cannibalsPassed > self.missionariesPassed > 0):
			return False

		return True

	def isGoalState(self):
		return self.cannibals == 0 and self.missionaries == 0 and self.dir == Direction.LEFT

	def __repr__(self):
		return "\n%s\n\n< @Depth:%d State (%d, %d, %d, %d, %d) >" % (
			self.action, self.level, self.missionaries, self.cannibals, self.dir, self.missionariesPassed,
			self.cannibalsPassed)

	def __eq__(self, other):
		return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.dir == other.dir

	def __hash__(self):
		return hash((self.missionaries, self.cannibals, self.dir))

	def __ne__(self, other):
		return not (self == other)


TERMINAL_STATE = State(-1, -1, Direction.LEFT, -1, -1, 0,None)

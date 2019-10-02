from copy import deepcopy
import numpy as np
class State(object):

	def __init__(self, values, parent=None):
		self.values = values
		self.parent = parent

	def legal(self):
		return True

	def final(self, final_values):
		return self.values == final_values

	def __hash__(self):
		return str(self).__hash__()

	def __str__(self):
		return str(self.values)

	def __eq__(self, other):
		return self.values == other.values


	def find_zero(self):
		for i, line in enumerate(self.values):
			for j, val in enumerate(line):
				if val == 0:
					return i, j


	@staticmethod
	def swap(values, x1, y1, x2, y2):
		# swap two cases in the plate of the puzzle
		# hint: a deepcopy is needed
		new_values = deepcopy(values)
		new_values[x1][y1],new_values[x2][y2] = new_values[x2][y2],new_values[x1][y1]
		return new_values

	def applicable_operators(self):
		# list of new values after the application of possible operators
		ops = []
		posx, posy = self.find_zero()
		nbline, nbcol = len(self.values), len(self.values[0])


		if posx > 0:
			ops.append(self.swap(self.values, posx, posy, posx-1, posy))
		if posx < nbline - 1:
			ops.append(self.swap(self.values, posx, posy, posx+1, posy))
		if posy > 0:
			ops.append(self.swap(self.values, posx, posy, posx, posy-1))
		if posy < nbcol - 1:
			ops.append(self.swap(self.values, posx, posy, posx, posy+1))
		return ops

	def apply(self, op):
		return State(op, self)

'''
Class Heuristique et ses différentes classes pour le pattern Strategy
une methode abstract pour pouvoir modifier la strategy avec les différents heuristique
une methode test pour afficher tous les algorithmes
'''

from abc import ABC, abstractmethod


class Heuristique(ABC):

	@abstractmethod
	def do_algorithm(self, t1, t2):
		pass

	@staticmethod
	def test(t1, t2):
		h0 = solution_heuristique()
		h1 = base_heuristique_x()
		h2 = base_heuristique_y()
		h3 = bird_flight()
		h4 = Manhattan()
		print(f"h0 = {h0.do_algorithm(t1, t2)}")
		print(f"h1 = {h1.do_algorithm(t1, t2)}")
		print(f"h2 = {h2.do_algorithm(t1, t2)}")
		print(f"h3 = {h3.do_algorithm(t1, t2)}")
		print(f"h4 = {h4.do_algorithm(t1, t2)}")

#admissible, ne surestimera jamais le coût entre deux villes(0)
class solution_heuristique(Heuristique):
	def do_algorithm(self, t1=None, t2=None):
		return 0
#admissible, distance x est toujours plus faible entre deux villes
class base_heuristique_x(Heuristique):
	def do_algorithm(self, t1, t2):
		return abs(t1.x - t2.x)

#admissible, même chose que heuristique_x mais en y
class base_heuristique_y(Heuristique):
	def do_algorithm(self, t1, t2):
		return abs(t1.y - t2.y)

#admissible, ne peut pas surestimer la distance (c'est la plus courte)
class bird_flight(Heuristique):
	def do_algorithm(self, t1, t2):
		x = base_heuristique_x()
		y = base_heuristique_y()
		return (x.do_algorithm(t1, t2)**2
						 + y.do_algorithm(t1, t2)**2) ** (1/2)

#pas admissible, Manhattan peut surestimer al distance entre 2 villes
class Manhattan(Heuristique):
	def do_algorithm(self, t1, t2):
		x = base_heuristique_x()
		y = base_heuristique_y()
		return x.do_algorithm(t1, t2) \
			   + y.do_algorithm(t1, t2)

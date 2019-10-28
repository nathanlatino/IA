'''
Class Astar avec Class parent (helper)
Class parent: represente un parent avec son poid du parcours, objet Town et
eventuellement le parent du parent
Class Astar: prend un heuristique à l'initialisation et peut denouveau le set
method find qui utilise l'astar avec l'heuristique actif entre deux ville
t1: ville de départ
t2: ville d'arrivée

Les villes voisines sont stockées s'ils n'ont pas été visités ou pas stockés
dans la pile de parcours. Si elle est déjà existante dans la pile, on prend
le chemin qui a le cout le plus faible.

Chaques ville voisines qui sont validées, sont stockée dans un tableau tuple
et ensuite trié par rapport à son coût
'''

from heuristique import Heuristique


class Parent:
	def __init__(self, g, town, parent=None):
		self.parent = parent
		self.weight = g
		self.town = town


class Astar:
	def __init__(self, heuristique: Heuristique) -> None:
		self._heuristique = heuristique

	@property
	def heuristique(self) -> Heuristique:
		return self._heuristique

	@heuristique.setter
	def heuristique(self, heuristique: Heuristique) -> None:
		self._heuristique = heuristique

	def find(self, t1, t2) -> None:
		stack_parcours = [(t1, 0, Parent(0, t2))]
		set_history = set()
		cpt_visited = 0
		while stack_parcours:
			current_tuple = stack_parcours.pop(0)
			cpt_visited += 1
			state_town = current_tuple[0]
			parent_path = current_tuple[2]
			set_history.add(state_town)
			if state_town == t2:
				return current_tuple, cpt_visited
			for k, v in state_town.dicneib.items():
				newparent = Parent(parent_path.weight + v, state_town, parent_path)
				value = parent_path.weight + v + self._heuristique.do_algorithm(k, t2)
				index = self.__tuple_get_index(k, stack_parcours)

				if k not in set_history and index == -1:
					stack_parcours.append((k, value, newparent))
				elif index != -1:
					if stack_parcours[index][1] > value:
						stack_parcours[index] = (k, value, newparent)

				stack_parcours.sort(key=lambda dist: dist[1])

		return None

	def __tuple_get_index(self, k, stack):
		for t in range(0, len(stack)):
			if stack[t][0] == k:
				return t
		else:
			return -1





	@staticmethod
	def show(res):
		'''affiche le résultat du astar'''
		tuple, cpt = res
		print("\n")
		print(f"Nombre ville visitée: {cpt}")
		parent_path = tuple[2]
		print(tuple[0].name)
		while parent_path.parent is not None:
			print(parent_path.town.name)
			parent_path = parent_path.parent

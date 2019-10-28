"""
Class Town
name: nom de la ville
x: postition x
y: postition y
dicNeib : dictionnaire des autres villes voisines (Neighbours)

create_towns(dictTown, filename): crée des objets villes depuis un fichier texte
create_neighbours(dicoTown, filename): crée les voisins de la ville
print_towns(dictTown): affiche toutes les villes avec leur lien du dictionnaire
"""


class Town:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
		self.dicneib = {}

	def __hash__(self):
		return str(self).__hash__()

	def __eq__(self, other):
		return self.name == other.name

	def __repr__(self):
		s = f"\nName: ({self.name}), posx({self.x}), posy({self.y})"
		s += "\ndistance with connection: "
		for k, v in self.dicneib.items():
			s += f"\n{k.name} : {v}"
		return s

	@staticmethod
	def create_towns(dictown, filename):
		with open(filename, "r") as f:
			contenu = f.read().split('\n')
			for line in contenu:
				splitl = line.split(" ")
				dictown[splitl[0]] = (Town(splitl[0], int(splitl[1]), int(splitl[2])))

	@staticmethod
	def create_neighbours(dicotown, filename):
		with open(filename, "r") as f:
			contenu = f.read().split('\n')
			for line in contenu:
				splitl = line.split(" ")
				for k, v in dicotown.items():
					if k == splitl[0]:
						v.dicneib[dicotown[splitl[1]]] = int(splitl[2])
					if k == splitl[1]:
						v.dicneib[dicotown[splitl[0]]] = int(splitl[2])

	@staticmethod
	def print_towns(dictown):
		for k, v in dictown.items():
			print(v)

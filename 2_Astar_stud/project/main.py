from town import Town
from astar import Astar
from heuristique import *

def test_astar(t1 ,t2):
    astar = Astar(solution_heuristique())
    Astar.show(astar.find(t1, t2))
    astar.heuristique = base_heuristique_x()
    Astar.show(astar.find(t1, t2))
    astar.heuristique = base_heuristique_y()
    Astar.show(astar.find(t1, t2))
    astar.heuristique = bird_flight()
    Astar.show(astar.find(t1, t2))
    astar.heuristique = Manhattan()
    Astar.show(astar.find(t1, t2))


if __name__ == '__main__':
    dicTown = {}
    start_town ="Amsterdam"
    destination_town ="Prague"
    # créations des villes et de leur voisin
    Town.create_towns(dicTown, "positions.txt")
    Town.create_neighbours(dicTown, "connections.txt")

    Town.print_towns(dicTown)



    Heuristique.test(dicTown[start_town], dicTown[destination_town])
    test_astar(dicTown[start_town], dicTown[destination_town])

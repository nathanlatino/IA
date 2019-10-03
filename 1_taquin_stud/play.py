from state_modele import State
from taquin_viewer import TaquinViewerHTML

def print_len(history, frontiere):
	print(f"History len: {len(history)}")
	print(f"Frontiere len: {len(frontiere)}")

def search(init, final_values):
	frontiere = []
	frontiere.append(init)
	history = set()

	while frontiere:
		etat = frontiere.pop()
		history.add(etat)
		if etat.final(final_values):
			print_len(history, frontiere)
			return etat
		ops = etat.applicable_operators()
		for op in ops:
			new = etat.apply(op)
			# if(new not in frontiere) and (new not in history) and new.legal():
			if(new not in history) and new.legal():
				frontiere.insert(0, new)
				# frontiere.append(new)
	print_len(history,frontiere)
	return None


if __name__ == '__main__':
	taquin_easy = [
		[1, 2, 3],
		[4, 0, 6],
		[7, 5, 8]
	]

	taquin_medium = [
		[0, 1, 2],
		[7, 4, 3],
		[5, 8, 6]
	]

	taquin_hard = [
		[4, 0, 2],
		[3, 5, 1],
		[6, 7, 8]
	]

	taquin_impossible = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]

	final_values = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 0]
	]

	result = search(State(taquin_easy), final_values)
	if result is not None:
		print("Solution found")
		result_path = []
		while result.parent is not None:
			result_path.insert(0,result)
			result = result.parent
		result_path.insert(0, result)
		with TaquinViewerHTML('easy.html') as viewer:
			for i, state in enumerate(result_path):
				viewer.add_taquin_state(state.values, title=i)
	else:
		print("Solution not found")

from taquin_viewer import TaquinViewerHTML

if __name__ == '__main__':

    # Show the usage of the viewer
    taquin_state1 = [[0, 4, 2],
                     [3, 1, 5],
                     [6, 7, 8]]

    first_move = [[4, 0, 2],
                  [3, 1, 5],
                  [6, 7, 8]]

    with TaquinViewerHTML('example.html') as viewer:
        viewer.add_taquin_state(taquin_state1, "origin")
        viewer.add_taquin_state(first_move, "first move")

    # You should test the following initial configurations:
    # your algorithm should reach the solution in few iterations
    taquin_easy = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    # your algorithm should reach the solution in few hundred iterations
    taquin_medium = [
        [0, 1, 2],
        [7, 4, 3],
        [5, 8, 6]
    ]

    # your algorithm will need more then 100'000 iterations
    taquin_hard = [
        [4, 0, 2],
        [3, 5, 1],
        [6, 7, 8]
    ]

    # just impossible
    taquin_impossible = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]

    # ... given this final state
    final_values = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
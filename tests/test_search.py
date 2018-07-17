from examples import queens
from cp_solver import propagator


def test_queens():
    solution = queens.solve(8, prop=propagator.NoPropagation())
    assert solution is not None
    for col in range(len(solution)):
        for col2 in range(len(solution)):
            assert solution[col] != solution[col2]
            assert solution[col] != solution[col2] + (col2 - col)
            assert solution[col] != solution[col2] - (col2 - col)

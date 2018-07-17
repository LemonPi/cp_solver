from examples import queens
from cp_solver import propagator
import pytest


def verify_queens_solution(solution):
    assert solution is not None

    for col in range(len(solution)):
        for col2 in range(len(solution)):
            if col == col2:
                continue
            assert solution[col] != solution[col2]
            assert solution[col] != solution[col2] + (col2 - col)
            assert solution[col] != solution[col2] - (col2 - col)


@pytest.mark.timeout(10)
def test_queens():
    prop = propagator.NoPropagation()

    for n in range(4, 14):
        solution = queens.solve(n, prop=prop)
        verify_queens_solution(solution)


@pytest.mark.timeout(10)
def test_queens_fc():
    prop = propagator.ForwardCheck()

    for n in range(4, 30):
        solution = queens.solve(n, prop=prop)
        verify_queens_solution(solution)

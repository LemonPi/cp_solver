from cp_solver import base
from cp_solver import search
from cp_solver import propagator


def solve(size, prop=propagator.ForwardCheck()):
    rows = list(range(size))
    cols = [base.Variable(rows) for _ in range(size)]
    csp = base.CSP(cols)
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            # can't be on same row
            csp.add_constraint(base.DifferentConstraint(cols[i], cols[j]))
            # upward diagonal (have to use default variables to bind at definition time)
            csp.add_constraint(base.FunctionConstraint([cols[i], cols[j]], lambda a, b, i=i, j=j: a != b + (j - i)))
            # downward diagonal
            csp.add_constraint(base.FunctionConstraint([cols[i], cols[j]], lambda a, b, i=i, j=j: a != b - (j - i)))

    bt = search.BacktrackSearch(csp, prop=prop)
    return bt.search()


def print_solution(solution, size):
    print("   %s \n" % ("-" * ((size * 4) - 1)), end='')
    for i in range(size):
        print("  |", end='')
        for j in range(size):
            if solution[j] == i:
                print(" %d |" % j, end='')
            else:
                print("   |", end='')
        print("\n", end='')
        if i != size - 1:
            print("  |%s|\n" % ("-" * ((size * 4) - 1)), end='')
    print("   %s \n" % ("-" * ((size * 4) - 1)), end='')

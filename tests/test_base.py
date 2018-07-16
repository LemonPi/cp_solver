from cp_solver.base import Variable


def test_variable_domain_iteration():
    domain = list(range(10))
    variable = Variable(domain)
    assert len(domain) == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert domain == domain_of_variable


def test_variable_pruned_iteration():
    domain = list(range(10))

    variable = Variable(domain)
    variable.prune(5)
    assert len(domain) - 1 == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert [d for d in domain if d != 5] == domain_of_variable

from cp_solver.base import Variable


def test_variable_domain_iteration():
    domain = list(range(10))
    variable = Variable(domain)
    assert len(domain) == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert domain == domain_of_variable


def test_variable_enumerated_iteration():
    domain = list(range(9, 0, -1))
    variable = Variable(domain)

    j = 0
    for i, v in variable.enumerate():
        assert i == j
        assert v == domain[i]
        j += 1


def test_variable_pruned_iteration():
    domain = list(range(10))

    variable = Variable(domain)
    variable.prune(5)
    assert len(domain) - 1 == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert [d for d in domain if d != 5] == domain_of_variable

    variable.prune(5, unprune=True)
    assert len(domain) == variable.domain_size()


def test_variable_pruned_index_iteration():
    domain = list(range(10))
    variable = Variable(domain)
    variable.prune_at_index(5)
    assert len(domain) - 1 == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert [d for d in domain if d != 5] == domain_of_variable
    variable.prune_at_index(5, unprune=True)
    assert len(domain) == variable.domain_size()

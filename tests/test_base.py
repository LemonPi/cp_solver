from cp_solver import base
import itertools


def test_variable_domain_iteration():
    domain = list(range(10))
    variable = base.Variable(domain)
    assert len(domain) == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert domain == domain_of_variable


def verify_domain_consistency(variable, domain):
    j = 0
    for i, v in variable.enumerate():
        assert i == j
        assert v == domain[i]
        j += 1


def test_variable_enumerated_iteration():
    domain = list(range(9, 0, -1))
    variable = base.Variable(domain)

    verify_domain_consistency(variable, domain)


def test_nested_iteration():
    # should go through all value combinations
    domain = list(range(10))
    variable = base.Variable(domain)

    value_combos = set()
    for v in variable:
        for vv in variable:
            value_combos.add((v, vv))

    should_produce = set(itertools.product(domain, domain))

    assert value_combos == should_produce


def test_variable_pruned_iteration():
    domain = list(range(10))

    variable = base.Variable(domain)
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
    variable = base.Variable(domain)
    variable.prune_at_index(5)
    assert len(domain) - 1 == variable.domain_size()

    domain_of_variable = []
    for value in variable:
        domain_of_variable.append(value)

    assert [d for d in domain if d != 5] == domain_of_variable
    variable.prune_at_index(5, unprune=True)
    assert len(domain) == variable.domain_size()


def test_variable_add_value():
    variable = base.Variable()
    domain = "abcdefghijklmn"
    for c in domain:
        variable.add_value(c)

    assert len(domain) == variable.domain_size()
    verify_domain_consistency(variable, domain)

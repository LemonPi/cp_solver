import abc
from cp_solver.base import CSP


class Propagator(abc.ABC):
    """A constraint propagator that prunes domains"""

    @abc.abstractmethod
    def __call__(self, csp: CSP, newly_instantiated_variable=None):
        """Prunes csp's variables and returns (domain wipeout, [(pruned variable, pruned value), ...])"""


class NoPropagation(Propagator):
    def __call__(self, csp: CSP, newly_instantiated_variable=None):
        if not newly_instantiated_variable:
            return False, []
        for c in csp.constraints_involving_variable(newly_instantiated_variable):
            if not c.unassigned():
                if not c.check_feasible():
                    return True, []
        return False, []


class ForwardCheck(Propagator):
    def __call__(self, csp: CSP, newly_instantiated_variable=None):
        total_pruned = []
        for con in csp.constraints():
            domain_wipeout, pruned = con.forward_check()
            total_pruned.extend(pruned)

            if domain_wipeout:
                return domain_wipeout, total_pruned

        return False, total_pruned


class GeneralArcConsistency(Propagator):
    def __call__(self, csp: CSP, newly_instantiated_variable=None):
        # TODO implement
        ...

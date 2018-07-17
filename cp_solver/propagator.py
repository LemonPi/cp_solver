import abc
from cp_solver import base


class Propagator(abc.ABC):
    """A constraint propagator that prunes domains"""

    @abc.abstractmethod
    def __call__(self, csp: base.CSP, newly_instantiated_variable=None):
        """Prunes csp's variables and returns (domain wipeout, [(pruned variable, pruned value), ...])"""


class NoPropagation(Propagator):
    def __call__(self, csp: base.CSP, newly_instantiated_variable=None):
        if not newly_instantiated_variable:
            return base.DomainWipeout.NO_DWO, []
        for c in csp.constraints_involving_variable(newly_instantiated_variable):
            if not c.unassigned():
                if not c.check_feasible():
                    return base.DomainWipeout.DWO, []
        return base.DomainWipeout.NO_DWO, []


class ForwardCheck(Propagator):
    def __call__(self, csp: base.CSP, newly_instantiated_variable=None):
        total_pruned = []
        for con in csp.constraints():
            domain_wipeout, pruned = con.forward_check()
            total_pruned.extend(pruned)

            if domain_wipeout:
                return base.DomainWipeout.DWO, total_pruned

        return base.DomainWipeout.NO_DWO, total_pruned


class GeneralArcConsistency(Propagator):
    def __call__(self, csp: base.CSP, newly_instantiated_variable=None):
        # TODO implement
        ...

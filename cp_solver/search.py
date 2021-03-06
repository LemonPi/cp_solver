from cp_solver import base
from cp_solver import propagator
import logging
import typing
import math
import time

logger = logging.getLogger(__name__)


def get_min_domain_max_constraint(csp):
    # by default use the fail-first principle and return the variable with the smallest domain
    min_domain = math.inf
    max_cons = 0
    chosen_i = None
    vars = csp.variables()
    for i in range(len(vars)):
        v = vars[i]
        if v.is_assigned():
            continue

        num_cons = len(csp.constraints_involving_variable(v))
        if v.domain_size() < min_domain or (v.domain_size() == min_domain and num_cons > max_cons):
            min_domain = v.domain_size()
            max_cons = num_cons
            chosen_i = i

    return (vars[chosen_i], chosen_i) if chosen_i is not None else (None, None)


def get_value_in_domain_order(csp, var_i):
    var = csp.variables()[var_i]
    for val in var:
        yield val


class BacktrackSearch:
    def __init__(self, csp: base.CSP, prop=propagator.ForwardCheck(),
                 select_next_variable: typing.Callable[
                     [base.CSP], typing.Tuple[base.Variable, int]] = get_min_domain_max_constraint,
                 select_next_value: typing.Callable[[base.CSP, int], typing.Any] = get_value_in_domain_order):

        self._csp = csp
        self._propagator = prop
        self._get_next_var = select_next_variable
        self._get_next_val = select_next_value
        self._solution = None

    def _restore_all_domains(self):
        for v in self._csp.variables():
            if v.is_assigned():
                v.unassign()
            v.restore_domain()

    def _restore_pruning(self, prunings: typing.List[typing.Tuple[base.Variable, int]]):
        for var, val_i in prunings:
            var.prune_at_index(val_i, unprune=True)

    def search(self):
        """Get first solution to CSP. Returns None if no solution, otherwise the solution."""
        start_time = time.time()

        self._restore_all_domains()

        # initial propagation
        domain_wipeout, prunings = self._propagator(self._csp)
        # infeasible
        if domain_wipeout == base.DomainWipeout.DWO:
            return None

        domain_wipeout = self._recurse()

        self._restore_pruning(prunings)

        logger.info("Search took {} seconds".format(time.time() - start_time))
        if domain_wipeout == base.DomainWipeout.DWO:
            return None
        return self._solution

    def _recurse(self, level=0):
        """Return whether we had a domain wipeout"""
        logging_indent = " " * level

        var, var_i = self._get_next_var(self._csp)

        # done since no more variables to assign
        if var is None:
            # reached a solution
            self._solution = [v.assigned_value() for v in self._csp.variables()]
            logger.debug("Reached solution {}".format(self._solution))
            return base.DomainWipeout.NO_DWO

        logger.debug("{}Find a value for {}".format(logging_indent, var_i))
        for val in self._get_next_val(self._csp, var_i):
            var.assign(val)
            domain_wipeout, prunings = self._propagator(self._csp, var)

            logger.debug("{}Assigning {} to {} -> {}".format(logging_indent, val, var_i, domain_wipeout))
            if not domain_wipeout:
                domain_wipeout = self._recurse(level + 1)
                if domain_wipeout != base.DomainWipeout.DWO:
                    return domain_wipeout

            # else this choice of val for var caused a domain wipeout so we need to restore and try something else
            self._restore_pruning(prunings)
            var.unassign()

        # if there was no choice for any var to not have domain wipeout, our previous choices forced us to wipeout
        return base.DomainWipeout.DWO

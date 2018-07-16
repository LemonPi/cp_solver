# Introduction

A pure python constraint satisfaction problem solver.

# Installation (development)

Install in editable mode with `py -3 -m pip install -e .` so that
modifications in the repository are automatically synced with the
installed library.

# Testing
Install dependencies

`py -3 -m pip install tox pytest coverage pytest-cov`

Run pytest at top level directly independently

`py -m pytest -s -v --log-cli-level=DEBUG --show-capture=no`

Run tox from any directory to run tests in a virtual environment and tests coverage.

`tox`

# Organization
Everything is under the `cp_solver` package.

Basic components such as `Variable`, `Constraint` and `CSP` are in `cp_solver.base`.

Constraint propagators for pruning purposes such as `ForwardCheck` and
`GeneralArcConsistency` are in `cp_solver.propagator`.

Search algorithms such as `BacktrackSearch` are in `cp_solver.search`.

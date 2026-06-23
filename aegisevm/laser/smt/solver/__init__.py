import z3

from aegisevm.laser.smt.solver.independence_solver import IndependenceSolver
from aegisevm.laser.smt.solver.solver import BaseSolver, Optimize, Solver
from aegisevm.laser.smt.solver.solver_statistics import SolverStatistics
from aegisevm.support.support_args import args

if args.parallel_solving:
    z3.set_param("parallel.enable", True)

"""Plugin implementations

This module contains the implementation of some features

- benchmarking
- pruning
"""

from aegisevm.laser.plugin.plugins.benchmark import BenchmarkPluginBuilder
from aegisevm.laser.plugin.plugins.call_depth_limiter import CallDepthLimitBuilder
from aegisevm.laser.plugin.plugins.coverage.coverage_plugin import CoveragePluginBuilder
from aegisevm.laser.plugin.plugins.coverage_metrics import CoverageMetricsPluginBuilder
from aegisevm.laser.plugin.plugins.dependency_pruner import DependencyPrunerBuilder
from aegisevm.laser.plugin.plugins.instruction_profiler import InstructionProfilerBuilder
from aegisevm.laser.plugin.plugins.mutation_pruner import MutationPrunerBuilder
from aegisevm.laser.plugin.plugins.state_merge import StateMergePluginBuilder
from aegisevm.laser.plugin.plugins.summary import SymbolicSummaryPluginBuilder
from aegisevm.laser.plugin.plugins.trace import TraceFinderBuilder

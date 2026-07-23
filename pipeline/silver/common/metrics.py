"""
Data model for Silver pipeline execution metrics.
"""

from dataclasses import dataclass


@dataclass
class PipelineMetrics:
    """
    Metrics returned by a Silver transformation.
    """

    table_name: str
    rows_read: int
    rows_written: int
    rows_rejected: int
    execution_time_ms: int
    status: str

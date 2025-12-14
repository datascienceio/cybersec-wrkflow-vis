"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline

from cybersecurity_pipeline.pipelines.cybersecurity import create_pipeline as cybersecurity_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines."""
    return {
        "__default__": cybersecurity_pipeline(),
        "cybersecurity": cybersecurity_pipeline(),
    }

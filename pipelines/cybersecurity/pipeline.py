"""Cybersecurity pipeline definition - NO DATA FILES REQUIRED."""
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import log_filtering, threat_detection, reporting

def create_pipeline(**kwargs) -> Pipeline:
    """Create the cybersecurity pipeline - generates synthetic data automatically."""
    return pipeline(
        [
            node(
                func=log_filtering.generate_sample_logs,
                inputs=[
                    "params:log_filtering.num_entries",
                    "params:log_filtering.random_seed",
                ],
                outputs="raw_log_data",
                name="generate_sample_logs",
                tags=["filtering", "data_generation"],
            ),
            
            node(
                func=log_filtering.filter_security_logs,
                inputs=[
                    "raw_log_data",
                    "params:log_filtering.filter_criteria",
                ],
                outputs="filtered_logs",
                name="filter_security_logs",
                tags=["filtering"],
            ),
            node(
                func=log_filtering.parse_log_metadata,
                inputs="filtered_logs",
                outputs="log_metadata",
                name="parse_log_metadata",
                tags=["filtering", "metadata"],
            ),
            
            node(
                func=threat_detection.detect_anomalies,
                inputs=[
                    "filtered_logs",
                    "params:threat_detection.anomaly_threshold",
                    "params:threat_detection.window_size",
                ],
                outputs=["normal_logs", "anomalous_logs"],
                name="detect_anomalies",
                tags=["detection", "anomaly"],
            ),
            node(
                func=threat_detection.classify_threats,
                inputs=[
                    "anomalous_logs",
                    "params:threat_detection.threat_patterns",
                ],
                outputs="classified_threats",
                name="classify_threats",
                tags=["detection", "classification"],
            ),
            node(
                func=threat_detection.calculate_risk_scores,
                inputs=[
                    "classified_threats",
                    "params:threat_detection.severity_weights",
                ],
                outputs="scored_threats",
                name="calculate_risk_scores",
                tags=["detection", "scoring"],
            ),
            
            node(
                func=reporting.generate_threat_summary,
                inputs="scored_threats",
                outputs="threat_summary",
                name="generate_threat_summary",
                tags=["reporting", "summary"],
            ),
            node(
                func=reporting.create_alert_report,
                inputs=["scored_threats", "threat_summary"],
                outputs="alert_report",
                name="create_alert_report",
                tags=["reporting", "alerts"],
            ),
        ],
        tags=["cybersecurity"],
    )

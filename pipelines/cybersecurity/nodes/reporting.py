"""Nodes for generating security reports."""
from typing import Dict
import pandas as pd

def generate_threat_summary(
    classified_threats: pd.DataFrame,
) -> Dict[str, int]:
    """
    Generate summary statistics of detected threats.
    
    Args:
        classified_threats: DataFrame with classified threats
    
    Returns:
        Dictionary with threat summary statistics
    """
    summary = {
        "total_threats": len(classified_threats),
        "threats_by_category": classified_threats["threat_category"].value_counts().to_dict(),
        "threats_by_severity": classified_threats["severity"].value_counts().to_dict(),
    }
    
    return summary

def create_alert_report(
    high_risk_threats: pd.DataFrame,
    summary: Dict[str, int],
) -> pd.DataFrame:
    """
    Create alert report for high-risk threats.
    
    Args:
        high_risk_threats: DataFrame filtered to high-risk threats
        summary: Threat summary statistics
    
    Returns:
        DataFrame formatted as alert report
    """
    alert_report = high_risk_threats[
        ["timestamp", "source_ip", "destination_ip", "threat_category", "risk_score"]
    ].copy()
    
    alert_report = alert_report.sort_values("risk_score", ascending=False)
    
    return alert_report

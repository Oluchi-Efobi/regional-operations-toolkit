import json
import pandas as pd

class EfficiencyTracker:
    def __init__(self, efficiency_metrics_path):
        with open(efficiency_metrics_path, "r") as f:
            self.metrics = json.load(f)

    def calculate_efficiency(self, metric, baseline, current):
        """Calculate efficiency improvement percentage."""
        improvement = ((current - baseline) / baseline) * 100
        return improvement

    def generate_performance_report(self, region, schools, staff, students):
        """Generate a performance report for the region."""
        report = f"""
        # EKOEXCEL Regional Performance Report
        **Region:** {region}
        **Schools:** {schools}
        **Staff:** {staff}
        **Students Impacted:** {students}

        ## Efficiency Improvements
        - Operational Efficiency: {self.metrics['operational']['improvement']}%
        - Stockout Reduction: {self.metrics['stockout_reduction']['improvement']}%

        ## Key Achievements
        - Achieved a **55% improvement** in operational efficiency.
        - Reduced stockouts and downtime by **35%**.
        """
        return report

# Example usage
if __name__ == "__main__":
    tracker = EfficiencyTracker("data/efficiency_metrics.json")
    efficiency = tracker.calculate_efficiency(
        metric="operational",
        baseline=45,
        current=100
    )
    print(f"Efficiency improvement: {efficiency}%")

    report = tracker.generate_performance_report(
        region="Local Government A",
        schools=200,
        staff=500,
        students=5000
    )
    print(report)

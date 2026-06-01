class ReportGenerator:
    def generate_operational_report(self, period, improvements, impact):
        """Generate an operational efficiency report."""
        report = f"""
        # EKOEXCEL Operational Efficiency Report
        **Period:** {period}

        ## Key Improvements
        - Operational Efficiency: **+{improvements['operational_efficiency']}%**
        - Stockout Reduction: **+{improvements['stockout_reduction']}%**

        ## Impact
        - **Students Impacted:** {impact}

        ## Summary
        The regional operations have achieved significant improvements in efficiency and resource allocation,
        directly benefiting {impact} across {len(improvements)} key metrics.
        """
        return report

    def compile_stakeholder_summary(self, schools, staff, students, key_achievements):
        """Compile a summary for stakeholders."""
        summary = f"""
        # EKOEXCEL Regional Operations Summary

        ## Scale
        - **Schools:** {schools}
        - **Staff:** {staff}
        - **Students:** {students}

        ## Key Achievements
        """
        for achievement in key_achievements:
            summary += f"- {achievement}\n"
        return summary

# Example usage
if __name__ == "__main__":
    generator = ReportGenerator()
    operational_report = generator.generate_operational_report(
        period="Q1 2023",
        improvements={
            "operational_efficiency": 55,
            "stockout_reduction": 35
        },
        impact="5,000+ students"
    )
    print(operational_report)

    stakeholder_summary = generator.compile_stakeholder_summary(
        schools=200,
        staff=500,
        students=5000,
        key_achievements=[
            "55% improvement in operational efficiency",
            "35% reduction in stockouts"
        ]
    )
    print(stakeholder_summary)

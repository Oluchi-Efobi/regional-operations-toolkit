import pandas as pd
import matplotlib.pyplot as plt

class DataInsights:
    def __init__(self, schools_data_path, supply_chain_data_path):
        self.schools_data = pd.read_csv(schools_data_path)
        self.supply_chain_data = pd.read_csv(supply_chain_data_path)

    def analyze_regional_data(self, region, metrics):
        """Analyze regional performance based on selected metrics."""
        regional_schools = self.schools_data[self.schools_data["local_government"] == region]
        analysis = {
            "region": region,
            "schools": len(regional_schools),
            "teachers": regional_schools["teachers"].sum(),
            "students": regional_schools["students"].sum()
        }

        if "material_distribution" in metrics:
            regional_supply = self.supply_chain_data[self.supply_chain_data["school_id"].isin(regional_schools["school_id"])]
            analysis["materials_distributed"] = regional_supply["quantity_delivered"].sum()

        if "teacher_productivity" in metrics:
            analysis["teacher_student_ratio"] = regional_schools["teachers"].sum() / regional_schools["students"].sum()

        return analysis

    def visualize_trends(self, data_path, x, y):
        """Visualize trends in the data (e.g., stockouts over time)."""
        df = pd.read_csv(data_path)
        plt.figure(figsize=(10, 6))
        plt.plot(df[x], df[y], marker='o')
        plt.title(f"Trend of {y} over {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid(True)
        plt.savefig("trends.png")
        plt.close()
        return "trends.png"

# Example usage
if __name__ == "__main__":
    insights = DataInsights("data/schools_data.csv", "data/supply_chain_data.csv")
    regional_analysis = insights.analyze_regional_data(
        region="Local Government A",
        metrics=["material_distribution", "teacher_productivity"]
    )
    print("Regional analysis:", regional_analysis)

    trend_plot = insights.visualize_trends(
        data_path="data/stockout_logs.csv",
        x="date",
        y="stockout_count"
    )
    print(f"Trend plot saved as: {trend_plot}")

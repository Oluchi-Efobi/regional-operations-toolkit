import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class SupplyChainAnalyzer:
    def __init__(self, supply_chain_data_path):
        self.data = pd.read_csv(supply_chain_data_path)
        self.model = self._train_stockout_model()

    def _train_stockout_model(self):
        """Train a model to predict stockouts based on historical data."""
        # Placeholder: Replace with actual features and labels
        X = self.data[["quantity_delivered", "stock_level"]]
        y = self.data["stockout_risk"]  # Assume this column exists (0 = no stockout, 1 = stockout)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        return model

    def predict_stockouts(self, item, threshold=100):
        """Predict stockout risk for a specific item."""
        item_data = self.data[self.data["item"] == item]
        if item_data.empty:
            return "No data available for this item."
        latest_stock = item_data.iloc[-1]["stock_level"]
        return latest_stock < threshold

    def recommend_replenishment(self, item, lead_time=7):
        """Recommend replenishment quantity based on usage rate and lead time."""
        item_data = self.data[self.data["item"] == item]
        if item_data.empty:
            return {"error": "No data available for this item."}

        usage_rate = item_data["quantity_delivered"].mean() / 30  # Average daily usage
        recommended_quantity = usage_rate * lead_time
        return {
            "item": item,
            "recommended_quantity": int(recommended_quantity),
            "lead_time_days": lead_time
        }

# Example usage
if __name__ == "__main__":
    analyzer = SupplyChainAnalyzer("data/supply_chain_data.csv")
    stockout_risk = analyzer.predict_stockouts(item="Tablets", threshold=100)
    print("Stockout risk for Tablets:", stockout_risk)

    recommendations = analyzer.recommend_replenishment(item="Textbooks", lead_time=7)
    print("Replenishment recommendations:", recommendations)

# EKOEXCEL Regional Operations Toolkit

**A Python-based toolkit for optimizing regional operations logistics, supply chain management, and data-driven decision-making in education.**

- **Oversight of 200+ schools** across two local governments, managing **200 administrators and 300 teachers**.
- **Data-driven supply chain systems** for distributing learning materials and technological tools.
- **Achieving a 55% improvement in operational efficiency** and **35% reduction in downtime/stockouts**.
- **Impact on 5,000+ students** through streamlined logistics and resource allocation.

---

##  **Purpose**

This toolkit aims to:  
✅ **Optimize logistics** for learning materials and tech tools across schools.  
✅ **Reduce stockouts and downtime** with predictive supply chain analytics.  
✅ **Track operational efficiency** (e.g., staff performance, resource utilization).  
✅ **Generate actionable insights** for data-driven decision-making.

---

##  **Features**


| **Module**              | **Description**                                                                             | **Key Functions**                                                |
| ----------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `logistics_optimizer`   | Optimizes distribution routes and schedules for learning materials/tech tools.              | `optimize_routes()`, `schedule_deliveries()`                     |
| `supply_chain_analyzer` | Analyzes supply chain data to predict stockouts and reduce downtime.                        | `predict_stockouts()`, `recommend_replenishment()`               |
| `efficiency_tracker`    | Tracks operational efficiency metrics (e.g., staff productivity, resource usage).           | `calculate_efficiency()`, `generate_performance_report()`        |
| `data_insights`         | Provides insights into regional operations (e.g., school performance, resource allocation). | `analyze_regional_data()`, `visualize_trends()`                  |
| `report_generator`      | Automates reports for stakeholders (e.g., efficiency improvements, stockout reductions).    | `generate_operational_report()`, `compile_stakeholder_summary()` |


---

##  **Repository Structure**

```
ekoexcel-regional-operations-toolkit/
│   ├── logistics_optimizer.py      # Route and delivery schedule optimization
│   ├── supply_chain_analyzer.py    # Stockout prediction and replenishment
│   ├── efficiency_tracker.py        # Operational efficiency tracking
│   ├── data_insights.py             # Regional data analysis and visualization
│   └── report_generator.py          # Automated report generation
│
├── README.md                       # Project documentation
├── requirements.txt                 # Python dependencies
└── LICENSE                          # MIT License
```

---

##  **Installation**

### **Prerequisites**

- Python 3.8+
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `openpyxl`

### **Setup**

1. Clone the repository:
  ```bash
   git clone https://github.com/Oluchi-Efobi/regional-operations-toolkit.git
   cd regional-operations-toolkit
  ```
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```

---

##  **Quick Start**

### **1. Logistics Optimization**

Optimize distribution routes and delivery schedules:

```python
from scripts.logistics_optimizer import LogisticsOptimizer

optimizer = LogisticsOptimizer("data/schools_data.csv", "data/supply_chain_data.csv")

# Optimize delivery routes for learning materials
optimized_routes = optimizer.optimize_routes(
    start_depot="EKOEXCEL HQ",
    max_stops=20
)
print(f"Optimized routes: {optimized_routes}")

# Schedule deliveries to schools
schedule = optimizer.schedule_deliveries(
    materials=["Textbooks", "Tablets", "Projectors"],
    urgency=["High", "Medium", "Low"]
)
print(f"Delivery schedule: {schedule}")
```

### **2. Supply Chain Analyzer**

Predict stockouts and recommend replenishment:

```python
from scripts.supply_chain_analyzer import SupplyChainAnalyzer

analyzer = SupplyChainAnalyzer("data/supply_chain_data.csv")

# Predict stockouts for learning materials
stockout_risk = analyzer.predict_stockouts(
    item="Tablets",
    threshold=100  # Minimum stock level
)
print(f"Stockout risk: {stockout_risk}")

# Recommend replenishment quantities
recommendations = analyzer.recommend_replenishment(
    item="Textbooks",
    lead_time=7  # days
)
print(f"Replenishment recommendations: {recommendations}")
```

### **3. Efficiency Tracker**

Track and analyze operational efficiency:

```python
from scripts.efficiency_tracker import EfficiencyTracker

tracker = EfficiencyTracker("data/efficiency_metrics.json")

# Calculate efficiency improvement
efficiency = tracker.calculate_efficiency(
    metric="operational",
    baseline=45,  # Previous efficiency (%)
    current=100   # Current efficiency (%)
)
print(f"Efficiency improvement: {efficiency}%")

# Generate a performance report
report = tracker.generate_performance_report(
    region="Local Government A",
    schools=200,
    staff=500,
    students=5000
)
print(report)
```

### **4. Data Insights**

Analyze regional operations data:

```python
from scripts.data_insights import DataInsights

insights = DataInsights("data/schools_data.csv", "data/supply_chain_data.csv")

# Analyze regional performance
regional_analysis = insights.analyze_regional_data(
    region="Local Government B",
    metrics=["material_distribution", "teacher_productivity"]
)
print(f"Regional analysis: {regional_analysis}")

# Visualize trends (e.g., stockouts over time)
insights.visualize_trends(
    data="data/stockout_logs.csv",
    x="date",
    y="stockout_count"
)
```

### **5. Report Generator**

Automate reports for stakeholders:

```python
from scripts.report_generator import ReportGenerator

generator = ReportGenerator()

# Generate an operational efficiency report
operational_report = generator.generate_operational_report(
    period="Q1 2023",
    improvements={
        "operational_efficiency": 55,
        "stockout_reduction": 35
    },
    impact="5,000+ students"
)
print(operational_report)

# Compile a stakeholder summary
summary = generator.compile_stakeholder_summary(
    schools=200,
    staff=500,
    students=5000,
    key_achievements=[
        "55% improvement in operational efficiency",
        "35% reduction in stockouts"
    ]
)
print(summary)
```

---

##  **Example Data**

### `**data/schools_data.csv**`

```csv
school_id,school_name,local_government,administrators,teachers,students
001,EKOEXCEL Primary A,Local Government A,5,10,200
002,EKOEXCEL Secondary B,Local Government A,5,15,300
003,EKOEXCEL Primary C,Local Government B,5,10,250
```

### `**data/supply_chain_data.csv**`

```csv
item,school_id,quantity_delivered,date,stock_level
Textbooks,001,500,2023-01-15,1000
Tablets,002,100,2023-01-20,50
Projectors,003,10,2023-02-01,20
```

### `**data/efficiency_metrics.json**`

```json
{
  "operational": {
    "baseline": 45,
    "current": 100,
    "improvement": 55
  },
  "stockout_reduction": {
    "baseline": 100,
    "current": 65,
    "improvement": 35
  }
}
```

---

##  **Use Cases**


| **Scenario**                  | **Tool**                   | **Output**                         |
| ----------------------------- | -------------------------- | ---------------------------------- |
| Optimize delivery routes      | `logistics_optimizer.py`   | Optimized routes (JSON)            |
| Predict stockouts for tablets | `supply_chain_analyzer.py` | Stockout risk (Boolean)            |
| Track operational efficiency  | `efficiency_tracker.py`    | Efficiency report (Markdown)       |
| Analyze regional performance  | `data_insights.py`         | Regional analysis (DataFrame)      |
| Generate stakeholder report   | `report_generator.py`      | Stakeholder summary (Markdown/PDF) |


---

##  **Customization**

### **Extend the Toolkit**

- **Add more metrics**: Update `efficiency_metrics.json` with additional KPIs (e.g., teacher attendance, student outcomes).
- **Integrate with school management systems**: Use APIs to fetch live data from EKOEXCEL platforms.
- **Add predictive analytics**: Use `scikit-learn` to forecast resource demand.
- **Automate email reports**: Use `smtplib` to send reports to stakeholders.

### **Visualization (Optional)**

Add a **Streamlit dashboard** to visualize:

- **Logistics routes** on a map (using `folium` or `plotly`).
- **Stockout trends** over time.
- **Efficiency improvements** by region.

Example:

```python
# Install Streamlit: pip install streamlit
import streamlit as st
import pandas as pd

st.title("EKOEXCEL Regional Operations Dashboard")
df = pd.read_csv("data/stockout_logs.csv")
st.line_chart(df, x="date", y="stockout_count")
```

---

##  **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

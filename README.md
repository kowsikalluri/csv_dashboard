#  Smart CSV Dashboard & ML Insight Generator

A lightweight and interactive Streamlit-based app to:

* Upload CSV files
* Automatically clean and process data
* Generate customizable dashboards
* Run ML models on cleaned data
* Download cleaned or predicted datasets

---

##  Features

| Feature           | Description                                           |
| ----------------- | ----------------------------------------------------- |
|  Upload CSV     | Upload raw datasets                                   |
|  Auto Cleaning  | Automatically fill missing values and drop duplicates |
|  User Cleaning | Choose custom strategies for specific columns         |
|  Visualizations | Create bar, line, and scatter plots using Plotly      |
|  Stats Summary  | View missing values, column types, and distributions  |
|  ML Modeling    | Predict selected target column using Random Forest    |
|  CSV Export     | Download cleaned data or prediction results           |

---

##  Folder Structure

```
csv-dashboard-app/
├── app.py                  # Streamlit frontend controller
├── auto_cleaning.py        # Automatic data cleaning logic
├── user_cleaning.py        # Manual cleaning interface
├── dashboard.py            # Plotly visualizations
├── insights.py             # Lightweight data profiling
├── ml_model.py             # ML training and evaluation
├── requirements.txt        # All dependencies
├── .gitignore
└── README.md               # You're here :)
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/csv-dashboard-app.git
cd csv-dashboard-app
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the App

```bash
streamlit run app.py
```

---

##  Usage Instructions

1. Upload a CSV file.
2. Wait for it to be auto-cleaned.
3. Use manual cleaning options to fine-tune.
4. Visualize your data.
5. Generate stats and summaries.
6. Select a target column and train a model.
7. Download cleaned and predicted datasets.

---



---

##  Deployment

You can deploy this app publicly using:

* [Streamlit Cloud](https://streamlit.io/cloud)
* Hugging Face Spaces
* Heroku or Render

---



## 👨‍💻 Author

Built  by **Kowsik Alluri**
Contact: [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/kowsikalluri)

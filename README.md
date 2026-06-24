# 🚗 91Wheels Lead Intelligence Engine

An AI-powered Lead Intelligence Engine designed for automotive marketplaces to identify high-intent buyers, predict purchase probability, and help sales teams prioritize leads more effectively.

## Overview

This project simulates a production-grade lead qualification system for an automotive platform like 91Wheels.

Using customer behavior signals such as website visits, car comparisons, EMI calculator usage, brochure downloads, and test drive requests, the system predicts:

* Purchase Probability
* Lead Score (0–100)
* Lead Priority (High / Medium / Low)
* Dealer Recommendations

The objective is to improve lead conversion rates while reducing manual effort for sales teams.

---

## Features

### Lead Scoring

Generate a lead score based on customer engagement and buying intent.

### Purchase Prediction

Predict the likelihood of a customer purchasing a vehicle using a LightGBM model.

### Dealer Copilot

Generate actionable recommendations for dealers, including follow-up priority and suggested next actions.

### Interactive Dashboard

Built with Streamlit for real-time lead analysis and visualization.

---

## Tech Stack

* Python
* LightGBM
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Joblib

---

## Dataset Features

The model is trained on lead behavior signals including:

* Budget Range
* Purchase Timeline
* Website Visits
* Cars Compared
* EMI Calculator Usage
* Test Drive Requests
* Brochure Downloads
* Occupation

---

## Project Structure

```text
91wheels/

├── data/
│   └── 91Wheels_leads_dataset_5000.csv
│
├── models/
│   └── lead_model.pkl
│
├── train_model.py
├── predict.py
├── app.py
└── README.md
```

## Installation

```bash
git clone <repository-url>

cd 91wheels

pip install -r requirements.txt
```

## Train Model

```bash
python train_model.py
```

## Run Prediction

```bash
python predict.py
```

## Launch Dashboard

```bash
streamlit run app.py
```

---

## Sample Output

```text
Lead Score: 89/100

Purchase Probability: 89%

Priority: HIGH

Reasons:
✓ Used EMI Calculator
✓ Requested Test Drive
✓ Compared Multiple Cars
✓ Planning Purchase Soon
```

---

## Business Impact

This system demonstrates how AI can help automotive marketplaces:

* Prioritize high-intent leads
* Improve dealer productivity
* Increase lead conversion rates
* Reduce manual qualification effort
* Enable data-driven sales workflows

---

## Future Improvements

* SHAP Explainability
* Real CRM Integration
* AI Calling Agent Integration
* OEM Intelligence Dashboard
* Real-time Lead Scoring API
* Multilingual Customer Engagement

---

## Author

Deepesh Lodhi
Mechanical Engineering, IIT Delhi
AI / Product Strategy Enthusiast

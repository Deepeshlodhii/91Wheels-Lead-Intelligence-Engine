import joblib
import numpy as np

model = joblib.load(
    "models/lead_model.pkl"
)

sample = np.array([[
    15,     # budget_lakh
    30,     # purchase_timeline
    8,      # visit_count
    5,      # comparison_count
    1,      # emi_used
    1,      # test_drive
    1,      # brochure_download
    2       # occupation
]])

prob = model.predict_proba(sample)[0][1]

lead_score = int(
    prob * 100
)

print("\nLead Intelligence Report")
print("-" * 30)

print(
    f"Purchase Probability: {prob:.2%}"
)

print(
    f"Lead Score: {lead_score}/100"
)

if lead_score > 80:
    priority = "HIGH"

elif lead_score > 50:
    priority = "MEDIUM"

else:
    priority = "LOW"

print(
    f"Priority: {priority}"
)

print("\nReasons:")

if sample[0][4] == 1:
    print("✓ Used EMI Calculator")

if sample[0][5] == 1:
    print("✓ Requested Test Drive")

if sample[0][3] > 3:
    print("✓ Compared Multiple Cars")

if sample[0][1] < 60:
    print("✓ Planning Purchase Soon")
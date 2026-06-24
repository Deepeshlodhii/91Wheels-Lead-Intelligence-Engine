import streamlit as st
import joblib
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="91Wheels Lead Intelligence Engine",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load(
    "models/lead_model.pkl"
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
# 🚗 91Wheels Lead Intelligence Engine

### AI-Powered Lead Qualification & Purchase Prediction
""")

st.markdown("---")

# -----------------------------
# TWO COLUMN LAYOUT
# -----------------------------

left_col, right_col = st.columns([2, 1])

# =============================
# LEFT SIDE
# =============================

with left_col:

    st.subheader("Customer Information")

    budget = st.slider(
        "Budget (Lakhs)",
        5,
        50,
        15
    )

    timeline = st.slider(
        "Purchase Timeline (Days)",
        1,
        365,
        30
    )

    visit_count = st.slider(
        "Website Visits",
        1,
        20,
        5
    )

    comparison_count = st.slider(
        "Cars Compared",
        0,
        10,
        3
    )

    st.markdown("### Engagement Signals")

    emi_used = st.checkbox(
        "Used EMI Calculator"
    )

    test_drive = st.checkbox(
        "Requested Test Drive"
    )

    brochure = st.checkbox(
        "Downloaded Brochure"
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Private Employee",
            "Government Employee",
            "Business Owner",
            "Professional"
        ]
    )

# =============================
# RIGHT SIDE
# =============================

with right_col:

    st.subheader("Lead Intelligence")

    st.info(
        """
        This engine predicts:

        • Purchase Probability

        • Lead Score

        • Lead Priority

        • Dealer Recommendation
        """
    )

# -----------------------------
# OCCUPATION MAP
# -----------------------------

occupation_map = {
    "Student": 1,
    "Private Employee": 2,
    "Government Employee": 3,
    "Business Owner": 4,
    "Professional": 5
}

# -----------------------------
# PREDICTION BUTTON
# -----------------------------

if st.button(
    "🚀 Generate Lead Intelligence",
    use_container_width=True
):

    sample = np.array([[
        budget,
        timeline,
        visit_count,
        comparison_count,
        int(emi_used),
        int(test_drive),
        int(brochure),
        occupation_map[occupation]
    ]])

    prob = model.predict_proba(sample)[0][1]

    lead_score = int(prob * 100)

    # -----------------------------
    # PRIORITY
    # -----------------------------

    if lead_score > 80:
        priority = "HIGH"

    elif lead_score > 50:
        priority = "MEDIUM"

    else:
        priority = "LOW"

    st.markdown("---")

    st.subheader("Prediction Results")

    # -----------------------------
    # KPI CARDS
    # -----------------------------

    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Lead Score",
        f"{lead_score}/100"
    )

    k2.metric(
        "Purchase Probability",
        f"{prob:.1%}"
    )

    k3.metric(
        "Priority",
        priority
    )

    # -----------------------------
    # PRIORITY BADGE
    # -----------------------------

    if priority == "HIGH":

        st.markdown("""
        <div style="
        background-color:#d4edda;
        padding:20px;
        border-radius:10px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        color:#155724;">
        🟢 HIGH PRIORITY LEAD
        </div>
        """,
        unsafe_allow_html=True)

    elif priority == "MEDIUM":

        st.markdown("""
        <div style="
        background-color:#fff3cd;
        padding:20px;
        border-radius:10px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        color:#856404;">
        🟡 MEDIUM PRIORITY LEAD
        </div>
        """,
        unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        background-color:#f8d7da;
        padding:20px;
        border-radius:10px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        color:#721c24;">
        🔴 LOW PRIORITY LEAD
        </div>
        """,
        unsafe_allow_html=True)

    # -----------------------------
    # REASONS
    # -----------------------------

    st.markdown("---")

    st.subheader("📊 Why This Lead Scored High")

    reasons = []

    if emi_used:
        reasons.append("Used EMI Calculator")

    if test_drive:
        reasons.append("Requested Test Drive")

    if brochure:
        reasons.append("Downloaded Brochure")

    if comparison_count >= 3:
        reasons.append("Compared Multiple Cars")

    if timeline <= 60:
        reasons.append("Planning Purchase Soon")

    if visit_count >= 5:
        reasons.append("Frequent Website Visitor")

    for reason in reasons:
        st.write(f"✅ {reason}")

    # -----------------------------
    # DEALER COPILOT
    # -----------------------------

    st.markdown("---")

    st.subheader("🤖 Dealer Copilot Summary")

    st.info(
        f"""
Customer Profile

• Occupation: {occupation}

• Budget: ₹{budget} Lakh

• Expected Purchase Timeline: {timeline} Days

• Lead Score: {lead_score}/100

• Purchase Probability: {prob:.1%}

Recommended Actions

1. Contact customer within 24 hours

2. Offer test drive

3. Discuss financing options

4. Share latest offers and discounts

5. Prioritize follow-up if no response
"""
    )

    # -----------------------------
    # LEAD JOURNEY
    # -----------------------------

    st.markdown("---")

    st.subheader("🚦 Lead Journey")

    st.markdown("""
👤 Customer

⬇️

📊 Lead Intelligence Engine

⬇️

🎯 Purchase Prediction

⬇️

📞 Dealer Copilot

⬇️

🚗 Vehicle Purchase
""")
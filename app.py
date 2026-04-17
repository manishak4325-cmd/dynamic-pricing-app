import streamlit as st
import datetime
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Dynamic Pricing System", layout="centered")

# Gradient Background + Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #ffffff;
    }
    .subtitle {
        text-align: center;
        color: #d1d5db;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💰 Dynamic Pricing System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Adjust parameters to see real-time pricing</div>', unsafe_allow_html=True)

st.divider()

# Inputs
st.markdown("### 📊 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    base_price = st.number_input("💵 Base Price", min_value=0.0, value=100.0)
    demand = st.slider("📈 Demand", 0, 100, 50)

with col2:
    supply = st.slider("📉 Supply", 0, 100, 50)
    category = st.selectbox("📦 Category", ["Cab 🚗", "Flight ✈️", "Hotel 🏨"])

# Time factor
hour = datetime.datetime.now().hour
if 18 <= hour <= 22:
    time_factor = 1.5
    st.warning("⏰ Peak Hours: Higher Pricing Applied")
else:
    time_factor = 1.0
    st.info("🕒 Normal Hours Pricing")

# Category adjustment
if category == "Flight ✈️":
    time_factor += 0.2
elif category == "Hotel 🏨":
    time_factor += 0.1

# Avoid division by zero
if supply == 0:
    supply = 1

# Calculation
demand_factor = 1 + (demand / 100)
supply_factor = 1 + (supply / 100)

final_price = base_price * demand_factor * time_factor / supply_factor

# Output
st.divider()
st.markdown("## 💵 Final Price")
st.success(f"₹ {round(final_price, 2)}")

# Explanation
with st.expander("📊 See Calculation Details"):
    st.write(f"Demand Factor: {round(demand_factor, 2)}")
    st.write(f"Supply Factor: {round(supply_factor, 2)}")
    st.write(f"Time Factor: {time_factor}")


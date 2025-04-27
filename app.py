import streamlit as st
import csv
import os
from datetime import datetime

# Function to store data in CSV file
def save_to_csv(data):
    file_exists = os.path.isfile('audi_recommendations.csv')
    
    with open('audi_recommendations.csv', mode='a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Budget', 'Vehicle Type', 'Features', 'Recommended Cars', 'Timestamp'])
        
        # Write data
        writer.writerow(data)

# Function to format price in Indian currency system (lakhs and crores)
def format_indian_currency(amount):
    if amount >= 100:
        crores = amount / 100
        return f"₹{crores:.2f} Crores"
    else:
        return f"₹{amount:.2f} Lakhs"

# Set page config
st.set_page_config(
    page_title="Audi Vehicle Selector",
    page_icon="🚗",
    layout="centered"
)

# Apply custom CSS styling for a professional tech look
st.markdown("""
<style>
    .main {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stButton button {
        background-color: #d50000;
        color: white;
        border-radius: 2px;
        padding: 10px 25px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton button:hover {
        background-color: #ff1744;
        box-shadow: 0 0 15px rgba(213, 0, 0, 0.5);
    }
    h1, h2, h3 {
        font-family: 'Arial', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .top-banner {
        background: linear-gradient(90deg, #000000, #212121);
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        border-bottom: 3px solid #d50000;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    .car-container {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 4px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        margin: 15px 0;
        border-left: 3px solid #d50000;
    }
    .recommendation {
        background-color: #252525;
        padding: 15px;
        border-left: 4px solid #d50000;
        margin: 10px 0;
        border-radius: 2px;
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        from {
            box-shadow: 0 0 5px rgba(213, 0, 0, 0.2);
        }
        to {
            box-shadow: 0 0 15px rgba(213, 0, 0, 0.6);
        }
    }
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .stSlider > div > div > div {
        background-color: #d50000 !important;
    }
    .stTextInput > div > div > input {
        background-color: #252525;
        color: #e0e0e0;
        border-radius: 2px;
        border: 1px solid #333;
    }
    .tech-line {
        height: 3px;
        background: linear-gradient(90deg, transparent, #d50000, transparent);
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        background-color: #1a1a1a;
        border-radius: 3px;
        border-top: 1px solid #333;
    }
    .stCheckbox label p {
        color: #e0e0e0 !important;
    }
    .feature-badge {
        display: inline-block;
        padding: 3px 8px;
        margin: 2px;
        background-color: #333;
        color: #fff;
        border-radius: 3px;
        font-size: 12px;
    }
    .car-card {
        background-color: #252525;
        padding: 15px;
        margin: 10px 0;
        border-left: 2px solid #d50000;
        transition: all 0.3s;
    }
    .car-card:hover {
        transform: translateX(5px);
        box-shadow: -5px 0 10px rgba(213, 0, 0, 0.3);
    }
    .car-features span {
        display: inline-block;
        margin: 3px;
        padding: 2px 6px;
        background-color: #333;
        font-size: 10px;
        border-radius: 2px;
    }
    .selector-container {
        background-color: #1a1a1a;
        padding: 5px;
        border-radius: 2px;
        margin-bottom: 10px;
    }
    .price-display {
        color: #e0e0e0;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Display top banner with logo
st.markdown(f"""
<div class="top-banner">
    <div class="logo-container">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 60" width="180">
          <circle cx="50" cy="30" r="15" fill="none" stroke="#FFFFFF" stroke-width="2"/>
          <circle cx="85" cy="30" r="15" fill="none" stroke="#FFFFFF" stroke-width="2"/>
          <circle cx="120" cy="30" r="15" fill="none" stroke="#FFFFFF" stroke-width="2"/>
          <circle cx="155" cy="30" r="15" fill="none" stroke="#FFFFFF" stroke-width="2"/>
        </svg>
    </div>
    <h1>AUDI VEHICLE SELECTOR</h1>
    <p style="color: #aaa;">Premium Automotive Excellence</p>
</div>
""", unsafe_allow_html=True)

# Enhanced Audi Car Data with categories and features
audi_cars = {
    "Q8": {
        "price": 107, 
        "type": "SUV", 
        "features": ["Quattro AWD", "MMI Navigation", "Panoramic Sunroof", "Adaptive Air Suspension", "Bang & Olufsen Sound"]
    },
    "Q8 e-tron": {
        "price": 114, 
        "type": "Electric SUV", 
        "features": ["Electric Powertrain", "400+ km Range", "Fast Charging", "Quattro AWD", "Digital Matrix LED Headlights"]
    },
    "e-tron GT": {
        "price": 172, 
        "type": "Electric Sportback", 
        "features": ["High-Performance Electric", "Boost Mode", "Adaptive Air Suspension", "Matrix LED Headlights", "Carbon Fiber Elements"]
    },
    "A4": {
        "price": 45.34, 
        "type": "Sedan", 
        "features": ["Turbocharged Engine", "Virtual Cockpit", "Audi Drive Select", "Pre-sense Safety", "LED Headlights"]
    },
    "A5": {
        "price": 60.00, 
        "type": "Sportback", 
        "features": ["Sport Suspension", "S-Line Exterior", "Virtual Cockpit", "MMI Touch", "B&O Sound System"]
    },
    "A6": {
        "price": 64.00, 
        "type": "Sedan", 
        "features": ["Mild Hybrid System", "Quattro AWD", "Adaptive Cruise", "MMI Navigation Plus", "Matrix LED Headlights"]
    },
    "Q3": {
        "price": 42.77, 
        "type": "Compact SUV", 
        "features": ["Quattro AWD", "Panoramic Sunroof", "Virtual Cockpit", "MMI Touch", "Progressive Steering"]
    },
    "Q5": {
        "price": 65.18, 
        "type": "SUV", 
        "features": ["TFSI Engine", "Quattro Ultra", "Adaptive Dampers", "Virtual Cockpit Plus", "Bang & Olufsen 3D Sound"]
    }
}

# Create a more professional title
st.markdown("<div class='tech-line'></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #e0e0e0;'>AUDI PREMIUM VEHICLE FINDER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Find your perfect Audi match with our advanced selection tool</p>", unsafe_allow_html=True)
st.markdown("<div class='tech-line'></div>", unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='car-container'>", unsafe_allow_html=True)
    st.subheader("CUSTOMER DETAILS")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='car-container'>", unsafe_allow_html=True)
    st.subheader("BUDGET INFORMATION")
    
    # Convert slider values to display in crores when necessary
    min_budget = 40  # in lakhs
    max_budget = 200  # in lakhs
    step_budget = 5   # in lakhs
    
    budget = st.slider("Budget Range", 
                   min_value=min_budget, 
                   max_value=max_budget, 
                   step=step_budget,
                   value=60,
                   format="%d")
    
    # Format budget display in Indian currency format
    budget_display = format_indian_currency(budget)
    st.markdown(f"<h3 style='color:#e0e0e0; text-align: center;'>{budget_display}</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Vehicle type and features selection
st.markdown("<div class='car-container'>", unsafe_allow_html=True)
st.subheader("VEHICLE PREFERENCES")

# Get unique vehicle types
vehicle_types = list(set(car_data["type"] for car_data in audi_cars.values()))
vehicle_types.sort()

# Vehicle type selection
selected_vehicle_types = []
st.markdown("<div class='selector-container'>", unsafe_allow_html=True)
st.write("**Select Vehicle Category:**")
col1, col2 = st.columns(2)
with col1:
    for vtype in vehicle_types[:len(vehicle_types)//2 + len(vehicle_types)%2]:
        if st.checkbox(vtype, value=True, key=f"vt_{vtype}"):
            selected_vehicle_types.append(vtype)
with col2:
    for vtype in vehicle_types[len(vehicle_types)//2 + len(vehicle_types)%2:]:
        if st.checkbox(vtype, value=True, key=f"vt_{vtype}"):
            selected_vehicle_types.append(vtype)
st.markdown("</div>", unsafe_allow_html=True)

# Get all unique features
all_features = []
for car_data in audi_cars.values():
    all_features.extend(car_data["features"])
unique_features = list(set(all_features))
unique_features.sort()

# Feature selection
selected_features = []
st.markdown("<div class='selector-container'>", unsafe_allow_html=True)
st.write("**Select Desired Features:**")
col1, col2, col3 = st.columns(3)
column_size = len(unique_features) // 3 + (1 if len(unique_features) % 3 > 0 else 0)

for i, col in enumerate([col1, col2, col3]):
    with col:
        start_idx = i * column_size
        end_idx = min(start_idx + column_size, len(unique_features))
        for feature in unique_features[start_idx:end_idx]:
            if st.checkbox(feature, key=f"feat_{feature}"):
                selected_features.append(feature)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Recommendation Logic
if st.button("FIND MY PERFECT AUDI"):
    if name and email:
        st.markdown("<div class='tech-line'></div>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #d50000;'>RECOMMENDED VEHICLES</h2>", unsafe_allow_html=True)
        st.markdown("<div class='recommendation'>", unsafe_allow_html=True)
        
        # Filter cars based on budget, type and features
        recommended_cars = []
        
        for car_name, car_data in audi_cars.items():
            # Check if price is within budget
            if car_data["price"] > budget:
                continue
                
            # Check if vehicle type matches selection (if any selected)
            if selected_vehicle_types and car_data["type"] not in selected_vehicle_types:
                continue
                
            # Check if car has at least one selected feature (if any selected)
            if selected_features:
                has_feature = False
                for feature in selected_features:
                    if feature in car_data["features"]:
                        has_feature = True
                        break
                if not has_feature:
                    continue
                    
            # If passed all filters, add to recommendations
            recommended_cars.append(car_name)
        
        if recommended_cars:
            st.markdown(f"<p style='color: #aaa;'>Based on your preferences, we found {len(recommended_cars)} vehicles that match your criteria.</p>", unsafe_allow_html=True)
            st.success(f"Here are the Audi models within your budget of {budget_display}:")
            
            # Display recommended cars with details
            for car in recommended_cars:
                car_data = audi_cars[car]
                car_price_display = format_indian_currency(car_data["price"])
                
                st.markdown(f"""
                <div class='car-card'>
                    <div style='display: flex; justify-content: space-between;'>
                        <span style='color: #d50000; font-weight: bold; font-size: 18px;'>{car}</span>
                        <span style='color: #aaa;'>{car_price_display}</span>
                    </div>
                    <div style='margin: 5px 0;'>
                        <span class='feature-badge'>{car_data['type']}</span>
                    </div>
                    <div class='car-features'>
                        {' '.join([f"<span>{feature}</span>" for feature in car_data['features']])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("We couldn't find any vehicles matching your criteria. Please adjust your preferences to see more options.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Store User Data in CSV file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_csv([
            name, 
            email, 
            budget_display, 
            ", ".join(selected_vehicle_types) if selected_vehicle_types else "All", 
            ", ".join(selected_features) if selected_features else "Any",
            ", ".join(recommended_cars), 
            timestamp
        ])
        
        st.markdown("""
        <div style='text-align: center; padding: 10px; color: #aaa;'>
        Your vehicle preferences have been saved. A consultant will contact you shortly.
        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("Please provide your name and email to view vehicle recommendations.")

# Footer
st.markdown("""
<div class='footer'>
    <p style='color: #aaa; font-size: 12px;'>Audi Premium Vehicle Selector</p>
    <p style='color: #888; font-size: 10px;'>© 2025 | Vorsprung durch Technik</p>
</div>
""", unsafe_allow_html=True)
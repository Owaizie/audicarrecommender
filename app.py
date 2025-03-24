# -*- coding: utf-8 -*-
"""AUDICAR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tW2CPumKD_Kun7dPHbZ_LvCLZFOuQZIm
"""

#import streamlit as st
 # Set up the app title st.title("🚗 Audi Car Recommender") # Ask the user for their preferences budget = st.slider("Select Your Budget (in Lakhs)", 30, 150, 50) fuel_type = st.radio("Preferred Fuel Type", ["Petrol", "Diesel", "Electric"]) car_type = st.selectbox("Select Car Type", ["Sedan", "SUV", "Coupe", "Convertible"]) # Car recommendation logic def recommend_car(budget, fuel_type, car_type): if budget < 40: return "Audi A3 - Best entry-level luxury sedan!" elif 40 <= budget < 70: if fuel_type == "Electric": return "Audi Q4 e-tron - A premium electric SUV!" return "Audi A6 - A perfect balance of luxury and performance!" elif 70 <= budget < 100: if car_type == "SUV": return "Audi Q7 - A powerful and spacious SUV!" return "Audi A8 - Ultimate luxury sedan!" else: return "Audi R8 - Supercar experience! 🚀" # Get the recommendation recommended_car = recommend_car(budget, fuel_type, car_type) # Show the result st.subheader("🔥 Recommended Audi Car for You:") st.success(recommended_car)



import streamlit as st

# Set up the app title
#st.title("🚗 Audi Car Recommender")

# Ask the user for their preferences
#budget = st.slider("Select Your Budget (in Lakhs)", 30, 150, 50)#
#fuel_type = st.radio("Preferred Fuel Type", ["Petrol", "Diesel", "Electric"])#
#car_type = st.selectbox("Select Car Type", ["Sedan", "SUV", "Coupe", "Convertible"])#

# Car recommendation logic
#def recommend_car(budget, fuel_type, car_type):
    #if budget < 40:
        #return "Audi A3 - Best entry-level luxury sedan!"
    #elif 40 <= budget < 70:
        #if fuel_type == "Electric":
            #return "Audi Q4 e-tron - A premium electric SUV!"
       # return "Audi A6 - A perfect balance of luxury and performance!"
    #elif 70 <= budget < 100:
        #if car_type == "SUV":
            #return "Audi Q7 - A powerful and spacious SUV!"
        #return "Audi A8 - Ultimate luxury sedan!"
    #else:
        #return "Audi R8 - Supercar experience! 🚀"#

# Get the recommendation
#recommended_car = recommend_car(budget, fuel_type, car_type)

# Show the result
#st.subheader("🔥 Recommended Audi Car for You:")
#st.success(recommended_car)
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from google.oauth2 import service_account
import json
from google.oauth2.service_account import Credentials





# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_service_account_info(st.secrets["gcp_service_account"])
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Audi Car Recommender User Data").sheet1  # First sheet

# Audi Car Data (Updated with Prices in Lakhs)
audi_cars = {
    "Q8": 107, "Q8 e-tron": 114, "e-tron GT": 172,
    "A4": 45.34, "A5": 60.00, "A6": 64.00,
    "Q3": 42.77, "Q5": 65.18
}

# Streamlit UI
st.title("🚗 Audi Car Recommender")
st.write("Find the best Audi car within your budget!")

# User Inputs
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")

# Budget Slider
budget = st.slider("Select Your Budget (in Lakhs)", 
                   min_value=40, 
                   max_value=200, 
                   step=5)
st.markdown(f"<h3 style='color:green;'>Your Budget: ₹{budget} Lakhs</h3>", unsafe_allow_html=True)

# Recommendation Logic
if st.button("Get Recommendations"):
    if name and email:
        recommended_cars = [car for car, price in audi_cars.items() if price <= budget]
        if recommended_cars:
            st.success(f"🚘 Based on your budget ({budget}L), you can buy: {', '.join(recommended_cars)}")
        else:
            st.warning("⚠️ No cars match your budget. Consider increasing it.")

        # Store User Data in Google Sheets
        sheet.append_row([name, email, budget, ", ".join(recommended_cars)])
        st.success("✅ Your details have been saved successfully!")

    else:
        st.error("❌ Please enter your name and email.")





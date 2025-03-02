import streamlit as st
import requests

# Function to get latitude & longitude from Open-Meteo Geocoding API
def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
    return None, None

# Function to get weather data from Open-Meteo API
def get_weather(city):
    lat, lon = get_coordinates(city)
    
    if lat is None or lon is None:
        return None  # Invalid city
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=Asia/Kolkata"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["daily"]["temperature_2m_max"][0]  # Today's max temperature
    return None

# Crop recommendations based on temperature
def recommend_crops(temp):
    if temp is None:
        return ["Weather data not available"]
    elif temp < 15:
        return ["Wheat", "Barley", "Peas"]
    elif 15 <= temp < 25:
        return ["Tomato", "Potato", "Carrots"]
    elif 25 <= temp < 35:
        return ["Rice", "Maize", "Banana"]
    else:
        return ["Millets", "Sorghum", "Sugarcane"]

# Streamlit UI
st.title("🌱 Crop Recommendation System")

city = st.text_input("Enter your city")

if st.button("Get Recommendations"):
    temperature = get_weather(city)
    
    if temperature is not None:
        st.write(f"🌡️ Current max temperature in {city}: {temperature}°C")
    
    crops = recommend_crops(temperature)
    st.success(f"Recommended crops for {city}: {', '.join(crops)}")

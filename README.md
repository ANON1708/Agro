# Agro

# 🌱 Crop Recommendation System using Real-Time Weather API

## 🚀 Problem Statement: Why This Project?
Agriculture is **heavily dependent on climate conditions**, and farmers need **accurate recommendations** on which crops to grow based on real-time weather data.  
This project provides **dynamic crop recommendations** based on the user's **location and current temperature** using **Open-Meteo APIs**.

### **🔍 Key Features**
✅ Accepts **any city name** as input.  
✅ Fetches **real-time temperature** from Open-Meteo API.  
✅ Dynamically recommends **best-suited crops** based on temperature.  
✅ **Interactive web app** using **Streamlit**.

---

## **💻 Tech Stack Used**
| Technology  | Purpose  |
|-------------|---------|
| **Python**  | Core programming language |
| **Streamlit** | Web app framework |
| **Open-Meteo API** | Real-time weather and geolocation |
| **Requests** | API calls to fetch temperature data |
| **Zsh / Terminal** | Running the application |

---

## **⚙️ Setup Instructions**
### **1️⃣ Install Dependencies**
Make sure you have Python installed, then run:
```bash
pip install streamlit requests
```

### **2️⃣ Run the Application**
```bash
streamlit run crop_recommendation.py
```

### **3️⃣ Open the App in Your Browser**
- If it doesn’t open automatically, **copy and paste** this into your browser:
  ```
  http://localhost:8501
  ```

---

## **📌 How It Works**
1. User Inputs a City (e.g., `"Delhi"`).
2. Geocoding API converts it to latitude/longitude.
3. Weather API fetches today's max temperature.
4. Temperature-based crop recommendations are displayed.

---

## **🌿 Example Outputs**
![image](https://github.com/user-attachments/assets/31ed3d7c-be76-443d-917f-9abf5e6e26b9)

![image](https://github.com/user-attachments/assets/6f3ca7c4-cbf2-4ed3-bb9a-b58c389b0493)

---

## **💡 Future Enhancements**
  
🔹 Use **machine learning** for more precise suggestions.  
🔹 Add **historical trends & seasonal insights**.  

---

## **💡 To run**
Install dependencies :Streamlit
python3 -m streamlit run crop_recommendation.py

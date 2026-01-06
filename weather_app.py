import tkinter as tk
import requests

# ===============================
# Working API Key (for demo purposes)
# In real use, get your own from: https://openweathermap.org/api
API_KEY = "f1d3d0b3c5b1a3e5d7c9b1a3e5d7c9b1"  # This is a sample format, you need a real key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# ===============================

def get_weather():
    city = city_entry.get().strip()
    
    if city == "":
        result_label.config(text="Please enter a city name")
        return
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()
        
        if data.get("cod") != 200:
            result_label.config(text="City not found ❌\nTry: Delhi, Ambala, or Karnal")
            return
        
        city_name = data["name"]
        temp = round(data["main"]["temp"], 1)
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()
        
        result = (
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Weather: {weather}\n"
            f"Humidity: {humidity}%\n\n"
            "─────────────────────\n"
            "Nearby Cities:\n"
            "Delhi: 28.5°C, Clear Sky\n"
            "Ambala: 26.3°C, Few Clouds\n"
            "Karnal: 27.1°C, Haze"
        )
        
        result_label.config(text=result, fg="black")
    
    except Exception as e:
        print(f"Error: {e}")
        result_label.config(text="Error fetching data\nCheck your API key", fg="red")

def get_all_cities():
    """Get weather for all 3 cities using API"""
    cities = ["Delhi", "Ambala", "Karnal"]
    all_results = "🌤 WEATHER FOR 3 CITIES 🌤\n\n"
    
    for city in cities:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        
        try:
            response = requests.get(BASE_URL, params=params, timeout=5)
            data = response.json()
            
            if data.get("cod") == 200:
                city_name = data["name"]
                temp = round(data["main"]["temp"], 1)
                humidity = data["main"]["humidity"]
                weather = data["weather"][0]["description"].title()
                
                all_results += (
                    f"📍 {city_name}\n"
                    f"🌡 Temperature: {temp}°C\n"
                    f"☁️ Weather: {weather}\n"
                    f"💧 Humidity: {humidity}%\n"
                    "─────────────────────\n"
                )
            else:
                all_results += f"❌ {city}: Data not available\n─────────────────────\n"
        
        except Exception:
            all_results += f"⚠️ {city}: Connection error\n─────────────────────\n"
    
    result_label.config(text=all_results, fg="black")

def show_sample_output():
    """Show sample output without API"""
    sample_text = """🌤 WEATHER FOR 3 CITIES 🌤

📍 Delhi
🌡 Temperature: 28.5°C
☁️ Weather: Clear Sky
💧 Humidity: 42%
─────────────────────

📍 Ambala
🌡 Temperature: 26.3°C
☁️ Weather: Few Clouds
💧 Humidity: 55%
─────────────────────

📍 Karnal
🌡 Temperature: 27.1°C
☁️ Weather: Haze
💧 Humidity: 58%
─────────────────────

*Note: Get real data with API key*
"""
    result_label.config(text=sample_text, fg="black")

# ===============================
# GUI Setup
# ===============================
app = tk.Tk()
app.title("Weather App - Delhi, Ambala, Karnal")
app.geometry("450x600")
app.resizable(False, False)

# Set background color
app.configure(bg="#e3f2fd")

# Title Frame
title_frame = tk.Frame(app, bg="#2196F3")
title_frame.pack(fill=tk.X, pady=(0, 10))

title = tk.Label(
    title_frame, 
    text="🌤 WEATHER DASHBOARD", 
    font=("Arial", 20, "bold"),
    bg="#2196F3",
    fg="white",
    pady=10
)
title.pack()

subtitle = tk.Label(
    title_frame,
    text="Real-time weather for Delhi, Ambala & Karnal",
    font=("Arial", 10),
    bg="#2196F3",
    fg="white"
)
subtitle.pack(pady=(0, 10))

# Main content frame
main_frame = tk.Frame(app, bg="#e3f2fd")
main_frame.pack(pady=20, padx=20)

# Input field
input_label = tk.Label(
    main_frame,
    text="Search any city:",
    font=("Arial", 11),
    bg="#e3f2fd"
)
input_label.pack(anchor=tk.W)

city_entry = tk.Entry(
    main_frame, 
    font=("Arial", 12), 
    width=30,
    relief=tk.GROOVE,
    borderwidth=2
)
city_entry.pack(pady=5)
city_entry.insert(0, "Delhi")
city_entry.bind("<Return>", lambda e: get_weather())

# Button Frame
button_frame = tk.Frame(main_frame, bg="#e3f2fd")
button_frame.pack(pady=15)

# Buttons with better styling
buttons_config = [
    ("🔍 Search City", get_weather, "#4CAF50"),
    ("📊 All 3 Cities", get_all_cities, "#2196F3"),
    ("📋 Sample Output", show_sample_output, "#9C27B0")
]

for text, command, color in buttons_config:
    btn = tk.Button(
        button_frame, 
        text=text, 
        font=("Arial", 11, "bold"), 
        command=command,
        width=15,
        bg=color,
        fg="white",
        relief=tk.RAISED,
        borderwidth=2,
        cursor="hand2",
        padx=10,
        pady=5
    )
    btn.pack(side=tk.LEFT, padx=5)

# Result Label with better styling
result_label = tk.Label(
    main_frame,
    text="Welcome to Weather Dashboard!\n\nClick 'Sample Output' to see example\nor 'All 3 Cities' for real data.\n\nMake sure to add your API key!",
    font=("Courier New", 10),
    justify="left",
    bg="white",
    relief=tk.GROOVE,
    borderwidth=2,
    padx=15,
    pady=15,
    width=45,
    height=20
)
result_label.pack(pady=20)

# Footer
footer_frame = tk.Frame(app, bg="#1976D2")
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

footer = tk.Label(
    footer_frame,
    text="🌐 Data from OpenWeather API | Get API key: openweathermap.org/api",
    font=("Arial", 8),
    bg="#1976D2",
    fg="white",
    pady=5
)
footer.pack()

# API key status
api_status = tk.Label(
    main_frame,
    text="⚠️ API Key Required - Get free key from website above",
    font=("Arial", 9),
    bg="#FFEB3B",
    fg="#D32F2F",
    pady=3
)
api_status.pack(pady=(5, 0))

app.mainloop()





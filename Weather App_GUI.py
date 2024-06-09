import tkinter as tk
from tkinter import ttk
import requests

# Replace 'your_api_key_here' with your actual API key
API_KEY = '835bc25da46e6051a6ce246a37272880'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data:
            weather_info = f"City: {weather_data['name']}\n"
            weather_info += f"Temperature: {weather_data['main']['temp']}°C\n"
            weather_info += f"Weather: {weather_data['weather'][0]['description']}"
            result_label.config(text=weather_info)
        else:
            result_label.config(text="City not found or error fetching data.")
    else:
        result_label.config(text="Please enter a city name.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg='#ADD8E6')

# Create and place the widgets using ttk for better UI
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), background='#ADD8E6', foreground='#333')
style.configure('TButton', font=('Helvetica', 12), background='#ADD8E6', foreground='#333')
style.configure('TEntry', font=('Helvetica', 12))

frame = ttk.Frame(root, padding="10 10 10 10", style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor='center')

city_label = ttk.Label(frame, text="Enter city name:", style='TLabel')
city_label.grid(row=0, column=0, pady=10)

city_entry = ttk.Entry(frame, width=30, style='TEntry')
city_entry.grid(row=1, column=0, pady=10)

get_weather_button = ttk.Button(frame, text="Get Weather", command=show_weather, style='TButton')
get_weather_button.grid(row=2, column=0, pady=20)

result_label = ttk.Label(frame, text="", wraplength=300, justify="center", style='TLabel')
result_label.grid(row=3, column=0, pady=10)

# Run the application
root.mainloop()

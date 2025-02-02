from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

data_store = {}

API_KEY = "67cdcff9e0394b0b87f153643253001"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    data = request.json
    city = data.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY})
    
    if response.status_code == 200:
        weather_data = response.json()
        formatted_data = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        data_store[city] = formatted_data
        return jsonify({"message": "Data fetched and stored", "data": formatted_data})
    else:
        return jsonify({"error": "Data for this city is not present"}), 404

if __name__ == '__main__':
    app.run(host='192.168.31.195', port=5001)

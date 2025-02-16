from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VM2_URL = "http://192.168.31.195:5001/fetch_data"  # Replace with actual VM2 IP

@app.route('/analyze_data', methods=['POST'])
def analyze_data():
    data = request.json
    city = data.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    # Fetch stored data from VM2
    response = requests.post(VM2_URL, json={"city": city})

    if response.status_code != 200:
        return jsonify({"error": "Data for this city is not present"}), 404

    weather_data = response.json().get("data", {})
    
    if not weather_data:
        return jsonify({"error": "No data available"}), 404

    temp_celsius = weather_data['current']['temp_c']  # Directly using Celsius from API

    analysis = {
        "city": city,
        "temperature_celsius": round(temp_celsius, 2),
        "condition": weather_data['current']['condition']['text'],
        "icon": weather_data['current']['condition']['icon']
    }

    return jsonify({"message": "Analysis complete", "analysis": analysis})

if __name__ == '__main__':
    app.run(host='192.168.31.151', port=5002)

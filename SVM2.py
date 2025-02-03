from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

data_store = {}

# API Key stored in a variable
API_KEY = "67cdcff9e0394b0b87f153643253001"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    data = request.json
    city = data.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400
    
    # Making the API request
    response = requests.get(BASE_URL, params={"q": city, "key": API_KEY, "lang": "En"})
    
    if response.status_code == 200:
        weather_data = response.json()
        
        formatted_data = {
            "location": weather_data["location"],
            "current": weather_data["current"]
        }
        
        data_store[city] = formatted_data
        return jsonify({"message": "Data fetched and stored", "data": formatted_data})
    else:
        return jsonify({"error": "Data for this city is not present"}), 404

if __name__ == '__main__':
    app.run(host='192.168.31.195', port=5001)

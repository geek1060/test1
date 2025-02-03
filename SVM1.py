from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define VM endpoints
VM2_URL = "http://192.168.31.195:5001/fetch_data"  # Replace with actual VM2 IP
VM3_URL = "http://192.168.31.151:5002/analyze_data"  # Replace with actual VM3 IP

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    city = data.get("city")
    operation = data.get("operation")  # 'fetch' or 'analyze'

    if not city or not operation:
        return jsonify({"error": "City and operation are required"}), 400

    if operation == "fetch":
        response = requests.post(VM2_URL, json={"city": city})
    elif operation == "analyze":
        response = requests.post(VM3_URL, json={"city": city})
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return response.json()

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        city = data.get('city')
        operation = data.get('operation')
        # Your logic here
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='192.168.31.186', port=5000)

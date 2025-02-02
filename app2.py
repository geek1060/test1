from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Mock order database
orders = []

PRODUCT_SERVICE_URL = "http://192.168.31.186:5000/products"

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Check product availability
    response = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
    if response.status_code != 200:
        return jsonify({"error": "Product not found"}), 404

    product = response.json()
    if product['stock'] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Create order
    order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product['price'] * quantity,
    }
    orders.append(order)
    return jsonify(order), 201

# Add this new endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='192.168.31.195', port=5001)

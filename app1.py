from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock product database
products = [
    {"id": 1, "name": "MacBook", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Samsung123", "price": 499.99, "stock": 20},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return jsonify(product) if product else ("Product not found", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

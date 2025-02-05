from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock user database
users = [
    {"id": 1, "username": "shrey", "email": "shrey@mystore.com"},
    {"id": 2, "username": "geek", "email": "geek@care.com"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

if __name__ == '__main__':
    app.run(host='192.168.31.151', port=5002)

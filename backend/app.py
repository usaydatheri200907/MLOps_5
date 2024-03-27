from flask import Flask, request, jsonify, render_template, send_file
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://database:27017/webapp"
mongo = PyMongo(app)

# Route to serve the index.html file
@app.route('/')
def index():
    return send_file('index.html')

# Route to handle the POST request from the frontend
@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        mongo.db.users.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data stored successfully.'}), 200
    else:
        return jsonify({'error': 'Name and email are required.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

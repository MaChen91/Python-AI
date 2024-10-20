# python-backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/python-api')
def hello_world():
    return jsonify(message="Hello from Python!")

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/api/data",methods=['GET'])

def get_data():
    data = {
        'message': "Hello World, from Flask"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
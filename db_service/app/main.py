from flask import Flask, request, jsonify
from flask_cors import CORS
from WKPython.final.db_operations import sqlite3_ops as db

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_handler():
    print("Inside get handler")
    response = jsonify(message='<h1>Hello from Webhook Listener!</h1>')
    return response

@app.route('/', methods=['POST'])
# @cross_origin()
def post_handler():
    req_data = request.get_json()
    write_to_db(req_data)
    return 'Data sent successfully'

def write_to_db(req_data):
    conn = db.initialize_conn()
    print(req_data)
    name, age, address, mobile, status = req_data.values()
    db.create_patient(conn, name, age, address, mobile, status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
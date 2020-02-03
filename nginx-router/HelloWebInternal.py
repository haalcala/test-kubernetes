from flask import Flask, request, jsonify
from datetime import datetime as dt
import uuid
import os

nodeid = uuid.uuid4()

app = Flask(__name__)

version = os.getenv('PYTHON_HELLO_WEB_INTERNAL_VERSION', '1111')

print("nodeid:", nodeid, 'version:', version)


@app.route("/", methods=['GET'])
def analyse_sentiment():
    return "Node ID: " + str(nodeid) + " Hello World Internal !!!!   " + str(dt.now()) + " VERSION " + version + " !!!!!!"

@app.route("/get_node_id", methods=['GET'])
def get_node_id():
    return "Node ID: " + str(nodeid) + " Hello World Internal !!!!   " + str(dt.now()) + " VERSION " + version + " !!!!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


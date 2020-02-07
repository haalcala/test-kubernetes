from flask import Flask, request, jsonify
from datetime import datetime as dt
import uuid
import requests 
from requests.exceptions import HTTPError
import os
import sys

nodeid = uuid.uuid4()

print(os.getenv('PYTHON_HELLO_WEB_INTERNAL_SVC_HOST', 'localhost'))

URL = "http://{}/get_node_id".format(os.getenv('PYTHON_HELLO_WEB_INTERNAL_SVC_HOST', 'localhost'))

print('URL:', URL, "nodeid:", nodeid)

app = Flask(__name__)

version = os.getenv('PYTHON_HELLO_WEB_VERSION', '1111')

message = os.getenv('PYTHON_HELLO_WEB_MSG', 'Hello World !!!!')

print('message:', message)

@app.route("/", methods=['GET'])
def default():
    return "Node ID: " + str(nodeid) + " " + message + " " + str(dt.now()) + " VERSION " + version + " !!!!!!"


@app.route("/internal", methods=['GET'])
def contact_other_nodes():
  print('contact_other_nodes(/internal)::')
  try:
    print('contact_other_nodes(/internal):: Connecting to URL', URL)
    r = requests.get(url = URL)
    data = r.text
    print('data:', data)
    return "Node ID: " + str(nodeid) + " Hello World !!!!   " + str(dt.now()) + " VERSION " + version + " !!!!!! data from internal node: " + data
  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
  except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
  else:
    print('Success!')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


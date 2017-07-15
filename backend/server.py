from flask import Flask, jsonify, request
from flask_cors import CORS 
import sys, requests
import simplejson as json
from pprint import pprint 

app = Flask(__name__)
CORS(app)

ticksmith_key = ""
ticksmith_email = ""

with open('keys.json') as infile:
    temp = json.load(infile)
    ticksmith_key = temp['ticksmith_key']
    ticksmith_email = temp['ticksmith_email']

HOST=None

if len(sys.argv)>1 and sys.argv[1] == "prod":
    HOST = '0.0.0.0'

@app.route('/')
def hello():
    return 'hello'

@app.route('/ticksmith', methods=['POST'])
def ticksmith():
    return "temp"

@app.route('/get_risk', methods=['POST'])
def get_risk():
    body = request.json
    return jsonify({"res" : "1. Low (<10%)"})

'''
Helper functions
'''

def get_ticksmith_token():
    global ticksmith_key
    global ticksmith_email
    base_url = "https://trdata.tickvault.com/sso/token"
    headers = {"Accept" : "application/json"}
    payload = {'grant_type' : 'client_credentials'}
    pprint(ticksmith_email)

    pprint(ticksmith_key)
    r = requests.post(base_url, headers=headers, data=payload, auth=(ticksmith_email, ticksmith_key))
    ticksmith_token = r.json()['access_token']
    return ticksmith_token

'''
TEST ENDPOINTS
'''

@app.route('/test')
def test():
    res = get_ticksmith_token()
    return jsonify({"res" : res})

if __name__ == "__main__":
    app.run(debug=True, host=HOST, threaded=True)
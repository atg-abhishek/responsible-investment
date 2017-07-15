from flask import Flask 
import sys 

app = Flask(__name__)

HOST=None

if len(sys.argv)>1 and sys.argv[1] == "prod":
    HOST = '0.0.0.0'

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True, host=HOST, threaded=True)
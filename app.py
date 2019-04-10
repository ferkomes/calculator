from flask import Flask, request
n = request.args.get("n")
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), debug=True)

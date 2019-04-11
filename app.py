from flask import Flask, render_template, request
import os
import sys

app = Flask(__name__)

@app.route('/')
def input_request():
    return render_template('input_request.html')

@app.route('/',methods = ['POST'])
def result():
    result = request.form
    return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), debug=True)

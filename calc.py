from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)





#FirstNumber = input()
#SecondNumber = input()
#FirstNumber=int(FirstNumber)
#SecondNumber=int(SecondNumber)

#print(FirstNumber+SecondNumber)

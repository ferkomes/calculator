from flask import Flask
import sys

calc = Flask(__name__)

@calc.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    calc.run(debug=True)





#FirstNumber = input()
#SecondNumber = input()
#FirstNumber=int(FirstNumber)
#SecondNumber=int(SecondNumber)

#print(FirstNumber+SecondNumber)

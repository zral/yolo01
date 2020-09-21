from flask import Flask

app = Flask(__name__)

@app.route('/')
def hey():
    return "halloen"

@app.route('/celcius/<value>')
def calculateF(value):
    return value + " Celcius er " + str(float(value)*1.8 + 32) + " i Fahrenheit"

@app.route('/fahrenheit/<value>')
def calculateC(value):
    return value + " Fahrenheit er " + str((float(value)/1.8) - 32) + " i Celcius"
    
if __name__ == "__main__":
    app.run(debug=True)
    

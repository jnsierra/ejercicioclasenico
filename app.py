from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola Mundo Primer Microservicio 002', 200

@app.route('/startup', methods=['GET'])
def startup():
    return 'Startup OK', 200

@app.route('/readiness', methods=['GET'])
def readiness():
    return 'Readiness OK', 200

@app.route('/health', methods=['GET'])
def health():
    return 'Health OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from my CI/CD pipeline! v2.0 - Release approved by EM"

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

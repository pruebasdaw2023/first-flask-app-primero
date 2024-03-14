from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hola mundo desde Flask en 2024 que tal?</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
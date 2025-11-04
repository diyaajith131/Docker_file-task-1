# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_from_docker():
    return 'Hello from Docker!'

if __name__ == '__main__':
    # Flask runs on port 5000 by default, setting host='0.0.0.0'
    # makes the app accessible outside the container's localhost.
    app.run(debug=True, host='0.0.0.0', port=5000)

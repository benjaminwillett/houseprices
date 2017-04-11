from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Medium House Price Cheltenham!'


if __name__ == '__main__':
    app.run()

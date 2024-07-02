from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is my first website opening"


if __name__ == "__main__':
    app.run(debug=true, port=8000)

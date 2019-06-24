from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "flask working now..."

def main():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()

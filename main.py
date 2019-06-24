from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_folder="statics")

@app.route("/")
def index():
    return "flask working now..."

@app.route("/desk")
def desk():
    return render_template("desk.html")

def main():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()

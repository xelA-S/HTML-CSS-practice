from flask import Flask,render_template,url_for

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", methods = ["GET"])

@app.route("/earth", methods = ["GET"])
def earth():
    return render_template("earth.html")

@app.route("/mars", methods = ["GET"])
def mars():
    return render_template("mars.html")

if __name__ == "__main__":
    app.run(debug=True)
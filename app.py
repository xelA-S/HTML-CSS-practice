from flask import Flask,render_template,url_for

app=Flask(__name__)


@app.route("/",  methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/earth", methods = ["GET"])
def earth():
    return render_template("earth.html")

@app.route("/mars", methods = ["GET"])
def mars():
    return render_template("mars.html")

@app.route("/dinosaurs", methods = ["GET"])
def dinosaur():
    return render_template("dinosaur.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == "POST":
        keyword = "Covid-19"
        pattern = "Boyers-Moore"
        return render_template("result.html", keyword=keyword, pattern=pattern)
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
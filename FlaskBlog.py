from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)

posts = [
    {
        'author': 'Michael Hans',
        'title': 'Sthyrelest Extractor Application',
        'content': 'Dasar-Dasar Pemrograman',
        'date_posted': 'April 21, 2020'
    }
]

@app.route("/", methods=["POST","GET"])
@app.route("/home", methods=["POST","GET"])
def home():
    if request.method == "POST":
        keyword = request.form['keyword']
        pattern = request.form['matchmethod']
        files = request.form.getlist('myfile')
        return redirect(url_for("result", kyw = keyword, ptr = pattern, fls = files))
    return render_template('home.html', posts=posts)

@app.route("/result")
def result():
    return render_template("result.html", keyword=request.args.get('kyw'), pattern=request.args.get('ptr')
    ,files = request.args.getlist('fls'), posts = posts)
    

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
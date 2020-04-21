# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Menu Program Utama : Application
# Terintegrasi dengan HTML dan Python dengan Flask Framework
# Created by: 13518056 / Michael Hans

from flask import Flask, redirect, render_template, url_for, request
from ExtractorApp import *

# Generate HTML Based on Flask
app = Flask(__name__)

# Halaman Web Bagian Home / Menu Awal
@app.route("/", methods=["POST","GET"])
@app.route("/home", methods=["POST","GET"])
def home():
    if request.method == "POST":
        keyword = request.form['keyword']
        method = request.form['matchmethod']
        files = request.form.getlist('myfile')
        return redirect(url_for("result", kyw = keyword, ptr = method, fls = files))
    return render_template('home.html')

# Halaman Web Bagian Hasil Ekstraksi
@app.route("/result")
def result():
    keyword = request.args.get('kyw')
    pattern = request.args.get('ptr')
    files = request.args.getlist('fls')
    result = BeginExtraction(keyword, pattern, files)
    return render_template("result.html", keyword = keyword, pattern = pattern ,files = files, result = result)
    
# Halaman Web Bagian Guide Line / How To Use
@app.route("/guideline")
def guideline():
    return render_template('guideline.html', title='About')

# Menjalankan Aplikasi
if __name__ == '__main__':
    app.run(debug=True)
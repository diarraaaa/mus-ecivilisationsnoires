from flask import Flask, render_template,session
from python import app

@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/niveaupage')
def pageniveau():
    return render_template("niveau.html")
if __name__ == '__main__':
    app.run(debug=True)

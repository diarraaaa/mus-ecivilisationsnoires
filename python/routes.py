from flask import Flask, render_template,session
from python import app

@app.route('/')
def index():
    return render_template('accueil.html')


if __name__ == '__main__':
    app.run(debug=True)

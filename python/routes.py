from flask import Flask, render_template,session
from python import app
from python.Fonctions import detailsparniveaucode, detailsparoeuvrecode

@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/niveaupage')
def pageniveau():
    return render_template("niveau.html")
@app.route('/detailsparpiece', methods=['POST'])
def detailsparpiece():
    return detailsparniveaucode()
@app.route('/detailsparoeuvre', methods=['POST'])
def detailsparoeuvre():
    return detailsparoeuvrecode()
if __name__ == '__main__':
    
    app.run(debug=True)

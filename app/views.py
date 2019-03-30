from flask import render_template, request
from app import app

@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    # NOte: moved below logic to the template, so the view controller here is cleaner.
    #if not name:
    #    name = '<unknown>'
    return render_template('homepage.html', name=name, number=number)

from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import *
from modules import slides

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def index():
   form = PresentationList()

   if request.method == 'POST':
       if form.validate() == False:
           flash('All fields are required.')
           return render_template('index.html', form = form)
       else:
           session["sliden"] = form.presentation.data
           return redirect(url_for('presentation'))
   elif request.method == 'GET':
       return render_template('index.html', form = form)

@app.route('/presentation', methods = ['GET', 'POST'])
def presentation():
    idn = session['sliden']
    title, filen, description, style = slides.showslide(idn)
    return render_template('presentation.html', filen = filen, title = title, description = description, style = style)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='8080')

from flask import redirect, url_for
from flask import Flask, render_template, request, make_response


app = Flask(__name__)


@app.route('/')
def index():
   name = request.cookies.get('userID')
   if name is not None:
   		return redirect(url_for('getcookie'))
   else:
   		return render_template('index.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   		user = request.form['nm']

   		resp = make_response(render_template('readcookie.html'))
   		resp.set_cookie('userID', user)
   
   return resp


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')

   return render_template('welcomepage.html', name=name)


@app.route('/removecookie', methods = ['POST', 'GET'])
def removecookie():
   if request.method == 'POST':
   	   user = request.form['nm']

   resp = make_response(render_template('index.html'))
   resp.delete_cookie('userID')

   return resp


app.run('0.0.0.0')
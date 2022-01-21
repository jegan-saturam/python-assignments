from flask import Flask, request, redirect, url_for, render_template
from sqlalchemy import create_engine
import re

app = Flask(__name__)

@app.route('/success/<username>')
def success(username):
	return 'Welcome %s !!  You Logged in successfully' % username
@app.route('/failed/<message>')
def failed(message):
	return '%s' % message
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username == '' or password == '':
			message = 'Please fill out the form !'
			return redirect(url_for('failed',message = message))	
		else:
			engine = create_engine("postgresql://postgres:Jeganchaela1011@localhost:5432/accounts")
			result = engine.execute('SELECT * FROM accounts WHERE username = %s', username)
			print(result)
			account = result.fetchone()
			print(account)
			if account != None:
				return redirect(url_for('success',username = username))
			else:
				message = 'Username doesnot exist !'
				return redirect(url_for('failed',message = message))
@app.route('/registration', methods=['GET','POST'])
def registration():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		if username == '' or password == '' or email == '':
			message = 'Please fill out the form !'
			return redirect(url_for('failed',message = message))
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			message = 'Invalid email address !'
			return redirect(url_for('failed',message = message))
		elif not re.match(r'[A-Za-z0-9]+', username):
			message = 'Username must contain only characters and numbers !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://postgres:Jeganchaela1011@localhost:5432/accounts")
			result = engine.execute('SELECT * FROM accounts WHERE username = %s', username)
			print(result)
			account = result.fetchone()
			print(account)
			if account == None:
				engine.execute('INSERT INTO accounts VALUES ( %s, %s, %s)', (username, password, email))
				return redirect(url_for('success',username = username))
			else:
				message = 'Account already exist !'
				return redirect(url_for('failed',message = message))

if __name__ == "__main__":
    app.run(debug = True)
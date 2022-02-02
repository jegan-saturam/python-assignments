from flask import Flask, request, redirect, url_for
import sqlalchemy
from sqlalchemy import create_engine
import re

app = Flask(__name__)


@app.route('/success/<username>')
def success(username):
	return 'Congrats %s !! Your credentials is updated' % username
@app.route('/failed/<message>')
def failed(message):
	return '%s' % message
@app.route('/update', methods=['PUT','DELETE'])
def update():
	if request.method == 'PUT':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print(username)
		if username == '' or password == '' or email == '':
			message = 'Please fill to update !'
			return redirect(url_for('failed',message = message))
		elif not re.fullmatch(r'[A-Za-z0-9]+', username):
			message = 'Username must contain only characters and numbers !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
			result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
			print(result)
			account = result.fetchone()
			print(account)
			if account == None:
				message = 'Username doesnot exist for updation !'
				return redirect(url_for('failed',message = message))
			else:
				try:
					engine.execute('UPDATE accounts SET password = %s WHERE email = %s', password, email)
					engine.execute('UPDATE accounts SET username = %s WHERE email = %s', username, email)
				except sqlalchemy.exc.IntegrityError:
					message = 'Enter the proper username and password to update'
					return redirect(url_for('failed',message = message))
				else:
					return redirect(url_for('success',username = username))
@app.route('/delete', methods=['PUT','DELETE'])
def delete():
	if request.method == 'DELETE':
		username = request.form['email']
		if email == '':
			message = 'Please fill to update !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
			result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
			print(result)
			account = result.fetchone()
			print(account)
			if account == None:
				message = 'account doesnot exist for deletion !'
				return redirect(url_for('failed',message = message))
			else:
				engine.execute('DELETE FROM accounts WHERE email = %s', email)
				message = 'Account deleted successfully!'
				return redirect(url_for('failed',message = message))
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username == '' or password == '':
			message = 'Please fill out the form !'
			return redirect(url_for('failed',message = message))	
		else:
			engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
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
		elif not re.fullmatch(r'[A-Za-z0-9]+', username):
			message = 'Username must contain only characters and numbers !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
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

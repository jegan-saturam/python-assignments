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
		username = request.args.get('username')
		password = request.args.get('password')
		email = request.args.get('email')
		print(username)
		if username == '' or password == '' or email == '':
			message = 'Please fill to update !'
			return redirect(url_for('failed',message = message))
		elif not re.fullmatch(r'[A-Za-z0-9]+', username):
			message = 'Username must contain only characters and numbers !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://postgres:Jeganchaela1011@localhost:5432/accounts")
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
		email = request.args.get('email')
		if email == '':
			message = 'Please fill to update !'
			return redirect(url_for('failed',message = message))
		else:
			engine = create_engine("postgresql://postgres:Jeganchaela1011@localhost:5432/accounts")
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


if __name__ == "__main__":
	app.run(debug = True)
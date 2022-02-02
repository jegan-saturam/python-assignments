from flask import Flask, request, redirect, url_for, render_template
import sqlalchemy
from sqlalchemy import create_engine
import re

app=Flask(__name__,template_folder='Template')


@app.route('/update', methods=['POST','DELETE'])
def update():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print(username)
		if username == '' or password == '' or email == '':
			result = 'Please fill to update !'
			render_template("jsajaxpy1.html", result=result)
		elif not re.fullmatch(r'[A-Za-z0-9]+', username):
			result = 'Username must contain only characters and numbers !'
			render_template("jsajaxpy1.html", result=result)
		else:
			engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
			result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
			print(result)
			account = result.fetchone()
			print(account)
			if account == None:
				result = 'Username doesnot exist for updation !'
				render_template("jsajaxpy1.html", result=result)
			else:
				try:
					engine.execute('UPDATE accounts SET password = %s WHERE email = %s', password, email)
					engine.execute('UPDATE accounts SET username = %s WHERE email = %s', username, email)
				except sqlalchemy.exc.IntegrityError:
					result = 'Enter the proper username and password to update'
					render_template("jsajaxpy1.html", result=result)
				else:
					result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
					render_template("jsajaxpy1.html", result=result)
					
					
if __name__ == "__main__":
	app.run(debug = True)

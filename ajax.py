from flask import Flask, request, jsonify
import json
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def updation():
	print("Updation Starts")
	rf=request.form
	print(rf)
	for key in rf.keys():
		data=key
	print(data)
	data_dic=json.loads(data)
	print(data_dic.keys())
	update_data = data_dic['updation']
	print(update_data)
	username=update_data[0]
	password=update_data[1]
	email=update_data[2]
	print(username)
	print(password)
	print(email)
	engine = create_engine("postgresql://myuser:mypass@localhost:5432/mydatabase")
	result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
	account = result.fetchone()
	if account == None:
		resp_dic={'result':'NA','msg':'Username doesnot exist for updation !'}
		resp = jsonify(resp_dic)
		resp.headers['Access-Control-Allow-Origin']='*'
		return resp
	else:
		try:
			engine.execute('UPDATE accounts SET password = %s WHERE email = %s', password, email)
			engine.execute('UPDATE accounts SET username = %s WHERE email = %s', username, email)
		except sqlalchemy.exc.IntegrityError:
			resp_dic={'result':'NA','msg':'Enter the proper username and password'}
			resp = jsonify(resp_dic)
			resp.headers['Access-Control-Allow-Origin']='*'
			return resp
			
		else:
			result = engine.execute('SELECT * FROM accounts WHERE email = %s', email)
			resp_dic={'result':'Updated','msg':'Updation Success'}
			resp = jsonify(resp_dic)
			resp.headers['Access-Control-Allow-Origin']='*'
			return resp
					
if __name__ == "__main__":
	app.run(debug = True)

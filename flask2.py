from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/success1/<int:number3>')
def success1(number3):
	return 'addition of numbers %d' % number3
@app.route('/addition', methods=['GET','POST'])
def addition():
	if request.method == 'GET':
		try:
			number1 = int(request.args.get('num1'))
			number2 = int(request.args.get('num2'))
		except ValueError:
			return 'Enter the Valid Input'
		else:		
			number3 = number1 + number2
			return redirect(url_for('success1',number3 = number3))
	
if __name__ == "__main__":
    app.run(debug = True)
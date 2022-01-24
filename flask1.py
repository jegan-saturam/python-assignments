from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/success/<int:number3>')
def success(number3):
	return 'addition of numbers %d' % number3
@app.route('/add', methods=['GET','POST'])
def add():
	if request.method == 'POST':
		number1 = int(request.form['num1'])
		number2 = int(request.form['num2'])
		number3 = number1 + number2
		return redirect(url_for('success',number3 = number3))
	else:
		number1 = int(request.args.get('num1'))
		number2 = int(request.args.get('num2'))
		number3 = number1 + number2
		return redirect(url_for('success',number3 = number3))

if __name__ == "__main__":
    app.run(debug = True)
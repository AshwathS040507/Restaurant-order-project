from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/order')
def order():
	return render_template('order.html')

@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/pay')
def pay():
	total = 14
	return render_template('pay.html', total=total)
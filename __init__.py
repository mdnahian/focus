from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


@app.route('/settings')
def settings():
	return render_template('settings.html')



@app.route('/api/mode', methods=['POST'])
def api_mode():
	if request.method == 'POST':
		modes = request.form['modes']
		with open('modes.txt', 'w') as modes_file:
			modes_file.write(modes)
		return True
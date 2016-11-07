from flask import Flask, render_template
from recipes import app
import json

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results')
def results():
	return render_template('results.html')

if __name__ == '__main__':
	app.run()

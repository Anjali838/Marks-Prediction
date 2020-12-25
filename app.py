from flask import Flask, render_template, redirect, request

import joblib

# __name__==__main__
app=Flask(__name__)
# __name__ is the module name

model = joblib.load("model.pkl")

# @ - decorator in Python
# Routes are used so that user can go to different url's or handling the different url's
@app.route('/')
def Hello():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':
		hours = float(request.form['hours'])

		marks = str(model.predict([[hours]])[0][0 ])

	return render_template("index.html",your_marks=marks)

# by default method is always GET so we don't need to explicitly write

# Using Ginger Template(of python) we can write python code in html code

if __name__=='__main__':
	app.debug=True
	app.run()



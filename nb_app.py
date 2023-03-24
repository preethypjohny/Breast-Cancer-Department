from flask import Flask, request, render_template
from markupsafe import escape
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/graphs')
def graphs():
    return render_template("graphs.html")


@app.route('/prediction')
def prediction():
        return render_template("prediction.html")

@app.route('/forecast')
def forecast():
        return render_template("forecast.html")


if __name__== "__main__":
    app.run(debug = True)
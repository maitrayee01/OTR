import os 
from flask import Flask, request, render_template, redirect, url_for, send_file
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

if __name__ == "__main__":
	app.run()
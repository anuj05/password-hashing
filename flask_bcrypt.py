from flask import Flask, render_template, request, redirect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash_password', methods=['POST'])
def hash_password():
    password = request.form['password']
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
     # Store hashed_password in the database
    return redirect('/')

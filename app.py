from flask import Flask, request, render_template,  redirect, url_for, session, flash
import pandas as pd
import numpy as np
import pickle
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Load the model
with open('xgboost.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

users = {}
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash("USername already exists")
            return redirect(url_for('register'))
        users[username] = generate_password_hash(password)
        flash('Registration successful! Please log in..........')
        return redirect(url_for('login'))
    return render_template('register.html')
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user_hash = users.get(username)
        if user_hash and check_password_hash(user_hash, password):
            session["username"] = username
            flash("Login Succsessfully!.......")
            return redirect('index')
        flash("Invalid username or password.....")
    return render_template("login.html")


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        # Extract form data
        baseline_value = float(request.form['baseline_value'])
        accelerations = float(request.form['accelerations'])
        fetal_movement = float(request.form['fetal_movement'])
        uterine_contractions = float(request.form['uterine_contractions'])
        light_decelerations = float(request.form['light_decelerations'])
        severe_decelerations = float(request.form['severe_decelerations'])
        prolongued_decelerations = float(request.form['prolongued_decelerations'])
        abnormal_short_term_variability = float(request.form['abnormal_short_term_variability'])
        mean_value_of_short_term_variability = float(request.form['mean_value_of_short_term_variability'])
        percentage_of_time_with_abnormal_long_term_variability = float(request.form['percentage_of_time_with_abnormal_long_term_variability'])
        mean_value_of_long_term_variability = float(request.form['mean_value_of_long_term_variability'])
        histogram_width = float(request.form['histogram_width'])
        histogram_min = float(request.form['histogram_min'])
        histogram_max = float(request.form['histogram_max'])
        histogram_number_of_peaks = float(request.form['histogram_number_of_peaks'])
        histogram_number_of_zeroes = float(request.form['histogram_number_of_zeroes'])
        histogram_mode = float(request.form['histogram_mode'])
        histogram_mean = float(request.form['histogram_mean'])
        histogram_median = float(request.form['histogram_median'])
        histogram_variance = float(request.form['histogram_variance'])
        histogram_tendency = float(request.form['histogram_tendency'])
        
        # Create DataFrame for prediction
        new_data = pd.DataFrame({
            'baseline_value': [baseline_value],
            'accelerations': [accelerations],
            'fetal_movement': [fetal_movement],
            'uterine_contractions': [uterine_contractions],
            'light_decelerations': [light_decelerations],
            'severe_decelerations': [severe_decelerations],
            'prolongued_decelerations': [prolongued_decelerations],
            'abnormal_short_term_variability': [abnormal_short_term_variability],
            'mean_value_of_short_term_variability': [mean_value_of_short_term_variability],
            'percentage_of_time_with_abnormal_long_term_variability': [percentage_of_time_with_abnormal_long_term_variability],
            'mean_value_of_long_term_variability': [mean_value_of_long_term_variability],
            'histogram_width': [histogram_width],
            'histogram_min': [histogram_min],
            'histogram_max': [histogram_max],
            'histogram_number_of_peaks': [histogram_number_of_peaks],
            'histogram_number_of_zeroes': [histogram_number_of_zeroes],
            'histogram_mode': [histogram_mode],
            'histogram_mean': [histogram_mean],
            'histogram_median': [histogram_median],
            'histogram_variance': [histogram_variance],
            'histogram_tendency': [histogram_tendency]
        })

        # Convert DataFrame to numpy array
        new_data = new_data.values

        # Make prediction
        prediction = loaded_model.predict(new_data)
        
        # Determine result based on predicted class
        if prediction == 1:
            result = "Normal"
        elif prediction == 2:
            result = "Suspect"
        else:
            result = "Pathological"

        return render_template('result.html', prediction = result )
    return render_template("index.html")

@app.route('/performance')
def performance():
    return render_template('performance.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')
    
@app.route('/logout')
def logout():
    return render_template('home.html')
   

if __name__ == '__main__':
    app.run()

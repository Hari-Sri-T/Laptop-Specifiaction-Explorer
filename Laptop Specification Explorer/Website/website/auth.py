from .models import mysql
from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint('auth', __name__)

# Hardcoded credentials
HARD_CODED_USERNAME = "User"    ##change it to whatever you like
HARD_CODED_PASSWORD = "123456"

# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')


        # Check if the username and password match the hardcoded values
        if username == HARD_CODED_USERNAME and password == HARD_CODED_PASSWORD:
            session['user_id'] = username  # Store username in session (or use a user ID if you have one)
            return redirect(url_for('views.home'))  # Redirect to the home page
        else:
            flash('Invalid credentials, please try again.')  # Use flash to show error message
            return redirect(url_for('auth.login'))  # Redirect back to the login page

    return render_template('login.html')  # Render the login page
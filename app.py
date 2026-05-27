from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Add Event Page
@app.route('/add_event')
def add_event():
    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True)
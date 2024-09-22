# app.py
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    # Variable to pass to the HTML template
    name = "enter your name here!"
    # Render the HTML page and pass the 'name' variable to it
    return render_template('index.html', name=name)

# Ensure the app runs in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)

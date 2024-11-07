# Import the Flask library
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "<h1>Welcome to My Website</h1><p>This is a basic Flask app!</p>"

# Define an about route
@app.route('/about')
def about():
    return "<h1>About Us</h1><p>This is the about page.</p>"

# Define a contact route
@app.route('/contact')
def contact():
    return "<h1>Contact</h1><p>Contact us at contact@mywebsite.com</p>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
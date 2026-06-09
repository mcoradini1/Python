"""
FLASK — Third-Party Library

Flask is a lightweight web framework used 5.1 - For:
- small web apps
- APIs
- prototypes

This example shows:
- creating a simple web server
- defining a route
"""

from flask import Flask

app = Flask(__name__)

# ---------------------------------------------------------
# BASIC ROUTE
# ---------------------------------------------------------

@app.route("/")
def home():
    return "Hello from Flask!"

# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template
app = Flask(__name__)

# Basic app output
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

# about page
@app.route("/about")
def about():
    return ""

if __name__ == "__main__":
    app.run()
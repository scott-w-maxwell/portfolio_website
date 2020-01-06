from flask import Flask, render_template
app = Flask(__name__)

# Basic app output
@app.route("/")
@app.route("/home")
def hello():
    return "<h1>This is my portfolio home page<h1>"

# about page
@app.route("/about")
def about():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
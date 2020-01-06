from flask import Flask
app = Flask(__name__)

# Basic app output
@app.route("/")
@app.route("/home")
def hello():
    return "<h1>This is my portfolio home page<h1>"

# about page
@app.route("/about")
def about():
    return "<h1>This is the about page<h1>"

if __name__ == "__main__":
    app.run()
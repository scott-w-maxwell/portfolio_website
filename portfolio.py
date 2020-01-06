from flask import Flask
app = Flask(__name__)

# Basic app output
@app.route("/")
def hello():
    return "<h1>This is my portfolio<h1>"

if __name__ == "__main__":
    app.run()
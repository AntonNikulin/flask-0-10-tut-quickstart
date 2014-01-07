from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/")
def index():
    return "Index Page"

@app.route("/user/<username>")
def showUserProfile(username):
    return "User %s" % username

@app.route("/meth", methods=["GET"])
def meth():
    return "Hi with GET!"

if __name__ == "__main__":
    app.run(debug=True)


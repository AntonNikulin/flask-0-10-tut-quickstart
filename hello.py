from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/")
def index():
    css = url_for("static", filename="style.css")
    return '<link rel="stylesheet" type="text/css" href="{0}">' \
           ' <p>Index Page</p>'.format(css)

@app.route("/user/<username>")
def showUserProfile(username):
    return "User %s" % username

@app.route("/meth", methods=["GET"])
def meth():
    return "Hi with GET!"

if __name__ == "__main__":
    app.run(debug=True)


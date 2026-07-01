import git
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)  #Flask
app.config['SECRET_KEY'] = '7c3d31e61005a9cc01a79df320cb8038'

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Home",
        subtitle="Welcome to Bean & Brew Café",
        text="Fresh coffee, homemade pastries, and friendly service."
    )


@app.route("/menu")
def menu():
    return render_template(
        "menu.html",
        title="Menu"
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About"
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact"
    )

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/hectorb/cafe_project')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
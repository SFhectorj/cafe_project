from flask import Flask, render_template
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
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


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
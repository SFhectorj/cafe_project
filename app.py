import git
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '7c3d31e61005a9cc01a79df320cb8038'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash("User created successfully!", "success")
        return redirect("/")

    return render_template("register.html")

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/hectorb/cafe_project')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
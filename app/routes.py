from flask import flash, redirect, render_template
from app import app
from app.forms import LoginForm


user = {
    "username": "Abdurrasheed"
}

posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", user=user, title="Home", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data,form.remember_me.data))
        return redirect("/index")
    return render_template("login.html", form=form, title="Sign In")
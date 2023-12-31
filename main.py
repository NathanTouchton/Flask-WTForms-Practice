from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "xH%o%8TZmfZ!bs7dWz"
bootstrap = Bootstrap5(app)

class MyForm(FlaskForm):
    username = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Submit")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.username.data == "admin@email.com" and form.password.data == "12345678":
                return redirect('/success')
            return redirect("/denied")
    return render_template('login.html', form=form, bootstrap=bootstrap)

@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template("success.html")

@app.route("/denied", methods=["GET", "POST"])
def denied():
    return render_template("denied.html")

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "xH%o%8TZmfZ!bs7dWz"

class MyForm(FlaskForm):
    username = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # return render_template("login.html")
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)

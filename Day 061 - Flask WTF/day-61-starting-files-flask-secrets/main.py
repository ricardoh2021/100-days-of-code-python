from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "dev-secret"  # needed for CSRF



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=8)])
    remember_me = BooleanField("Remember Me")
    role = SelectField("Role", choices=[("admin", "Admin"), ("student", "Student"), ("guest", "Guest")])
    bio = TextAreaField("Short Bio", validators=[Length(max=150)])
    submit = SubmitField("Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.email.data, form.password.data
        valid_credentials = {"email": "admin@email.com", "password": "12345678"}

        if email == valid_credentials["email"] and password == valid_credentials["password"]:
            return render_template("success.html")

        print("Invalid login attempt")
        return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))
main_flask = Flask(__name__)
main_flask.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
main_flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://C:/Users/raziuddin.khazi/Documents/DataCamp_2022/UI_Datacamp2database.db'
Bootstrap(main_flask)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


@main_flask.route('/')
def index():
    #index_path = "./templates/index.html"
    return render_template('index.html')


@main_flask.route('/login', methods=['GET', 'POST'])
def login():
    #login_path = "./templates/login.html"
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == "__main__":
    main_flask.run(debug=True)


from os import path, environ

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from pymongo import MongoClient
from configparser import ConfigParser

basedir = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
app.config['WTF_CSRF_SECRET_KEY'] = '8702d997ad5988fbf2d6b950aa1167528191a356573a92847b9cdc533a511e03'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'lupify.db')
#db = SQLAlchemy(app)

# mongoClient = MongoClient('127.0.0.1', 27017)

try:
    mongodb_uri = environ['LUPIFY_MONGODB_URI']
    mongodb_user = environ['LUPIFY_MONGODB_USER']
    mongodb_pass = environ['LUPIFY_MONGODB_PASS']

    mongoClient = MongoClient(mongodb_uri, 27017)
    db = mongoClient.lupify
    db.authenticate(mongodb_user, mongodb_pass)
except:
    print("Failed to connect to MongoDB")

try:
    app.config['LDAP_HOST'] = environ['LDAP_HOST']
    app.config['LDAP_BIND_USER'] = environ['LDAP_BIND_USER']
    app.config['LDAP_BIND_PASS'] = environ['LDAP_BIND_PASS']
    app.config['LDAP_BASE_DN'] = environ['LDAP_BASE_DN']
    app.config['LDAP_GROUP_DN'] = environ['LDAP_GROUP_DN']
except:
    print('Failed to retreive LDAP configuration')

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

import lupify.models
import lupify.views
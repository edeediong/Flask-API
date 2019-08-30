from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

basedir = os.path.abspath(os.path.dirname(__file__))
targetdir = os.path.join(basedir, 'database.db')
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + targetdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

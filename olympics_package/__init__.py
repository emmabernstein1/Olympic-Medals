from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
# from olympics_package.models import *

import dash
import dash_core_components as dcc
import dash_html_components as html


server = Flask(__name__)


server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olympics.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# server.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname = '/')

# some_engine = create_engine('postgresql://scott:tiger@localhost/')

# create a configured "Session" class
engine = create_engine('sqlite:///olympics.db', echo=True)
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# from olympics_package import routes
# from spotify_package.seed import *
from olympics_package.dashboard import *
app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

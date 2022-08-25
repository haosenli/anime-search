# for custom imports
import sys # for import from parent directory
import os # for import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from flask import Flask


# start flask app
app = Flask(__name__)

# get website routes
from flask_app import routes


# for custom imports
import sys # for import from parent directory
import os # for import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from flask_app import app

# run
print('Flask app is online.')
app.run()

from flask import render_template, jsonify, json
# from olympics_package.models import *
# from olympics_package import *
from olympics_package.dashboard import app

@app.server.route('/olympics')
def olympic_findings():
    return render_template('olympics.html')

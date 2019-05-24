#!/usr/bin/python3
"""Start Flask web app for our TripleTail
website"""

from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from user import User

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '127.0.0.1'

# Cross-Origin Resource sharing
cors = CORS(app, resouces={r"/*": {"origins": "*"}})

def page_not_found(e):
    """404 error page for nonexistent routes"""
    return jsonify({'error': "Not found"}), 404

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Landing page
    """
    return render_template('index.html')

@app.route('/<username>/tier/')
def tier_page(username):
    """
    Returns a page containing the Tier of the
    Github user
    """
    userinfo = User(username)
    return render_template('ranking.html',
                           userinfo=userinfo)

@app.route('/testing')
def test():
    userinfo = {'tier': 'tier1'}
    return render_template('ranking.html', userinfo=userinfo)

@app.route('/<username>/stats')
def followers():
    pass


if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host)

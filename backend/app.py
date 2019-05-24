#!/usr/bin/python3
"""Start Flask web app for our TripleTail
website"""

from flask import Flask, jsonify, request
from user import User

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '35.245.121.190'

def page_not_found(e):
    """404 error page for nonexistent routes"""
    return jsonify({'error': "Not found"}), 404

@app.route('/')
def homepage():
    """
    Landing page
    """
    return render_template('index.html')

@app.route('/tier/', methods=['POST'])
def tier_page(debug=True):
    """
    Takes a POST request with the
    Oauth2 token of the new user and
    returns a page containing the Tier
    and stats of the Github user
    """
    oauth_token = request.data
    if oauth_token is None:
        return render_template('index.html')
    else:
        user_info = User(oauth_token)
        return render_template('ranking.html',
                               token=oauth_token,
                               user_info=user_info.to_dict())

@app.route('/<username>/stats')
def followers


if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host)

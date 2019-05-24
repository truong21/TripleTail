#!/usr/bin/python3
"""Start Flask web app for our TripleTail
website"""

from flask import Flask, jsonify, render_template

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '35.245.121.190'
host = '127.0.0.1'

def page_not_found(e):
    """404 error page for nonexistent routes"""
    return jsonify({'error': "Not found"}), 404

@app.route('/')
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
    userinfo = User(userinfo)
    return render_template('ranking.html',
                           userinfo=userinfo)

@app.route('/testing')
def test():
    return render_template('ranking.html')

if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host)

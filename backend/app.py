#!/usr/bin/python3
"""Start Flask web app for our TripleTail
website"""

from flask import Flask, jsonify

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
    # TODO - insert html file name and necessary variables
    return render_template(info)

if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host)

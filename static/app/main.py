"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)


#if __name__ == '__main__':
#    app.run(debug=True)
###
# Routing for your application.
###

@app.route('/')
def home(name=None):
    """Render website's home page."""
    return render_template('home.html',name=name)
    #return 'Hello tks final'
    

@app.route('/about/')
def about(name=None):
    """Render the website's about page."""
    return render_template('about.html',name=name)

@app.route('/profile/')
def profile(name=None):
    """Render the website's about page."""
    return render_template('profile.html',name=name)

  
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

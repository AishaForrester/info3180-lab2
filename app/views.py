from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

@app.route("/profile")
def profile():
    #Using a desired date that we would like to be displayed in the profile.html when it is rendered
    dateJoined = datetime.date(2025, 1, 7) 

    #calling our previously created function to create a more visually appealing display of the given date
    formatDate = format_date_joined(dateJoined)

    #Sending over the date reference to the profile.html so it will be displayed when the html is rendered
    return render_template("profile.html", dateJoined = formatDate)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def format_date_joined(date):

    """our date will be converted into a string based on the given format Month, Year. This is more visually
    appealing to the user"""
    return date.strftime("%B, %Y")
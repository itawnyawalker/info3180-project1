"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os, locale
from app import app
from flask import render_template, request, redirect, send_from_directory, url_for, flash, safe_join
from werkzeug.utils import secure_filename

from app.forms import PropertyForm
from app.models import Property
from . import db

locale.setlocale(locale.LC_ALL,'en_CA.UTF-8')


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
    return render_template('about.html', name="Itawnya Walker")

@app.route('/properties/create', methods=['POST', 'GET'])
def add_property():
    """Renders page which displays for to add new property """
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            num_bed = form.num_bed.data
            num_bath = form.num_bath.data
            location = form.location.data
            price = form.price.data
            ptype = form.type.data
            desc = form.desc.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            print(filename)
            photo.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))

            new = Property(title=title, num_bedrooms=num_bed, num_bathrooms=num_bath, location=location, price=price, ptype=ptype, description=desc, photo=filename)

            db.session.add(new)
            db.session.commit()

            flash('Property Added', 'success')
            return redirect(url_for('properties'))
    return render_template('newproperty.html', form=form )


@app.route('/properties', methods=['POST', 'GET'])
def properties():
    """Renders list of all properties in the database"""
    if request.method == 'GET':
        return render_template('properties.html', properties=Property.query.all(),loc=locale)


@app.route('/properties/<propertyid>')
def get_property(propertyid):
    """Viewing an individual property by the specific property id """
    property = Property.query.filter_by(id=propertyid).first()
    
    if property is not None: 
        return render_template('property.html',  p=property, loc=locale)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

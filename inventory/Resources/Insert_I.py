from flask_restful import Resource
from flask import render_template, request, flash, redirect, url_for
from comman.utility import output_html, allowed_file, mypath, utc2cst
from Database.db_connector import connection_object
from werkzeug import secure_filename
import os
from Database.insert import insert
import logging
log = logging.getLogger(__name__)



class insert_inventory(Resource):
    def get(self):
        return output_html(render_template('insert_inventory.html'), 200)
    def post(self):
        data = request.form
        name = data['name']
        category = data['category']
        etime = data['etime']
        quantity = data['quantity']
        mtime = data['mtime']
        image = request.files['image']
        error = None
        if not name:
            error = "Please enter name of product"
        elif not category:
            error = "Please enter category"
        elif not etime:
            error = "Please enter etime"
        elif not quantity:
            error = "please enter quantity"
        elif not mtime:
            error = "please enter mtime"
        elif image.filename == '':
            error = 'please select image'
        elif image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_name = name + '-' + "image." + filename.rsplit('.', 1)[-1].lower()
            pname = os.path.join(mypath, image_name)
            sname = os.path.join('/static/image', image_name)
            image.save(pname)
        else:
            error = "Please enter valid format of image"
            log.warning("try to enter different format")

        if error is None:
            etime = utc2cst(etime)
            mtime = utc2cst(mtime)
            i_data = insert(name, category, etime, quantity, mtime, sname)
            log.debug("Data entered successfully")
            return output_html("Data Entered Successfully <p><a href='http://127.0.0.1:5000/search'>search</a></p>", 200)
        else:
            log.warning(error)
            flash(error)
            return redirect(url_for('insert_inventory'))




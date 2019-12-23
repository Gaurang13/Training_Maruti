from flask_restful import Resource
from flask import render_template, request, current_app, flash, redirect, url_for
from comman.utility import output_html, allowed_file, mypath
from Database.db_connector import connection_object
from werkzeug import secure_filename
import os
from Database.insert import insert
import datetime
from pytz import timezone
import pytz

import logging



def utc2cst(date_str):
    d1 = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
    cst_time = datetime.timedelta(hours=6, minutes=0)
    now_cst = d1-cst_time
    #now_cst = d1.astimezone(timezone(''))
    print(now_cst)
    print(type(now_cst))

    return now_cst

class insert_inventory(Resource):
    def get(self):
        return output_html(render_template('insert_inventory.html'), 200)
    def post(self):
        data = request.form
        name = data['name']
        category = data['category']
        etime = utc2cst(data['etime'])
        quantity = data['quantity']
        mtime = utc2cst(data['mtime'])
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
            image_name = name + '-' + secure_filename(image.filename)
            pname = os.path.join(mypath, image_name)
            sname = os.path.join('/static/image', image_name)
            image.save(pname)
        else:
            error = "Please enter valid format of image"

        if error is None:

            i_data = insert(name, category, etime, quantity, mtime, sname)
            return output_html("Data Entered Successfully <p><a href='http://127.0.0.1:5000/'>search</a></p>", 200)
        else:
            flash(error)
            return redirect(url_for('insert_inventory'))




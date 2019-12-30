from flask_restful import Resource
from flask import render_template, request, flash, redirect, url_for
from comman.utility import output_html, time2cst,save_file
from  comman.validation import insert_validation
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
        print(etime)
        error = None
        error = insert_validation(name,category,etime,quantity,mtime,image)
        if not etime:
            error = "Please enter etime"
        elif not mtime:
            error = "please enter mtime"


        if error is None:

            sname = save_file(image, name)

            etime = time2cst(etime)
            mtime = time2cst(mtime)

            insert(name, category, etime, quantity, mtime, sname)
            log.debug("Data entered successfully")
            return output_html("Data Entered Successfully <p><a href='http://127.0.0.1:5000/search'>search</a></p>", 200)
        else:
            log.warning(error)
            flash(error)
            return redirect(url_for('insert_inventory'))




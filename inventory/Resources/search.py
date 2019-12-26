from flask_restful import Resource
from flask import render_template, request, flash, redirect, url_for
from comman.utility import output_html,check_expire_time
from Database.search import search_item
import logging
log = logging.getLogger(__name__)


class item_search(Resource):

    def get(self):
        return output_html(render_template('search.html'), 200)

    def post(self):
        sname = request.form['s_name']
        scategory = request.form['s_category']
        time_zone = request.form['time_zone']
        error = None
        if time_zone=="":
            error = "Please enter time zone"
            log.info("not enterd time zone")
        if scategory and sname:
            error = "please enter any one"
            log.warning("try to search by both fields")
        if error is not None:
            flash(error)
            return output_html(render_template('search.html'), 201)

        else:

            data = search_item(s_name=sname, s_category=scategory)
            if data:
                log.info("data found successfully")
                for d in data:
                    expire_time = check_expire_time(time_zone, d['expire_time'])
                    if expire_time:
                        d['expire_time']="expired"
                return output_html(render_template('search.html', data=data), 200)

            else:

                error="Data Not available"
                log.warning("try to enter data that is not available")
                flash(error)
                return output_html(render_template('search.html'), 201)
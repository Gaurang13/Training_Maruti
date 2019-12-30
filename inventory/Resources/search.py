from flask_restful import Resource
from flask import render_template, request, flash, redirect, url_for, current_app
from comman.utility import output_html,check_expire_time
from comman.validation import search_valdation
from Database.search import search_item
import logging
import pytz
log = logging.getLogger(__name__)




class item_search(Resource):

    def get(self):
        return output_html(render_template('search.html',timezone_list=pytz.all_timezones), 200)

    def post(self):
        try:

            sname = ""
            scategory = ""
            if request.form.get('s_name'):
                sname = request.form['s_name']
            if request.form.get('s_category'):
                scategory = request.form['s_category']
            time_zone = request.form['time_zone']
            error = None
            error = search_valdation(sname,scategory,time_zone)
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

        except Exception as e:
            print(e)
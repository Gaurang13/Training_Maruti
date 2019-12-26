from flask_restful import Resource
from flask import render_template, request, current_app, flash, redirect, url_for
from comman.utility import output_html
from Database.update_item import update
import logging
log = logging.getLogger(__name__)


class update_item(Resource):
    def get(self):
        return output_html(render_template('update_item.html'), 200)

    def post(self):
        i_id = request.form['i_id']
        quantity = request.form['quantity']
        if i_id and quantity:
            data = update(i_id, quantity)
            if data:
                message = "Quantity Updated"
                log.info("Quantity Updated")
                return output_html(render_template('update_item.html', data=message), 200)

            else:
                error = "id not available"
                flash(error)
                log.warning("enterd id not available")
                return output_html(render_template('update_item.html'), 200)
        else:
            flash("please enter both the field")
            log.info("Not only one file")
            return output_html(render_template('update_item.html'),200)

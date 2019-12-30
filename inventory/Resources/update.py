from flask_restful import Resource
from flask import render_template, request, current_app, flash, redirect, url_for
from comman.utility import output_html
from comman.validation import update_validation
from Database.update import update
import logging
log = logging.getLogger(__name__)


class update_item(Resource):
    def get(self):
        return output_html(render_template('update.html'), 200)

    def post(self):
        i_id = request.form['i_id']
        quantity = request.form['quantity']
        error = None
        error = update_validation(i_id,quantity)
        if error is None:
            data = update(i_id, quantity)
            if data:
                message = "Quantity Updated"
                log.info("Quantity Updated")
                return output_html(render_template('update.html', data=message), 200)

            else:
                error = "id not available"
                flash(error)
                log.warning("enterd id not available")
                return output_html(render_template('update.html'), 200)
        else:
            flash(error)
            log.info(error)
            return output_html(render_template('update.html'),200)

from flask_restful import Resource
from flask import render_template, request, flash, redirect, url_for
from comman.utility import output_html
from comman.validation import delete_validation
from Database.delete import delete_object, get_id, get_image
import logging
import os
log = logging.getLogger(__name__)


class delete_item(Resource):
    def get(self):
        return output_html(render_template('delete.html'), 200)
    def post(self):

        i_ids = request.form['mdelete']
        error = None
        error = delete_validation(i_ids)

        if error is None:

            i_ids = i_ids.split(',')
            i_ids = [int(i) for i in i_ids]
            id_fetched = get_id()
            id_list = [i['inventory_id'] for i in id_fetched]
            not_id = list(set(i_ids)-set(id_list))

            if not_id:

                message = "Id Number" + " " +str(not_id) + " " + "Not Available"
                log.warning("try to delete not present id")
                flash(message)
                return redirect(url_for(('delete_item')))

            else:

                image_path = get_image(set(i_ids))
                dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

                for image_path_delete in image_path:

                    delete_item_path = image_path_delete['image']
                    str_temp = (dir_name, delete_item_path)
                    try:
                        os.remove("".join(str_temp))
                    except:
                        log.warning("image not found in directory")

                result = delete_object(i_ids)
                message = str(result) + " " + "row deleted"
                log.info(message)
                flash(message)
                return redirect(url_for('delete_item'))
        else:
                flash(error)
                return redirect(url_for('delete_item'))
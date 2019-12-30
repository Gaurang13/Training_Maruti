import re
from comman.utility import allowed_file

import logging
log = logging.getLogger(__name__)

def insert_validation(name,category,etime,quantity,mtime,image):

    if not re.match("\w+", name) or not name:
        error = "Error! Make sure you only use letters in your name or not blank"
        return error

    elif not re.match("\w+", category) or not category:
        error = "Error! Make sure you only use letters in your category or not blank"
        return error

    elif not etime or not re.match("^\d{4}\-\d{2}\-\d{2}[ ]\d{2}\:\d{2}$",etime):
        error = "Error! Make sure you entered expire date in yyyy-mm-dd H:M format or not blank"
        return error

    elif not re.match('["\d+"]',quantity) or not quantity:
        error = "Error! Make sure you only use digits in your quantity or not blank"
        return error
    elif not mtime or not re.match("^\d{4}\-\d{2}\-\d{2}[ ]\d{2}\:\d{2}$",mtime):
        error = "Error! Make sure you entered manufacturing date in yyyy-mm-dd H:M format"
        return error

    elif image.filename == "":
        error = 'please select image'
        return error

    elif not allowed_file(image.filename):
        error = "Please enter valid format of image"
        return error
        log.warning("try to enter different format")


def search_valdation(sname,scategory,timezone):
    import pytz

    if not sname and not scategory:
        error = "Please enter any one field"
        return error

    elif sname and scategory:
        error = "Please enter any one field"
        return error

    elif not re.match("\w+", sname) and sname != "":
        error = "Error! Make sure you can only use letters in your name"
        return error

    elif not re.match("\w+", scategory) and scategory != "":
        error = "Error! Make sure you can only use letters in your category"
        return error

    elif not timezone or timezone not in pytz.all_timezones:
        error = "Please selete timezone from the given menu"
        return error
        log.warning("Try to make error in timezone")


def update_validation(i_id,quantity):

    if not i_id or not quantity:
        error = "Please Enter Both the field"
        return error

    elif not re.match("\d",i_id):
        error = "Error! Make sure you can only use digits in Id field or not black"
        return error

    elif not re.match("\d",quantity):
        error = "Error! Make sure you can only use digits in Id field"
        return error



def delete_validation(i_ids):

    if not i_ids:
        error = "Please enter id"
        return error

    elif not re.match("(\d{1,},)*\d{1,}$",i_ids):
        error = "Please enter data in format like 1,2,3 or don't add comma at last"
        return error
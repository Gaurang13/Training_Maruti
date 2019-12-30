import os
from flask import Response, current_app
import datetime
import pytz


def output_html(data, code, headers=None):
    resp = Response(data, mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mypath = os.path.join(project_root, 'static/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.count(".") == 1 and \
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

def save_file(image,name):
    import os
    from werkzeug import secure_filename
    filename = secure_filename(image.filename)
    image_name = name + '-' + "image." + filename.rsplit('.', 1)[-1].lower()
    pname = os.path.join(mypath, image_name)
    sname = os.path.join('/static/image', image_name)
    image.save(pname)
    return sname


def time2cst(date_str):
    d1 = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")#convert string date time in specific date time format
    local_tz = pytz.timezone('Asia/Kolkata')
    date_temp = local_tz.localize(d1, is_dst=None) #navie time to aware time
    now_cst = date_temp.astimezone(pytz.timezone('CST6CDT'))#convert time to CST time


    return now_cst

def check_expire_time(given_timezone, ex_time):
    tz_NY = pytz.timezone(given_timezone)#take user specified time zone
    datetime_NY = datetime.datetime.now(tz_NY)#take current time of given time zone
    now_cst = datetime_NY.astimezone(pytz.timezone('CST6CDT'))#convert time to CST time

    local_tz = pytz.timezone('CST6CDT')
    ex_time = local_tz.localize(ex_time, is_dst=None)

    if now_cst > ex_time: #compare to aware time
        return True #if item expired
    else:
        return False #if item not expired

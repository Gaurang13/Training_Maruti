import re
date = "1,1,,,"
if re.match("(\d{1,},)*\d{1,}$",date):
    print("hello")
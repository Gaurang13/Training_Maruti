from app.database.db_connector import connection_object
import logging
from jproperties import Properties
import os

log = logging.getLogger(__name__)

sql = Properties()
sql_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"sql.properties")
with open(sql_file, "rb") as f:
    sql.load(f, "utf-8")
print(sql['SQL_SELECT_QUERY'])

# function that fatch whatsapp data from database
def fetch_whatsapp_data(id):
    import json
    connection = connection_object()
    try:
        with connection.cursor() as cursor:
            param = {
                'id': id
            }
            cursor.execute(sql['SQL_SELECT_QUERY'], param)
            wsdata = cursor.fetchall()
            return json.loads(wsdata)  # return the fetched whatsapp data

    except Exception as e:
        log.error(e)
        log.error("Error! Some thing went wrong  with fetch whatsapp data")

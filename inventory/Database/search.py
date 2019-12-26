import logging
from Database.db_connector import connection_object
import logging
log = logging.getLogger(__name__)


def search_item(**kwargs):
    connection = connection_object()
    try:
        with connection.cursor() as cursor:
            sql = "select * from inventory_data where Name = %s  or Category = %s"
            cursor.execute(sql, (kwargs.get('s_name'), kwargs.get('s_category')))
            item = cursor.fetchall()
            logging.info(item)
            connection.commit()
            return item
    except Exception as e:
        log.error(e)
        log.error("error in sql in search_item")

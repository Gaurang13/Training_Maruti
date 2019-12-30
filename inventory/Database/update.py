from Database.db_connector import connection_object
import logging
import logging
log = logging.getLogger(__name__)


def update(id, quantity):
    try:
        connection = connection_object()
        with connection.cursor() as cursor:
            sql = "update inventory_data set Quantity = %s where inventory_id = %s"
            data = cursor.execute(sql, (quantity, id))
            connection.commit()
            return data
    except Exception as e:
        log.info(e)
        log.info("error in sql in update")
from Database.db_connector import connection_object
import logging
log = logging.getLogger(__name__)

def delete_object(i_ids):
    try:
        connection = connection_object()
        with connection.cursor() as cursor:

            sql = "delete from inventory_data where inventory_id = %s"
            cursor.executemany(sql, i_ids)
            data = cursor.rowcount
            connection.commit()
            return data

    except Exception as e:
        log.error("Error in sql in i_delete")
        log.error(e)

def get_id():
    try:
        connection = connection_object()
        with connection.cursor() as cursor:
            sql = "select inventory_id from inventory_data"
            cursor.execute(sql)
            id_fetched = cursor.fetchall()
            connection.commit()
            return id_fetched
    except Exception as e:
        log.error("error in sql")

def get_image(i_ids):
    try:
        connection = connection_object()
        with connection.cursor() as cursor:
            sql = "select image from inventory_data where inventory_id in %s"
            cursor.execute(sql, i_ids)
            image_fetched = cursor.fetchall()
            return  image_fetched
            connection.commit()
    except Exception as e:
        print("error in sql")
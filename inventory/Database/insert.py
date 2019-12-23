import logging
from Database.db_connector import connection_object



def insert(name, category, etime, quantity, mtime, sname):
    try:
        connection = connection_object()
        with connection.cursor() as cursor:
            sql = 'insert into inventory_data(Name, Category, expire_time, Quantity, manufacturing_date, image) values(%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (name, category, etime, quantity, mtime, sname))
            logging.info(name)
            connection.commit()
            return "Done"
    except Exception as e:
        print(e)



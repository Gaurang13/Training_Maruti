import pymysql.cursors

connection = pymysql.connect(host="localhost",user="root",password="Mtech@12345",db="test",charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES ('webmaster@python.org', 'very-secret')"
        cursor.execute(sql)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT * from users"
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
finally:
    print("Great Job!");
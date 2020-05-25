import pymysql

username = 'root'

# Connect to database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close the connection
    connection.close()

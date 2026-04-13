import mysql.connector
from setting import mydomain

mydb=mysql.connector.connect(
    host=f'{mydomain.domain}',
    user=f'{mydomain.mysql_user}',
    passwd=f'{mydomain.mysql_passwd}',
    database=f'{mydomain.mysql_database}',
    charset='utf8mb4'
)
mycursor=mydb.cursor()
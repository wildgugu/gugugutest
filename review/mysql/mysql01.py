import mysql.connector
import mydomain

mydb = mysql.connector.connect(
    host=f"{mydomain.domain}",  # 数据库主机地址
    user=f"{mydomain.mysql_user}",  # 数据库用户名
    passwd=f"{mydomain.mysql_passwd}",  # 数据库密码
    database=f"{mydomain.mysql_database}",
    charset='utf8mb4'
)
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
all_tables = [table[0] for table in mycursor.fetchall()]
for table_name in all_tables:
    print(table_name)
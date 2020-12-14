# from redis import Redis
#
# conn=Redis(host='127.0.0.1')
# v=conn.keys()
# print(v)



#数据库练习

import pymysql

conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='mysql',db='mvc',charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select id,name from user_tb where name =%s and password=%s",['041640820','123'])
obj=cursor.fetchone()
conn.commit()
cursor.close()
conn.close()

print(obj)
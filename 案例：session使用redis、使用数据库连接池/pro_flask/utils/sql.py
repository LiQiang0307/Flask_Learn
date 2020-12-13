import pymysql
from flask import current_app
# from .pool import POOL


class SQLHelper(object):

    @staticmethod
    def open():
        POOL=current_app.config['PYMYSQL_POOL']
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql', db='mvc', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn=POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls, sql, args):
        # 连接数据库，查询
        conn, cursor = cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        cls.close(conn, cursor)
        return obj

    @classmethod
    def fetch_all(cls, sql, args):
        # 连接数据库，查询
        conn, cursor = cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchall()
        cls.close(conn, cursor)
        return obj

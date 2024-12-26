# -*- coding:utf-8 -*-
# @Time:2020/3/3 13:21
# @Author:whweia
# @File:MySQL_dome.py
import pymysql

# host='47.113.116.171',
# port=3306,
# user='root',
# password='root',
# db='recruit_students'


class MysqlManager(object):
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        "连接数据库"
        try:
            conn = pymysql.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        password=self.password,
                                        db=self.db)
            cursor = conn.cursor()
            return cursor
        except Exception as e:
            print(e)

    def get_data(self, sql):
        try:
            cursor = self.connect()
            cursor.execute(sql)
            return cursor.fetchone()
        except:
            print('数据库操作失败，请检查！')
        finally:
            cursor.close()

    def delete_data(self, param):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            sql = 'DELETE from t_school_info WHERE f_school_name = "%s"' % param
            print(sql)
            cursor.execute(sql)
            result = conn.commit()
            return result
        except:
            print("操作失败，请检查！")
        # finally:
        #     cursor.close()
        #     conn.close()


if __name__ == "__main__":
    host='192.168.1.15',
    port=3306,
    user='root',
    password='',
    db='student'
    mc = MysqlManager(host, port, user, password, db)
    r = mc.delete_data("573097")
    print(r)
    # r = mc.delete_data(6389048)

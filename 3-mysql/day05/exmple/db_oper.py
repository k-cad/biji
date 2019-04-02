#利用pymysql封装的数据库操作类
#连接,断开数据库，执行查询，增删改
from db_conf import *
import pymysql
class DBOper: #数据库操作类
    def __init__(self):
        self.db_conn = None

    def open_conn(self):#连接数据库
        try:
            self.db_conn = pymysql.connect(host,user,passwd,dbname)
        except Exception as e:
            print(e)
        else:
            print('数据库连接成功')
    def close_conn(self):#关闭连接
        try:
            self.db_conn.close()
        except Exception as e:
            print('数据库连接关闭错误')
            print(e)
        else:
            print('数据库连接关闭成功')
    def do_query(self,sql):#查询
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            print(result)
            return result
            
                
           
        except Exception as e:
            print("执行查询信息错误")
            print(e)
            return None

    def do_update(self,sql):
        try:
            cursor = self.db_conn.cursor()
            result = cursor.execute(sql)
            self.db_conn.commit()
            cursor.close()
            return result
        except Exception as e:
            self.db_conn.rollback()
            print("执行SQL出错")
            print(e)
            return None

    def do_insert(self,sql):
        try:
            cursor = self.db_conn.corsor()
            result = cursor.execute(sql)
            self.db_conn.commit()
            cursor.close()
            return result
        except Exception as e:
            self.db_conn.rollback()
            print("执行SQL出错")
            print(e)
            return None
           


if __name__ == '__main__':
    dboper = DBOper()
    dboper.open_conn()
    result = dboper.do_query("select * from orders where order_id = '2018010100000007'")
    # for r in result:
    #     print(r)
    # sql = '''update orders set amt=amt+100
    #          where order_id = '2018010100000002'
    #       '''
    # result = dboper.do_update(sql)
    print(result)

    dboper.close_conn()



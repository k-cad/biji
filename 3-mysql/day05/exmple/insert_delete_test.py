import pymysql

from db_conf import *

try:
    conn = pymysql.connect(host,user,passwd,dbname)
    cursor = conn.cursor()
    # sql = '''insert into orders
    # (order_id,cust_id,amt)
    # values('201801010001','C00001',230.00)
    # '''
    sql = "delete from orders where cust_id ='C00001'"
    cursor.execute(sql)
    conn.commit()
    # print('插入成功')
    print('删除成功')

except Exception as e:
    conn.rollback()
    print(e)

cursor.close()
conn.close()



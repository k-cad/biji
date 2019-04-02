#查询示例
# 1)导入pymysql模块
import pymysql
# 2)创建数据库连接
host = 'localhost' #主机
user = 'root' #用户名
passwd = '123456' #密码
dbname = 'eshop' #库名称
conn = pymysql.connect(host,user,passwd,dbname)
# 3)创建游标对象
cursor = conn.cursor()

# 4)使用游标对象提供的方法，执行SQL语句
sql = "select * from orders"
cursor.execute(sql)
result = cursor.fetchall()

# 5)打印数据
for r in result:
    order_id = r[0]
    cust_id = r[1]
    amt = r[5]
    print(order_id,cust_id,amt)

# 6)关闭游标
cursor.close()
# 7)关闭数据库连接对象
conn.close()


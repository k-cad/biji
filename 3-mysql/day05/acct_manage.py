# acct_manage.py
# 账户管理类
from db_oper import *
from acct import *

class AcctManage:
    def __init__(self, db_oper):
        self.db_oper = db_oper  #实例化数据操作对象

    def query_by_id(self, acct_no): #查询账户
        if not acct_no:
            print("账号对象非法")
            return None
        if acct_no == "":
            print("账号不能为空")
            return None
        
        sql = "select * from acct where acct_no = '%s'" % acct_no

        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None
        else:
            acct_info = result[0]
            acct_no = acct_info[0]
            acct_name = acct_info[1]
            acct_type = int(acct_info[3])
            balance = acct_info[6]
            return Acct(acct_no, acct_name, acct_type, balance)

    def query_all_acct(self):
        accts = []
        sql = "select * from acct" 

        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None

        for acct_info in result:
            acct_no = acct_info[0]
            acct_name = acct_info[1]
            acct_type = int(acct_info[3])
            balance = acct_info[6]
            accts.append(Acct(acct_no, acct_name, acct_type, balance))

        return accts

    def insert_acct(self, acct):  #插入对象
        sql = '''insert into acct(acct_no, acct_name, acct_type, balance) \
                 values('%s','%s',%d,%.2f)
        ''' % (acct.acct_no, acct.acct_name, acct.acct_type, acct.balance)
        print("\nsql:%s\n" % sql)
        result = self.db_oper.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return

    # 作为作业布置
    def update_acct(self, acct):
        sql = '''update acct \
                 set acct_type = %d,
                     balance = %.2f
                where acct_no = '%s'
        ''' % (acct.acct_type, acct.balance, acct.acct_no)
        print("\nsql:%s\n" % sql)
        result = self.db_oper.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return

    # 作为作业布置
    def query_by_name(self, acct_name):
        if not acct_name:
            print("户名对象非法")
            return None
        if acct_name == "":
            print("户名不能为空")
            return None

        accts = []
        sql = "select * from acct where acct_name = '%s'" % acct_name

        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None

        for acct_info in result:
            acct_no = acct_info[0]
            acct_name = acct_info[1]
            acct_type = int(acct_info[3])
            balance = acct_info[6]
            accts.append(Acct(acct_no, acct_name, acct_type, balance))

        return accts

if __name__ == "__main__":
    db_oper = DBOper()    #实例化数据访问对象
    db_oper.open_conn()   #打开数据库连接

    am = AcctManage(db_oper)  #实例化AcctManage对象

    # 根据账号查询
    # acct = am.query_by_id("622345000001")
    # print(acct)

    # 根据户名查询
    # accts = am.query_by_name("Dokas")
    # for a in accts:
    #     print(a)

    # 插入
    # new_acct = Acct("622345000006", "Dokas", 1, 4444.67)
    # am.insert_acct(new_acct)

    # 更新
    # new_acct = Acct("622345000005", "Dokas", 1, 1111.22)
    # am.update_acct(new_acct)

    # 查询全部
    # accts = am.query_all_acct()
    # for a in accts:
    #     print(a)

    db_oper.close_conn()



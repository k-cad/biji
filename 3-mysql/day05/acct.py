# acct.py
# 账户类
class Acct:
    def __init__(self, acct_no, acct_name, acct_type, balance):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_type = acct_type
        self.balance = balance

    def __str__(self):
        ret = "账号:%s, 户名:%s, 类型:%d, 余额:%.2f" % \
             (self.acct_no, self.acct_name, self.acct_type, self.balance)
        return ret


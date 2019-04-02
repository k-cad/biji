# account.py
# 账户类
dict_status = {  #状态字典
  0:"正常",1:"冻结",2:"挂失",3:"销户"
}
dict_type = {0:"借记账户", 1:"贷记账户"}

class Account:  
    def __init__(self, acct_no, acct_name,
                 reg_date, acct_type,
                 acct_status, balance):
        self.acct_no = acct_no #账号
        self.acct_name = acct_name #户名
        self.reg_date = reg_date #开户日期
        self.acct_type = acct_type #类型
        self.acct_status = acct_status #状态
        self.balance = balance #余额
    
    def diposite(self, amt): #存款
        print("存款前余额：%.2f"%self.balance)
        self.balance += amt #修改余额
        print("存款后余额：%.2f"%self.balance)

    def draw(self, amt): #取款
        if self.acct_status == 0: #正常
            if self.balance < amt: #余额不足
                print("余额不足")
                return
            else:  #余额充足
                print("取款前余额:%.2f" % self.balance)
                self.balance -= amt #修改余额
                print("取款后余额:%.2f" % self.balance)
        else:  #非正常状态
            print("状态不允许取款")
    
    def freeze(self): # 冻结
        if self.acct_status != 0:
            print("状态不允许冻结")
            return
        self.acct_status = 1 #状态置为冻结
        print("账户已冻结")

    def unfreeze(self): #解冻
        if self.acct_status != 1: #判断已冻结
            print("状态不允许解冻")
            return
        self.acct_status = 0 #状态置为正常
        print("账户已解冻")

    def __str__(self): #重写__str__()
        # 将状态转换为对应的字符串
        status = dict_status[self.acct_status]
        # 将类型转换为对应的字符串
        type = dict_type[self.acct_type]
        ret="账号:%s,户名:%s,开户日期:%s,类型:%s,状态:%s,余额:%.2f"\
            %(self.acct_no, self.acct_name, \
             self.reg_date, type, \
             status, self.balance)
        return ret

if __name__ == "__main__":
    acct = Account("6223450001", "张大大", 
                   "2018-01-01", 0, 0, 2000.00)
    acct.diposite(1000.00)  #存款
    acct.draw(500)  #取款
    print(acct)  #打印账户信息
    acct.freeze() #冻结
    print(acct)  #打印账户信息
    acct.unfreeze() #解冻
    print(acct)  #打印账户信息




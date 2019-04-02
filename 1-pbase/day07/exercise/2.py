# 输入一些单词和解释，将单词作为键，将解释作为值，存入字典，
# 当输入单词或解释为空时停止输入，打印这个字典
# 输入查询的单词给出单词内容，如果单词不存在，提示啊：查无此词

d={}
while True:
    k=input('请输入单词:')    
    if k=='':#if not k:
        break
    v=input('请输入解释:')
    if v=='':#if not v:
        break
    d[k]=v
print(d)

while True:
    w=input('请输入查询单词：')
    if w in d:
        print('该词解释为：',d[w])
        
    else:
        print('查无此词')
        break

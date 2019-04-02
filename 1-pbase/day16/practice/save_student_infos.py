def save_to_file(L):
    try:
    #1，打开文件
        f=open('mynote.txt','w')
        for d in L:
            f.write(d['name'])
            f.write(',')
            f.write(str(d["age"]))
            f.write(',')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
        print('保存成功')
    except OSError:
        print('保存失败')




L=[dict(name='zz',age=18,score=89),
    dict(name='yy',age=19,score=90)  
   ]
save_to_file(L)
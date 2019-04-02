#此示例示意用seek方法来改变文件流的读写位置

f=open('char20.txt','rb')
print('当前文件的读写位置是',f.tell())
b=f.read(3)
print('读写三位置后的读写位置是',f.tell())

f.seek(5,0)
print('移动后的文件的位置',f.tell())
b=f.read(5)
print('b=',b)

f.close
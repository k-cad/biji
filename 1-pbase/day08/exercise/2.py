def get_chinese_char_count(s):
    c=0
    for  x in s:
        # if int('0x4e00',base=16)<=ord(x)<=int('0x9fa5',base=16):
        if 0x4e00<=ord(x)<=0x9fa5:
            c += 1
    return c

s=input('请输入中英文混合字符串：')



print('中文字符的个数是：',get_chinese_char_count(s))



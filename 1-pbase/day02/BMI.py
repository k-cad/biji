meter=float(input('身高(米)是：'))
kg=float(input('体重是(公斤)：'))
BMI=kg/meter**2
print('BMI=',BMI)
if BMI < 18.5:
    print('体重过轻') 
elif 18.5 <= BMI < 24: 
    print('正常范围')
else:
    print('体重过重')
    
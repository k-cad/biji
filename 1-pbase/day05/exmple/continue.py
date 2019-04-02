# for x in range(5):
#     if x == 2:
#         continue
#     print(x)



# for x in range(10):
#     if x % 2 ==1:
#         continue
#     print(x)

# x = 0
# while x <10:
#     if x % 2==0:
        
#         continue
#         print(x)
   
    
    

# x = 0
# while x < 5:
#     if x==2:
#         x += 1 # 在continue之前
#         continue
#     x += 1
#     print(x)



s=0
for x in range(1,101):
    if x % 2==0 or x%3==0 or x%5==0 or x%7==0 :
        continue
    s += x
print(s) 
def get_heigh(h,n):
    for _ in range(n):
        h/=2
    
    return h

print(get_heigh(100,10))

def get_distance(h,n):
    s=0
    for _ in range(n):
        s+=h
        h=h/2
        s+=h
    return s

print(get_distance(100,10))
        


from test import *
import time

t = time.time()

for i in range(10):
    # count(1,1)
    myIO()


# print('Sigle CPU:',time.time() - t)
print('Sigle IO:',time.time() - t)
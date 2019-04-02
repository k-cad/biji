import copy  # 导入考拷贝模块
L1 = [1, 2, [3.1, 3.2]]
L2 = copy.deepcopy(L1)
L2[2][0] = 3.14
print(L1)  # [1, 2, [3.1, 3.2]]
print(L2)  # [1, 2, [3.14, 3.2]]

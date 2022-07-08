import math
num = int(input('请输入一个正整数：'))
for i in range(2,num):
    if num%i == 0:
        print('不是素数')
        break
else:
     print('是素数')

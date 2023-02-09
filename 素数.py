import math
num = eval(input())
n = math.sqrt(num)
i = 2
while i <= n:
    if num % i == 0:
        print('不是素数')
        break
    i += 1
else:
    print('是素数')
    

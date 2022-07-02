print('100~500之间不能被3整除但能被4整除的数为：')
y = 100
x = 0
while y < 500:
    if y % 3 != 0 and y % 4 == 0:
        print('{} '.format(y),end = '')
        x += 1
    y += 1
    if x == 10:
        print()
        x = 0

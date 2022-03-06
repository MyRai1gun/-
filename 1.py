import turtle as t
x=2
t.speed(0)
while x <=12:
    y = 0
    while y < x:
        t.fd(100)
        t.left(180-180*(x-2)/x)
        y += 1
    x += 1
t.done()

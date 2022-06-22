import turtle as t
x=2
for x in range(10):
    t.speed(0)
    for y in range(x):
        t.fd(100)
        t.left(180-180*(x-2)/x)
t.done()

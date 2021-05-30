from random import randrange
import time

t1 = time.time()

seq = [randrange(10**10) for i in range(10**4)]
dd = float("inf")


seq.sort()
for i in range(len(seq)-1):
    x, y = seq[i], seq[i+1]
    if x == y:
        continue
    d = abs(x-y)
    if d < dd:
        xx, yy, dd = x, y, d

t2 = time.time()

print(xx, yy, abs(xx-yy), dd)
print(t2-t1)


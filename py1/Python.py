import random


x = int()
y = int()

for i in range(10000000):
    y = random.randint(100, 2000)
    x = x+y
    print(x)
    print("X-Y=", x-y)

import math
import random
n = 1000000
nc = 0
d = 5.0
dist = 0
pi = 0
for i in range (n):
  x = random.random() * d
  y = random.random() * d
  dist = math.sqrt((d/2 - x) ** 2 + (d/2 - y) ** 2)
  if dist < d/2:
    nc = nc + 1
pi = 4 * (nc/n)
print(pi)
  

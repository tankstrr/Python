import math
import time

print ("tankPi v1")
print (math.pi)

maxSteps = 10000000
pi = 0
addsub = 'a'

for d in range (1, maxSteps, 2):
    if (addsub == 'a'):
        pi += 4 / d
        addsub = 'b'
    else:
        pi -= 4 / d
        addsub = 'a'

print (pi)

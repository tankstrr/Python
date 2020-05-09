import math
import time

print ("tankPrime v1")
def is_prime_v2(n):
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor):
        if n % d == 0:
            return False
    return True

t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1 - t0)

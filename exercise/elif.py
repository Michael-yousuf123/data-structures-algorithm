import math
import os
import random
import re
import sys


n = random.randint(1, 100)

if n % 2 == 0:
    print("Weird")
elif (n % 2 == 0 or 2 <= n <= 5):
    print("Not Weird")
elif (n % 2 == 0 and 6 <= n%2 <= 20):
    print("Weird")
elif (n % 2 == 0 and n > 20):
    print("Not Weird")
if __name__ == '__main__':
    n = int(input().strip())
    n =2

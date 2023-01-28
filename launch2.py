import os
from random import sample
from statistics import mean, pstdev
import sys

GARBAGE_FILE = "tests/garbage/out"
RESULT_FILE = "tests/garbage/result"
os.system("make -s")
size = int(sys.argv[1])
limit = int(sys.argv[2])
operations = []
n = 0
while True:
    nums = " ".join(map(str, sample(range(-2000, 2000), k=size)))
    # print(nums)
    os.system(f"./push_swap {nums} > {GARBAGE_FILE}")
    count = sum(1 for _ in open(GARBAGE_FILE))
    # print(f"{count} operations")
    os.system(f"cat tests/garbage/out | ./checker_linux {nums} > {RESULT_FILE}")
    result = open(RESULT_FILE).read().strip()
    print(result)
    operations.append(count)
    if count >= limit or result == "KO":
        break
print(nums)
print(f"{count} operations")
print(f"Average number of operations : {mean(operations)} +- {pstdev(operations):.2f}")
print(f"Minimum number of operations : {min(operations)}")
print(f"Failed at test {n}")

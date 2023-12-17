# 시간 측정
import math
import time

from book.greedy import Greedy

g = Greedy()

print("문제 :", g.ex1.__doc__)
start_time = time.process_time()
print(g.ex1(18022))
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")


print("문제 :", g.ex2.__doc__)
start_time = time.process_time()
print(g.ex2())
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")
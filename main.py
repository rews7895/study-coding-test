# 시간 측정
import math
import time

from book.greedy import Greedy

g = Greedy()
ex_count = g.count


print("문제1 :", g.ex1.__doc__)
start_time = time.process_time()
print(g.ex1())
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")

print("문제2 :", g.ex2.__doc__)
start_time = time.process_time()
print(g.ex2())
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")

print("문제3 :", g.ex3.__doc__)
start_time = time.process_time()
print(g.ex3())
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")

print("문제4 :", g.ex3.__doc__)
start_time = time.process_time()
print(g.ex4())
end_time = time.process_time()
print(f"실행시간 : {int(round((end_time - start_time) * 1000))}ms")

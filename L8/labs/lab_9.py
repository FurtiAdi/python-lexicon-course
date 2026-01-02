#Challenge Task 9: Recursive problem design 
import time

def sum_seq(num):
  if num == 1:
    return num
  
  return num + sum_seq(num-1)
  
start = time.time()
print("Total sum: ",sum_seq(3)) #it will ad 1,2,3
print("Total time without memoization: ",time.time() - start)

#With memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def sum_seq(num):
  if num == 1:
    return num
  
  return num + sum_seq(num-1)
  
start = time.time()
print("Total sum: ",sum_seq(3))
print("Total time with memoization: ", time.time() - start)
print(sum_seq.cache_info())

"""
The performance is a bit better with memoization because previously executed 
results are cached and reused, which avoids repeated recursive calls. 
This leads to faster execution time
"""
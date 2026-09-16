# generate an input, then time the actual thing that needs timing, over multiple trials, and find the average time
# record the times in microseconds, which is not the default unit, so you have to convert
# do that for n=10, and then also n=1000 and n=1_000_000
# your code should somehow output all of your results to the terminal, so you can save them
# save them in a file or something

# 'Add a number to the beginning of a list of n elements, with lst.insert(0, -77).

# Add a number to the beginning of a list of n elements, with lst.append(-77).

# Remove a number from the beginning of a list of n elements, with lst.pop(0).

# Remove a number from the beginning of a list of n elements, with lst.pop().

# Determine if a number is in a list of n elements, when the answer is true, with present in lst.

# Determine if a number is in a list of n elements, when the answer is false, with absent in lst.

# Determine if a key is in a dict of n key-value pairs, when the answer is true, with present in dct.

# Determine if a key is in a dict of n key-value pairs, when the answer is false, with absent in dct.'

def make_list(n):
  return list(range(n))

def make_dict(n):
  return {i: i for i in range(n)}

n = 10

lst = make_list(n)

import statistics
import time



times = []
for i in range(100000):
    lst = make_list(n)
    before = time.perf_counter()
    lst.insert(0,-77)
    after = time.perf_counter()
    delta = after - before
    times.append(delta * 1000000)

print("mean insert: ", statistics.mean(times))
print("median insert: ", statistics.median(times))

times = []
for i in range(100000):
    lst = make_list(n)
    before = time.perf_counter()
    lst.append(-77)
    after = time.perf_counter()
    delta = after - before
    times.append(delta * 1000000)

print("mean append: ", statistics.mean(times))
print("median append: ", statistics.median(times))

times = []
for i in range(100000):
    lst = make_list(n)
    before = time.perf_counter()
    lst.pop(0)
    after = time.perf_counter()
    delta = after - before
    times.append(delta * 1000000)

print("mean pop(0): ", statistics.mean(times))
print("median pop(0): ", statistics.median(times))



times = []
for i in range(100000):
    lst = make_list(n)
    before = time.perf_counter()
    lst.pop()
    after = time.perf_counter()
    delta = after - before
    times.append(delta * 1000000)

print("mean pop(): ", statistics.mean(times))
print("median pop(): ", statistics.median(times))



def present_in_list(lst):
  target = 6
  for num in range (len(lst)):
    if lst[num] == target:
      return True
  return False
present_in_list(lst)

times = []
for i in range(100000):
    before = time.perf_counter()
    present_in_list(lst)
    after = time.perf_counter()
    delta = after - before
    times.append(delta * 1000000)

print("mean present lst: ", statistics.mean(times))
print("median present lst: ", statistics.median(times))



dic = make_dict(n)
target = 4

present = n - 1

absent = -1

# def present_in_dict(dic, target):
#   for num in range (present):

# def present_in_dict(dic, target):
#   lo = 0
#   hi = len(dic)
#   while lo < hi:
#     mid = ((hi - lo) // 2) + lo
#     if (target == dic[mid]):
#       # print ("mid", mid)
#       return mid
#     elif dic[mid] > target:
#       # print ("hi",hi)
#       hi = mid
#     else:
#       # print ("lo",lo)
#       lo = mid + 1
#   return None

# result = present_in_dict(dic,target)
# if result != None:
#   print (result)
# else:
#   print ("not here")

# times = []
# for i in range(100000):
#     before = time.perf_counter()
#     present_in_dict(dic, target)
#     after = time.perf_counter()
#     delta = after - before
#     times.append(delta * 1000000)

# print("mean present dict: ", statistics.mean(times))
# print("median present dict: ", statistics.median(times))
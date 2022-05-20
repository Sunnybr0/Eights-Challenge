"""
Author: Suneel Denneny 682097
Assignment: U5C1 Eights Challenge
Description: Pattern Matchers have been designed for various sorts of patterns. Mr. HKP likes to observe patterns in numbers. After completing his extensive research on the squares of numbers, he has moved on to cubes. Now he wants to know all numbers whose cube ends in 888.

Given a number k, help Mr. HKP find the 1st number larger than k whose cube ends in 888.

Date Start: July 19, 2021
Date Completed: July 21, 2021
Completion Time: 1 hour

I pledge that this program represents my own code.
"""

#MY PROGRAM CODE

numOfTests = int(input())
nums = []
for i in range(numOfTests):
  num = int(input())
  it = 0
  start = 192
  while it < 1:
    if num >= start:
      start = start + 250
    else:
      answer = start
      it = 1
      nums.append(answer)

for i in range(len(nums)):
  print(nums[i])

"""
TEST RESULTS:

INPUT - 
2
191
192
OUTPUT - 
192
442

INPUT - 
2
441
442
OUTPUT - 
442
692

INPUT - 
2
691
692
OUTPUT - 
692
942

INPUT -
2
941
942
OUTPUT - 
942
1192

INPUT - 
5
1
200
470
700
950
OUTPUT - 
192
442
692
942
1192

INPUT - 
3
10192
11192
12192
OUTPUT - 
10442
11442
12442

INPUT - 
2
19999
15999
OUTPUT - 
20192
16192
"""
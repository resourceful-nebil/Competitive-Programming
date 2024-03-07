import sys
import bisect

def input():
  return sys.stdin.readline().strip()

t = int(input())

arr = list(map(int,input().split()))

n = int(input())

q = []
for i in range(n):
  q.append(int(input()))

arr.sort()

for i in range(n):
  print(bisect.bisect_right(arr,q[i]))


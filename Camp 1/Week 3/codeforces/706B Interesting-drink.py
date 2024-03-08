import sys
import bisect

def input():
  return sys.stdin.readline().strip()

t = int(input())

arr = list(map(int,input().split()))

n = int(input())

p = []
for i in range(n):
  p.append(int(input()))

arr.sort()

for i in range(n):
  print(bisect.bisect_right(arr,p[i]))


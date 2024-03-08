import bisect
import sys

def input():
  return sys.stdin.readline().strip()

t = int(input())

arr = list(map(int,input().split()))

n = int(input())

ans = []
for i in range(n):
  ans.append(int(input()))

arr.sort()

for i in range(n):
  print(bisect.bisect_right(arr,ans[i]))


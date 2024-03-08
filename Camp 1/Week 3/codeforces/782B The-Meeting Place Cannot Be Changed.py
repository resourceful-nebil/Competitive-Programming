import sys


def input():
  return sys.stdin.readline().strip()

n = int(input())

x = list(map(int,input().split()))
v = list(map(int,input().split()))

x_v = []
for i in range(n):
  x_v.append([x[i],v[i]])

x_v.sort()

def helper(t):
  limit = x_v[0][0] + x_v[0][1] * t
  for i in range(n):
    if limit >= x_v[i][0]:
      limit = min(limit, x_v[i][0] + t * x_v[i][1])
    
    else:
      if limit < x_v[i][0] - t * x_v[i][1]:
        return False
  return True 


l = 0
r = max(x) - min(x) 

while l <= r:
  mid = (l + r)/ 2
  if helper(mid):
    r = mid - (10**-6)
  else:
    l = mid + (10**-6)
  

print(l)

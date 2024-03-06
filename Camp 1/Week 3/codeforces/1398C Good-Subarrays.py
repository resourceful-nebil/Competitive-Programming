from collections import defaultdict
t = int(input())

for _ in range(t):
  n = int(input())

  arr = list(map(int,input()))
  # print(arr)
  
  prefix = [0]*(n+1)
  prefix[0] = 0
  for i in range(1,n+1):
    prefix[i] = prefix[i - 1] + arr[i-1]
  # prefix = prefix[1:]
  # print(prefix)

  ans = 0
  di = defaultdict(int)
  for i in range(n+1):
    good = prefix[i] - i
    if di[good] > 0:
      ans += di[good]
    di[good] += 1
    
  # print(di)
  
  print(ans)


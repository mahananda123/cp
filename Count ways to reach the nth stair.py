def traverse(n,dp):
  if n<=1:
    return 1
  if dp[n]!=-1:
    return dp[n]
  dp[n]=traverse(n-1,dp[n])+traverse(n-2,dp[n])
  return dp[n]
# driver code
T=int(input())
for _ in range(T):
  n=int(input())
  dp=[-1 for i in range(n+1)]
  res=traverse(n,dp)
  print(res)

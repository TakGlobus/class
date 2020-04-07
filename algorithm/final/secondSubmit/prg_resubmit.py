#
# Re-submit for partial credit
#

import numpy as np
def get_data():
  x = np.zeros((7,9))
  # p-1
  for i in [1,2,3,4]:
    x[0,i-1] = 1
  # p-2
  for i in [1,2,3,4,5]:
    x[1,i-1] = 1
  # p-3
  for i in [3,4,5,6]:
    x[2,i-1] = 1
  # p-4 
  for i in [4,5,6,7]:
    x[3,i-1] = 1
  # p-5
  for i in [5,6]:
    x[4,i-1] = 1
  # p-6
  for i in [6,7]:
    x[5,i-1] = 1
  # p-7
  for i in [7,8,9]:
    x[6,i-1] = 1

  return x


def findOptSize(x):
  """ x  : 2D array input data
  """
  inf = 99
  k,n = x.shape
  print(k,n)
  dp = np.zeros((n+1, k+1)).astype(np.float64)
  dp[:,:] = inf
  print(dp.shape)

  for ipath in range(1,k+1,1):
    # There is a path
    if x[ipath-1,0] == 1:  
      dp[1,ipath] = 1
    else:
      dp[1,ipath] = inf

  for u in range(2,n+1,1): 
    for ipath in range(1,k+1,1):
      # There is a path
      if x[ipath-1,u-1] == 1:  
        ## Before debug
        #dp[u,ipath] = min(dp[u-1,ipath],
        #                  np.min( np.array([ dp[u-1,jpath] for jpath in range(1,k+1,1) if jpath != ipath])
        #                  )+1
        #              )
        #print(dp[u,ipath])

        ## After debug 
        tmp_list = []
        for jpath in range(1,k+1,1):
          if jpath != ipath:
            if x[jpath-1, u-1] != 1 :
              tmp_list.append(dp[u-1,jpath])
        tmp = np.min(np.array(tmp_list))+1

        # update do table
        dp[u,ipath]  = min(dp[u-1,ipath], tmp)
      else:
        dp[u,ipath] = inf

  solution = min([dp[n,i] for i in range(1,k+1,1)])
  print("## DP Table  ##\n")
  print(dp.T)
  return solution

if __name__ == "__main__":
  x = get_data()
  print(x)

  solution = findOptSize(x)
  print(solution)


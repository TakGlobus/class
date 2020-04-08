#
# Re-submit for partial credit
#

import numpy as np
def get_data1():
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

def get_data():
  x = np.zeros((8,11))
  # p-1
  for i in [1,2]:
    x[0,i-1] = 1
  # p-2
  for i in [1,2,3]:
    x[1,i-1] = 1
  # p-3
  for i in [2,3,4]:
    x[2,i-1] = 1
  # p-4
  for i in [3,4,5]:
    x[3,i-1] = 1
  # p-5
  for i in [ j for j in range(6,10,1)]:
    x[4,i-1] = 1
  # p-6
  for i in [ j for j in range(6,12,1)]:
    x[5,i-1] = 1
  # p-7
  for i in [ j for j in range(9,12,1)]:
    x[6,i-1] = 1
  # p-8
  for i in [ 10, 11]:
    x[7,i-1] = 1
  return  x

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
        #  """ all nodes before u do not belong to Pj
        #  """
        tmp_list = []
        for jpath in range(1,k+1,1):
          if jpath != ipath:
            #tmp_node_info = np.array([x[jpath-1,v-1] for v in range(1,u+1,1)])
            nodup_list = []
            for v in range(1,u+1,1):
               if x[ipath-1,v-1] == 1 and x[jpath-1,v-1] == 1:
                 nodup_list.append(False)
               else:
                 nodup_list.append(True)

            if np.all(nodup_list):
              tmp_list.append(dp[u-1,jpath])

        if  len(tmp_list) > 0:
            tmp = np.min(np.array(tmp_list))+1
            dp[u,ipath] = min(tmp, dp[u-1, ipath])
        else:
            dp[u,ipath] = inf

      else:
        dp[u,ipath] = inf

  solution = min([dp[n,i] for i in range(1,k+1,1)])
  print("## DP Table  ##\n")
  #print(dp)
  print(dp.T)
  return solution

if __name__ == "__main__":
  x = get_data()
  print(x)

  solution = findOptSize(x)
  print(solution)


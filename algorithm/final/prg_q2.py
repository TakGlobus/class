import numpy as np

correct_answer = 3

# data generation
npath=9
nodes=8
x = np.zeros((nodes, npath))
data_index_list = [
  [0,1,2,4], [0,2,7],[2,4,5],[1,3,4],
  [2,5], [6,7], [7], [5,6,8]
]
for idx, i in enumerate(data_index_list):
  for j in i:
    x[idx,j] = 1
print(x)

def FindMinParition(x):
  """  x : data
      dp : dp table
  """  
  nodes = x.shape[0]
  npath = x.shape[1]
  inf = 9999

  dp = np.zeros((nodes+1, npath)).astype(int)

  # initialization
  dp[:,:] = inf
  dp[0,:] = 0

  for ipath in range(npath):
    if x[0,ipath] == 1:
      dp[1,ipath] = 1
    else:
      # inf or 0??
      dp[1,ipath] =  inf # ?? dp[0,ipath] #???

  # main loop
  for inode in range(2,nodes+1,1):
    for ipath in range(npath):
      node_index = inode-1 
      
      ## node u is included in Path i
      if x[node_index,ipath] == 1:
        ## already there is valid info
        if dp[inode-1,ipath] < inf:
          dp[inode,ipath] = dp[inode-1,ipath] # generic version
        else:
          dp[inode, ipath] = np.min( [dp[inode-1,j] for j in range(npath)]) + 1
          #print(dp[inode, ipath])

      ## node u is NOT included in Path i
      else:
          search_index = [ x[inode-1,ii] for ii in range(npath) ]
          update = False
          for idx, ii in enumerate(search_index):
            if ii == 1:
              if dp[inode-1,idx] == inf:
                update = True
      
          if update:
            if dp[inode-1,ipath] < inf:
              dp[inode, ipath] = np.min( [dp[inode-1,j] for j in range(npath)]) + 1
          else:
            if dp[inode-1,ipath] < inf:
              #dp[inode, ipath] = np.min( [dp[inode-1,j] for j in range(npath)])
              dp[inode,ipath] = dp[inode-1,ipath] # generic version

  print(dp)
  #print([dp[nodes,j] for j in range(npath)])
  solution = np.min( [dp[nodes,j] for j in range(npath)])
  return solution

if __name__ == "__main__":
  my_answer = FindMinParition(x)
  print(" My Answer = {} | Correct Answer {}".format(my_answer, correct_answer))

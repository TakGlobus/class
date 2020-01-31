import numpy as np

example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])
#example = np.array([4,3,-4,3,2,5])
#example = np.array([4,3,-4,3])
#example = np.array([-6,5,-2,6,-4,-7])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5,1,-1,-3,-1,6,0,-4])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5])

def my_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  nk = n//2
  dp = np.zeros((n+1,n+1, nk+1))  # dp[i,j,k]
  array = np.zeros((n+1,n+1))

  #--------------------------------------------------
  #  Construct array stored multiplication results
  #--------------------------------------------------
  for i in range(0,n+1,1):
    # loop to construct individual product array
    for j in range(0,i+1,1):

      if i > j :
        if i >= 1 and j >= 1:
          array[i,j] = x[i-1] * x[j-1]


  #--------------------------------------------------
  # "sum_proc" Update
  #--------------------------------------------------
  """ sum_proc : sum of k's pair of product

      Overview of solution:

  """
  overall_max = 0
  overall_k = 0
  tmp_max = 0
  tmp_k   = 0
  for i in range(1,n+1,1):
    for j in range(1,n+1,1):
      for k in range(1,nk+1,1):

        if i > j:
          if k <= i//2:
            if array[i,j] > 0:
              loop = [ dp[j-1,jj,k-1] for jj in range(0,j-1,1)] + [0]
              dp[i,j,k] = max(loop) + array[i,j]
            else:
              case1 = [dp[j-1, jj, k] for jj in range(0,j+1,1)]
              case2 = [dp[j, jj, k] for jj in range(0,j,1)]
              dp[i,j,k] = max(max(case1), max(case2),0)

            
            if dp[i,j,k] > tmp_max:
              print(dp[i,j,k], i,j,k)
              tmp_max = dp[i,j,k]
              tmp_k   = k

  # compute overall score
  overall_max = tmp_max
  overall_k = tmp_k


  # stdout
  print(dp[:,:,4])
  print(" MAX = {} when K = {}".format(overall_max, overall_k))

if __name__ == "__main__": 
  my_solution(example)


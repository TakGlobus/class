import numpy as np

example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])
#example = np.array([4,3,-4,3,2,5])
#example = np.array([4,3,-4,3])
#example = np.array([-6,5,-2,6,-4,-7])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5,1,-1,-3,-1,6,0,-4])

def my_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  nk = n//2
  dp = np.zeros((n+1,n+1, nk+1))  # dp[i,j,k]
  opt_index_array = np.zeros((n+1,n+1, nk+1))  # dp[i,j,k]
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
  update=False
  tmp_max = 0
  for i in range(1,n+1,1):
    for j in range(1,n+1,1):
      for k in range(1,nk+1,1):
      #for k in range(1,3,1):

        if i > j:

          ii = int(opt_index_array[i,j-1,k-1])
          case1 = dp[i, j-1, k-1] + max([array[i,jj] for jj in range(ii+1, j+1,1)]+[0])

          ii = int(opt_index_array[i-1,j-1,k-1])
          case2 = dp[i-1,j-1,k-1] + max([array[i,jj] for jj in range(ii+1, j+1,1)]+[0])

          case3 = dp[i-1,j,k]
          case4 = dp[i,j-1,k]

          #dp[i,j,k] = max(case1, case2)
          #update = True          
          if case1 >= case2:
            if (case1 - dp[i,j-1,k-1]) > 0:
                dp[i,j,k] = case1
                update = True
            else :
                update = False
          elif case1 < case2:
            if (case2 - dp[i-1,j-1,k-1]) > 0:
                dp[i,j,k] = case2
                update = True
            else :
                update = False

          if (dp[i,j,k] - max(case3, case4) ) <=  0:
            update = False
            dp[i,j,k] = max(case3, case4)
            if case3 >= case4:
              opt_index_array[i,j,k] = opt_index_array[i-1,j,k] 
            else :
              opt_index_array[i,j,k] = opt_index_array[i,j-1,k] 

          #if i == 4 and j == 1 and k == 1:
          #  print(case1, case2, case3, case4, dp[i,j,k]-case3)
          if i == 10 and j == 8 and k == 3:
            print(dp[i,j-1,k-1], dp[i-1,j-1,k-1])
            print(opt_index_array[i,j-1,k-1], opt_index_array[i-1,j-1,k-1])
            print(opt_index_array[:,:,3])
            print(dp[:,:,3])
            print(case1, case2, case3, case4, dp[i,j,k] ); exit(0)


          #if i == 6 and j == 5 and k ==2:
          #  ii = int(opt_index_array[i-1,j-1,k-1])
          #  print(dp[5,4,1])
          #  print(ii,j+1)
          #  print([array[i,jj] for jj in range(ii+1, j+1,1)]+[0])
          #  print('check here', tmp_max, case1, case2,case3, case4, ii);exit(0)

          tmp_max = np.max(dp[:i+1,:j+1,:k+1])
          #if (dp[i,j,k] - tmp_max) >  0:
          if update:
            """ updated
            """
            if k <= i/2:
              print("updated", dp[i,j,k], i,j,k, ii)
              opt_index_array[i,j,k] = i
              update = False
            
            #print("updated", dp[i,j,k], i,j,k, ii)
            #opt_index_array[i,j,k] = i
            #update = False

  # stdout
  print(array)
  print(np.max(dp))
  print(dp[:,:,1])
  print(dp[:,:,3])
  print(opt_index_array[:,:,1])

if __name__ == "__main__": 
  my_solution(example)


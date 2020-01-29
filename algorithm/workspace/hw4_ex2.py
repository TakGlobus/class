import numpy as np

#example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])
example = np.array([4,3,-4,3,2,5])
#example = np.array([4,3,-4,3])
#example = np.array([-6,5,-2,6,-4,-7])

def my_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  nk = n//2
  dp = np.zeros((n+1, nk+1))
  print(dp.shape)
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
        search each column of array to get local maximum
        move i+j column if we get previous value at array(i,j)
        stop if satisfy K requirements or hit bottom of array
        iterate start-column (initial position of j ) 

  """
  # First, disect k == 1 or k >=2 for simplicity

  #for k in range(1,nk+1,1):
  for k in range(1,2,1):
    sum_proc = 0
    for i in range(1,n+1,1):

      # initialize index in every row iter
      ik = 0
      ii = 1
      jj = 1

      for j in range(1, n+1,1):

        if i > j:

          ##### K == 1
          if k == 1:      
            if array[i,j] > sum_proc:
              #print(array[i,j], sum_proc)
              sum_proc = array[i,j]
  
            #print(sum_proc,i,k)
            #--------------------------------------------------
            # DP Update
            #--------------------------------------------------
            dp[i][k] = max( dp[i-1][k-1], dp[i-1][k], sum_proc )
          

  ##### K >= 2
  for k in range(2, nk+1,1):
    ik = 0
    sum_proc = 0
    for j in range(1,n+1,1):
      for i in range(2,n+1,1):

          jj = i + j
          tmp_list = []
          jj = i+j+1
          for ii in range(i+j,n+1,1):
            #print("I {} J {} |  II  {}  JJ  {} | sum_proc {} {}".format(
            #       i,j,ii,jj, sum_proc, array[ii,j]) 
            #)
            #print(" i {} j {} ii {} jj {} array {}".format(i,j,ii,jj,array[ii,jj]))
            if ii <= n and jj <= n:
              tmp_list.append(array[i,j]+array[ii,jj])
          #print(tmp_list) #;exit(0)

          if len(tmp_list) > 0:
            sum_proc = max(tmp_list)

            #print(sum_proc,i,k)
            #--------------------------------------------------
            # DP Update
            #--------------------------------------------------
            dp[i][k] = max( dp[i-1][k-1], dp[i-1][k], sum_proc )


  # stdout
  print(array)
  print(dp)

if __name__ == "__main__": 
  my_solution(example)

#            if array[i,j] + sum_proc > sum_proc:
#                #print("I {} J {} |  II  {}  JJ  {} | sum_proc {}".format(i,j,ii,jj, sum_proc) )
#                if i >= ii and j >= jj:
#                #if j >= jj:
#                  ii = i+j+1
#                  jj = i+j 
#                  if ik <= k:
#                    sum_proc += array[i,j]
#                    print("I {} J {} |  II  {}  JJ  {} | sum_proc {}".format(i,j,ii,jj, sum_proc) )
#                    ik +=1
#                  else :
#                    break

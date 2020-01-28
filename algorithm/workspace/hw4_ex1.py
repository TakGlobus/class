import numpy as np

#example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])
example = np.array([4,3,-4,3,2,5])
#example = np.array([-6,5,-2,6,-4,-7])

def make_candidates(array, nk):
  """
      array[i,j] = product of input[i] x input[j]
  """
  ni, nj = array.shape
  cand_list = []

  for istart in range(1, ni+1,1):
    tmp_cand = 0.0
    while ik < nk:
      for i in range(istart,ni+1, i1):
        ii = 1
        jj = 2
        for j in range(0,nj+1,1):
          if array[i,j] > 0:
            if i >= ii and j >= jj:
              tmp_cand += array[i,j]
              ii = jj+1
              jj = ii
      break
    cand_list.append(tmp_cand)
  return cand_list


def my_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  nk = n//2
  dp = np.zeros((n+1, nk+1))
  print(dp.shape)
  array = np.zeros((n+1,n+1))

  #ii = 1
  #jj = 2
  #pivot = 0
  #ik = 0
  #for k in range(1,2,1):
  for k in range(1,nk+1,1):
    for idx, i in enumerate(range(0,n+1,1)):
      for jdx, j in enumerate(range(0,n+1,1)):

        if i < j :
          if i >= 1 and j >= 1:
            array[i,j] = x[i-1] * x[j-1]

      #=====================================================
      # Create new sum of product list
      #=====================================================
      ik = 0
      cand_list = []
      for istart in range(1,i+1,1):
        tmp_cand = 0
        while ik <= k:
          ii = istart
          jj = istart+1
          for l in range(0,i+1,1):
            for z in range(0,n+1,1):
              if array[l,z] > 0:
                if l >= ii and z >= jj:
                  print(array[l,z] )
                  tmp_cand += array[l,z]
                  ii = l+1
                  jj = ii+1
                  ik +=1
                  #print(" ii {} jj {} ik {} | tmp_cand {}".format(
                  #        ii,jj,ik, tmp_cand )
                  #)
          cand_list.append(tmp_cand)
          #if ik < nk:
          #  cand_list = [0]
          break
     
      imax = 0
      if len(cand_list) > 0:
        imax = max(cand_list)
        print(" K= {} I = {} imax={}".format(k, i, imax) )

      #=====================================================

      ## DP TABLE
      if imax > dp[i-1,k]:
        dp[i,k] = max( dp[i-1][k] , imax )
      elif imax <= dp[i-1,k] :
        dp[i,k] = dp[i-1,k]

  print(array)
  print(dp)

if __name__ == "__main__": 
  my_solution(example)


#    # DP table update
#    if k == 1 :       
#      pivot = 0
#      for l in range(0,n+1,1):
#       if array[1,l] > pivot:
#         dp[l,1] = array[1,l]
#         pivot = array[1,l]
#       else :
#         dp[l,1] = dp[l-1,1]

import numpy as np

#example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])
#example = np.array([4,3,-4,3,2,5])
#example = np.array([4,3,-4,3])
#example = np.array([-6,5,-2,6,-4,-7])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5,1,-1,-3,-1,6,0,-4])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5])

correct_answer = 222454
example= np.array([-100,-82,60,-73,-82,3,62,36,-75,69,34,80,25,-51,51,-66,90,56,65,-2,-95,-9,-91,-56,-12,-23,-81,13,100,91,4,76,45,-95,33,-92,-59,34,63,10,50,48,-47,-74,-65,27,-90,-100,15,47,-12,16,82,11,-11,-76,-72,-1,-84,10,61,89,50,-32,29,16,50,-53,55,-97,-33,-55,-3,-16,27,0,-43,85,-74,47,-70,3,64,0,-84,-16,80,-5,-94,-46,45,7,44,21,92,28,-14,94,84,-94,-27,-8,71,-72,-31,-29,-10,9,33,45,3,28,-13,-48,36,-29,58,-41,42,-24,-18,94,53,42,-49,-22,64,88,76,-55,-52,3,-37,49,-51,-72,63,1,81,-27,60,-26,-38,87,-58,19,63,57,68,52,-79,-39,54,-80,98,100,5,79,2,33,66,-21,4,36,-26,-12,-37,5,31,92,-63,40,11,54,0,-97])


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
              #print(dp[i,j,k], i,j,k)
              tmp_max = dp[i,j,k]
              tmp_k   = k

  # compute overall score
  overall_max = tmp_max
  overall_k = tmp_k


  # stdout
  #print(dp[:,:,4])
  print(" MAX = {} when K = {} Correct Ans = {}".format(overall_max, overall_k,correct_answer))

if __name__ == "__main__": 
  my_solution(example)


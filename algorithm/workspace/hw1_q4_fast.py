import numpy as np

#correct_answer=47
#example = np.array([4,3,-4,3,2,5,-3,-5,1,-4])

#example = np.array([4,3,-4,3,2,5])
#example = np.array([4,3,-4,3])
#example = np.array([-6,5,-2,6,-4,-7])
#correct_answer=141
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5,1,-1,-3,-1,6,0,-4])
#example = np.array([-6,5,-2,6,-4,-7,1,0,6,-1,6,7,5])

#correct_answer = 222454
#example= np.array([-100,-82,60,-73,-82,3,62,36,-75,69,34,80,25,-51,51,-66,90,56,65,-2,-95,-9,-91,-56,-12,-23,-81,13,100,91,4,76,45,-95,33,-92,-59,34,63,10,50,48,-47,-74,-65,27,-90,-100,15,47,-12,16,82,11,-11,-76,-72,-1,-84,10,61,89,50,-32,29,16,50,-53,55,-97,-33,-55,-3,-16,27,0,-43,85,-74,47,-70,3,64,0,-84,-16,80,-5,-94,-46,45,7,44,21,92,28,-14,94,84,-94,-27,-8,71,-72,-31,-29,-10,9,33,45,3,28,-13,-48,36,-29,58,-41,42,-24,-18,94,53,42,-49,-22,64,88,76,-55,-52,3,-37,49,-51,-72,63,1,81,-27,60,-26,-38,87,-58,19,63,57,68,52,-79,-39,54,-80,98,100,5,79,2,33,66,-21,4,36,-26,-12,-37,5,31,92,-63,40,11,54,0,-97])

correct_answer= 219414
example = np.array([-10,-4,-55,-78,-44,-18,69,-19,27,-58,91,-51,36,-38,-33,32,2,-7,63,79,-20,85,-34,-82,96,4,50,-40,40,37,-60,18,19,-43,-87,56,86,54,-98,-17,15,-71,96,-76,-3,-79,-72,27,-19,-68,93,-35,68,46,44,-14,92,-42,82,-73,-16,-100,21,91,69,22,-41,-62,2,-30,33,-10,75,-12,-27,53,40,8,68,-39,60,87,37,-87,31,-64,49,-48,-30,-34,53,59,-39,-89,-66,-47,-21,22,-32,-50,59,-1,73,-77,-54,46,11,46,-6,-53,-13,41,77,82,56,82,88,-88,-70,-25,71,-26,9,-45,3,71,-41,97,51,27,100,61,48,18,-55,-19,30,49,-59,87,-19,-98,97,-11,49,-9,46,-69,-4,-55,11,30,55,10,-69,-45,-29,-5,98,-79,-78,68,-2,38,35,-38,-97,-27,71,13,-13,-59,-57,-88,-81,-13])

def my_old_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  nk = n//2
  print(" Size of array {} | Upperbound # of k {}".format(n,nk))
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
                #++ case: adding array[i,j] is larger than non-adding case
                #loop = [ dp[j-1,jj,k-1] for ii in range(0,j-1,1) for jj in range(0,j-1,1)]+[0]
                loop = [ dp[ii,jj,k-1] for ii in range(0,j,1) for jj in range(0,j,1)]+[0]
                tmp1 = 0
                if len(loop) > 0:
                  #if not max(loop) == 0:
                    tmp1 = max(loop) + array[i,j]
                #++ case: non-adding case is larger
                tmp2 = max([dp[j-1,jj,k] for jj in range(0,j,1)]+[0]) 
                #++ case: non-adding case 2
                tmp3 = max([dp[i,jj,k] for jj in range(0,j,1)]+[0]) 
                dp[i,j,k] = max(tmp1,tmp2,tmp3)

            else:
              # if now j then case 1 is below j
              case1 = [dp[j-1, jj, k] for jj in range(0,j+1,1)]+[0]
              # if now j then case 1 is upper j
              case2 = [dp[i, jj, k] for jj in range(0,j-1,1)]+[0]

              dp[i,j,k] = max(max(case1), max(case2),0)
            
            if dp[i,j,k] > tmp_max:
              tmp_max = dp[i,j,k]
              tmp_k   = k

  # compute overall score
  overall_max = tmp_max
  overall_k = tmp_k


  # stdout
  print(" MAX = {} when K = {} Correct Ans = {}".format(overall_max, overall_k,correct_answer))


def my_solution(x):
  """
    x  : example array
  """
  n = len(x) # number of items
  print(" Size of array {} ".format(n))
  #dp = np.zeros((n+1,n+1))  # dp[i,j]
  dp = np.zeros((n+1))  # dp[i,j]
  array = np.zeros((n+1,n+1))


  #--------------------------------------------------
  # "sum_proc" Update
  #--------------------------------------------------
  """ sum_proc : sum of k's pair of product

      Overview of solution:
  """
  for i in range(1, n+1, 1):
    for j in range(1, n, 1):
      if j < i:
        tmp = x[i-1] * x[j-1]
        if dp[j-1] + tmp > dp[i-1]:
          #print(dp[j-1], tmp, dp[j-1]+tmp, dp[i])
          dp[i] = max(dp[j-1] + tmp, dp[i])
        else:
          dp[i] = max(dp[i-1], dp[i])


  overall_max = np.max(dp)
  # stdout
  print(" MAX = {} Correct Ans = {}".format(overall_max, correct_answer))

if __name__ == "__main__": 
  my_solution(example)


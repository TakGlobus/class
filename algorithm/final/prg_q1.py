
import numpy as np

## Debug
#correct_answer=5
#x = [28, 35, 14, 26, 40, 41, 32, 21, 36, 50, 19, 26]
#correct_answer=3
#x = [2, 13, 16, 3]
#correct_answer=5
#x = [38, 45, 36, 46, 42, 27, 9, 15, 11, 21, 8, 50, 37, 33, 25, 9, 3, 45, 46, 18]
correct_answer=7
x = [3, 47, 19, 7, 32, 8, 46, 15, 40, 37, 3, 3, 6]
#correct_answer=2
#x = [1,18,19]
#correct_answer=7
#x = [18, 11, 40, 14, 41, 44, 33, 49, 17, 2, 43, 1, 28, 46, 26, 14, 21, 41, 8]
#correct_answer=5
#x= [6, 21, 17, 27, 7, 21, 13, 2, 12]
#correct_answer=5
#x = [15, 31, 31, 15, 9, 21, 9, 3, 8, 11]


## Test
dataset_list = [
 [ 1, 18, 19],
 [ 2, 13, 16, 3],
 [ 17, 28, 30, 19, 26],
 [ 4, 23, 11, 17, 20, 19],
 [ 1, 27, 11, 25, 5, 2, 14],
 [ 29, 2, 29, 3, 11, 11, 10, 6],
 [ 6, 21, 17, 27, 7, 21, 13, 2, 12],
 [ 15, 31, 31, 15, 9, 21, 9, 3, 8, 11],
 [ 47, 46, 9, 40, 50, 18, 40, 8, 30, 1, 20],
 [ 28, 35, 14, 26, 40, 41, 32, 21, 36, 50, 19, 26],
 [ 3, 47, 19, 7, 32, 8, 46, 15, 40, 37, 3, 3, 6],
 [ 29, 26, 32, 7, 19, 34, 6, 2, 4, 20, 48, 26, 16, 16],
 [ 33, 42, 19, 27, 1, 2, 29, 2, 9, 47, 17, 43, 26, 18, 10],
 [ 6, 17, 7, 14, 3, 26, 27, 42, 24, 18, 31, 42, 42, 38, 28, 9],
 [ 40, 26, 2, 24, 39, 40, 38, 8, 23, 10, 23, 3, 49, 45, 33, 50, 11],
 [ 19, 10, 33, 18, 5, 6, 13, 3, 13, 44, 41, 8, 49, 18, 28, 3, 22, 25],
 [ 18, 11, 40, 14, 41, 44, 33, 49, 17, 2, 43, 1, 28, 46, 26, 14, 21, 41, 8],
 [ 38, 45, 36, 46, 42, 27, 9, 15, 11, 21, 8, 50, 37, 33, 25, 9, 3, 45, 46, 18],
]
answerset_list=[
  2,3,4,5,5,6,5,5,6,5,7,5,6,5,8,6,7,5
]


def OldFindLongestStableArray(x):
  """
    INPUT
      x : input sequence
  """


  n = len(x)
  dp = np.zeros((n+1,n+1,n+1))

  tmp = 0
  x = [99999]+x

  #initialization
  for i in range(0,3,1):
    for j in range(0,2,1):
        k = 0
        if k<j<i:
          if x[j] <= x[i] and x[i]<= x[k]:
            #if dp[j,k,k-1] != 0:
            #  dp[i,j,k] = dp[j,k,k-1] + 1
            #else:
            #  dp[i,j,k] = 2
            dp[i,j,k] = max(2, dp[j,k,0]+1)
            
          elif x[k] <= x[i] and x[i]<= x[j]:
            #if dp[j,k,k-1] != 0:
            #  dp[i,j,k] = dp[j,k,k-1] + 1
            #else:
            #  dp[i,j,k] = 2
            dp[i,j,k] = max(2, dp[j,k,0]+1)

          if tmp < dp[i,j,k]:
              tmp = dp[i,j,k]
          

  # main
  for i in range(3,n+1,1):
    for j in range(2,n+1,1):
      for k in range(1,n+1,1):
        for l in range(0,n+1,1):
          # valid index order
          if l<k<j<i:
            if x[j] <= x[i] and x[i]<= x[k]:
              #if dp[j,k,l] != 0:
              #  dp[i,j,k] = dp[j,k,l] + 1
              #else:
              #  dp[i,j,k] = 3
              dp[i,j,k] = max(dp[j,k,l]+1, 3, dp[i,j,k])
              #print(dp[i,j,k],"Index i j k=", i,j,k,"Value i j k", x[i], x[j], x[k])
              
            elif x[k] <= x[i] and x[i]<= x[j]:
              #if dp[j,k,l] != 0:
              #  dp[i,j,k] = dp[j,k,l] + 1
              #else:
              #  dp[i,j,k] = 3
              dp[i,j,k] = max(dp[j,k,l]+1, 3, dp[i,j,k])
              #print(dp[i,j,k],"Index i j k=", i,j,k,"Value i j k", x[i], x[j], x[k])

            if tmp < dp[i,j,k]:
              tmp = dp[i,j,k]
  return tmp

def FindLongestStableArray(x):
  """
    INPUT
      x : input sequence
  """


  n = len(x)
  dp = np.zeros((n+1,n+1))

  x =[9999]+x

  tmp =0
  for i in range(0,4,1):
    for j in range(0,3,1):
      for k in range(0,2,1):
        if k<j<i:
          # update 
          if x[j] <= x[i] and x[i]<= x[k]:
            dp[i,j] = max(2, dp[j,k]+1)
          elif x[k] <= x[i] and x[i]<= x[j]:
            dp[i,j] = max(2, dp[j,k]+1)
          #else:
          #  dp[i,j] = 0 # max(dp[i,j-1], dp[i-1,j])
          if tmp < dp[i,j]:
              tmp = dp[i,j]

  for i in range(1,n+1,1):
    for j in range(1,n+1,1):
      for k in range(1,n+1,1):
        if k<j<i:
          # update 
          if x[j] <= x[i] and x[i]<= x[k]:
            dp[i,j] = max(dp[j,k]+1, dp[i,j],3)
          elif x[k] <= x[i] and x[i]<= x[j]:
            dp[i,j] = max(dp[j,k]+1, dp[i,j],3)
          # no update
          #else:
          #  dp[i,j] =   #max(dp[i,j-1], dp[i-1,j])

      if tmp < dp[i,j]:
        tmp = dp[i,j]

  #tmp = 0
  #for i in range(n+1):
  #  if tmp < dp[n,i]:
  #    tmp = dp[n,i]

  #print(dp)

  return tmp
  



if __name__ == "__main__":

  for x, correct_answer in zip(dataset_list, answerset_list):
    my_answer = FindLongestStableArray(x)
    #break
    if my_answer - correct_answer != 0:
      print("My Answer {} | Solution {}".format(my_answer, correct_answer))
    else:
      print("Pass!")

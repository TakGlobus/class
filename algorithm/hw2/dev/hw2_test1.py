import time
import numpy as np


#correct_answer = 3
#s = "traingz"
#t = "strongz"
#correct_answer = 4
#s = "aaadbbbba"
#t = "aaacbbbbc"

correct_answer=4
s='elephant'
t='elephantzzt'

#correct_answer = 14
#s = "sjpgzirqwuuhzttfxtqetsfncggealzdqwmxpyisulygnmmtfhzzkkiumvduocip"
#t = "naqihutusctsisjmziykrazehzymsocxoutwiszoabcxwgarfygduybidnzntfu"

#correct_answer= 11
#s="oijjgveresojcjmolkwmdicrhlcjafbifaxuweigdtrohkatddtzhgaemclwowgfiikxtwn"
#t="padztmkzdmwhmznfnhwfajaalirnwcuefwjkibual"

def my_solution(x,y):
  """
    Temp solution for HW2 DP
      x,y : string
  """
  stime = time.perf_counter()

  nx = len(x)
  ny = len(y)
  dp = np.zeros((nx+1, ny+1))
  dp_s = []
  update = False
  for ix in range(1,nx+1,1):
    for iy in range(1,ny+1,1):
        i = ix-1
        j = iy-1
        if x[i] == y[j] and x[i-1] != y[j-1]:
          if not update:
            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
            update = True
            print("tmp dp max {} | i = {} j = {}".format(dp[ix,iy], i,j))
          else:
            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])
            update = False
        elif x[i] == y[j] and x[i-1] == y[j-1]:
          if not update:
            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-2,iy-2]+1)
            update=True
          else:
            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-2,iy-2])
            update = False
            
          #dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy])
          #print("tmp dp max {} | i = {} j = {}".format(dp[ix,iy], i,j))
        else:
          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])
          update=False
           
        #if i == 38 and j == 3:
        #  print(x[i-2:i+1], y[j-2:j+1])
        #  print(dp[i,:j+1])
        #  print(max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1))
        #  print(max(dp[ix,iy-1], dp[ix-1,iy],dp[ix,iy-2], dp[ix-2,iy], dp[ix-2,iy-2]+1))
        #  stop

  etime = time.perf_counter()
  print(" My Answer = {}  | Correct Answer = {} ".format(np.max(dp), correct_answer))
  print(" Time = {}s ".format(etime-stime))
  #print("{}".format(np.argwhere(dp == np.max(dp))))
  print(dp)


if __name__ == "__main__":
  my_solution(s,t)

#    for iy in range(1,ny+1,1):
#        i = ix-1
#        j = iy-1
#        if x[i] == y[j]:
#          if x[i-1] != y[j-1]:
#            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
#          else:
#            if x[i-2] == y[j-2]:
#              dp[ix,iy] = max(dp[ix,iy-2], dp[ix-2,iy], dp[ix-2,iy-2]+1)
#            else:
#              dp[ix,iy] = max(dp[ix,iy-2], dp[ix-2,iy], dp[ix-2,iy-2])
#        else:
#          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy])

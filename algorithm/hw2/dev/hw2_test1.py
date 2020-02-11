import time
import numpy as np


#correct_answer = 3
#s = "traingz"
#t = "strongz"
#correct_answer = 4
#s = "aaadbbbba"
#t = "aaacbbbbc"

#correct_answer=4
#s='elephant'
#t='elephantt'
correct_answer=3
s='eleph'
t='elephphhhhhhhhhp'

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
  for ix in range(1,nx+1,1):
    updated = False
    for iy in range(1,ny+1,1):
        i = ix-1
        j = iy-1
        if x[i] == y[j] and x[i-1] != y[j-1]:
              dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
              #print("tmp dp max {} | i = {} j = {}".format(dp[ix,iy], i,j))
        elif x[i] == y[j] and x[i-1] == y[j-1]:
              dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-2,iy-2]+1)
        else:
          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])
           

  etime = time.perf_counter()
  print(" My Answer = {}  | Correct Answer = {} ".format(np.max(dp), correct_answer))
  print(" Time = {}s ".format(etime-stime))
  #print("{}".format(np.argwhere(dp == np.max(dp))))
  print(dp)


if __name__ == "__main__":
  my_solution(s,t)


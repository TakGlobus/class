import time
import numpy as np


correct_answer = 14
s = "sjpgzirqwuuhzttfxtqetsfncggealzdqwmxpyisulygnmmtfhzzkkiumvduocip"
t = "naqihutusctsisjmziykrazehzymsocxoutwiszoabcxwgarfygduybidnzntfu"


def my_solution(x,y):
  """
    Temp solution for HW2 DP
      x,y : string
  """
  stime = time.perf_counter()

  nx = len(x)
  ny = len(y)
  dp = np.zeros((nx+1, ny+1))
  skip_row = 0
  skip_col = 0
  for ix in range(1,nx,1):
    for iy in range(1,ny,1):
      if ix != skip_row and iy != skip_col:
        if x[ix-1] == y[iy-1]:
          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
          skip_row = ix+1
          skip_col = iy+1
        else:
          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy])
           
      else: 
        dp[ix,iy] = dp[ix-1,iy-1]

  etime = time.perf_counter()
  print(" My Answer = {}  | Correct Answer = {} ".format(np.max(dp), correct_answer))
  print(" Time = {}s ".format(etime-stime))


if __name__ == "__main__":
  my_solution(s,t)

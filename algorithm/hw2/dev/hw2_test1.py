import time
import numpy as np


correct_answer = 3
s = "traingz"
t = "strongz"

#correct_answer = 14
#s = "sjpgzirqwuuhzttfxtqetsfncggealzdqwmxpyisulygnmmtfhzzkkiumvduocip"
#t = "naqihutusctsisjmziykrazehzymsocxoutwiszoabcxwgarfygduybidnzntfu"
SKIP=-9999

def my_solution(x,y):
  """
    Temp solution for HW2 DP
      x,y : string
  """
  stime = time.perf_counter()

  nx = len(x)
  ny = len(y)
  dp = np.zeros((nx+1, ny+1))
  for ix in range(1,nx+1,1):
    for iy in range(1,ny+1,1):
        if x[ix-1] == y[iy-1]:
          if x[ix-2] != y[iy-2]:
            dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
          else:
            if ix >=3 and iy >= 3:
              if x[ix-3] == y[ix-3]:
                dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-2,iy-2]+1)
              else:
                print(ix,iy,x[ix-1], y[iy-1])
                dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])
            else:
                dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])

        else:
          dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy])
           

  etime = time.perf_counter()
  print(" My Answer = {}  | Correct Answer = {} ".format(np.max(dp), correct_answer))
  print(" Time = {}s ".format(etime-stime))
  print("{}".format(np.argwhere(dp == np.max(dp))))
  print(dp)


if __name__ == "__main__":
  my_solution(s,t)

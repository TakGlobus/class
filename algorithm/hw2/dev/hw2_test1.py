import time
import numpy as np


#correct_answer = 3
#s = "traingz"
#t = "strongz"
#correct_answer = 4
#s = "aaadbbbba"
#t = "aaacbbbbc"

#correct_answer=2
#s='elep'
#t='elepppp'
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

#correct_answer=20
#s="yawtfuuyisvllkyifiqvuqbrtjbvahejzjhynijyxzofbqodbpzpnxbevkbapqszmasarbjvttkjkelhokiegd"
#t="zkpowopmvtgvixytcsfocymffbrkpknvuvfnrjuvfogytwbxeaxgpjislqhmuzcfhilgsafnrldteitffzyjfeof"


# -problem: 10
#correct_answer=14
#s="foyzyzlljxgjqqvwiuqaoqehbmgrehpyupvwnyqlaqpgmomnootyoajkgndforsyoeh"
#t="yfzchfonlqwbdzpiqiyfvaawrkmrhabakzplccutnxyokrhbtnjb"

# -problem: 17
# correct_answer: 15
# s: "txyozstumnseldqomgnywmkcccgbtuoupeavoqearxkcw"
# t: "tyoeuncrlvwzvfpeihnzzpsndtmzsbegppuijodjmhbutkbucatkubekxpobsnzqwumndayulcbhflhqljomb"

# -problem: 60
# correct_answer: 17
# s: "dljnzpijrpqpefmxdfmajbrvrbkwesqnuswamlfwnfehotmombiirpliojjxfvmih"
# t: "lazriakdbjrgotprbrmnwlluouniyrqpoaxyavyuylvytwkicxrsjlsqbpuphtqqxaimpjcbpq"

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
  for iy in range(1,ny+1,1):
    if x[0] == y[iy-1]:
      dp[1,iy] = 1
    else:
      dp[1,iy] = max(dp[1,iy-1], dp[0,iy], dp[0,iy-1])
  for ix in range(1,nx+1,1):
    if x[ix-1] == y[0]:
      dp[ix,1] = 1
    else:
      dp[ix,1] = max(dp[ix-1,0], dp[ix,1], dp[ix-1,0])


  for ix in range(2,nx+1,1):
    for iy in range(2,ny+1,1):
       i = ix-1
       j = iy-1
       if dp[ix-1,iy-1] - dp[ix-2,iy-2] == 0:
         if x[i] == y[j] and x[i-1] != y[j-1]:
           dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1]+1)
           print("tmp dp max {} | i = {} j = {}".format(dp[ix,iy], i,j))
         elif x[i] == y[j] and x[i-1] == y[j-1]:
           dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-2,iy-2]+1)
         else:
           dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])
       else:
         dp[ix,iy] = max(dp[ix,iy-1], dp[ix-1,iy], dp[ix-1,iy-1])

      

  etime = time.perf_counter()
  print(" My Answer = {}  | Correct Answer = {} ".format(np.max(dp), correct_answer))
  print(" Time = {}s ".format(etime-stime))
  #print("{}".format(np.argwhere(dp == np.max(dp))))
  print(dp)


if __name__ == "__main__":
  my_solution(s,t)


#
# ExtraHW
# 
import os
import itertools
import numpy as np

#correct_answer=5922
#r=[4,64,25,3,9,15,85,69,53,66,65,90,42,21,8,97,30,11,91,77,92,52,99,91,47,38,9,38,23,65,18,35,100,12,25,39,38,83,96,80,24,79,72,61,34,69,15,69,23,55,30,22,10,73,54,17,22,25,12,32,42,18,59,78,29,54,22,40,27,90,50,46,91,100,100,13,49,21,57,65,95,12,96,76,26,3,45,100,12,72,71,49,50]
#g=[7,23,27,37,78,45,18,46,54,32,12,12,84,90,5,29,96,29,12,22,79,87,34,45,24,66,52,22,56,53,6,1,100,3,46,82,66,42,99,12,74,71,67,35,78,5,54,78,15,37,53,40,72,82,78,69,95,9,29,86,76,82,42,63,47,65,39,4,45,79,23,47,5,74,65,9,70,49,86,56,99,37,52,18,86,38,2,84,7,62,35,34,56]
#b=[11,95,63,25,41,94,37,20,71,38,93,52,38,92,85,8,8,70,84,67,25,23,88,95,8,18,83,14,46,47,71,40,49,19,53,53,98,20,21,84,93,100,99,14,13,9,28,45,38,58,90,45,80,23,73,82,71,27,49,18,12,65,98,74,81,93,86,38,12,15,47,72,5,96,56,79,63,44,57,51,33,79,37,44,26,11,98,14,11,95,91,26,44]
correct_answer= 2947
r=[96,3,53,51,17,30,72,80,3,18,76,80,78,89,30,47,56,41,72,98,45,73,8,40,7,48,75,25,98,1,30,67,89,50,17,99,53,6,32,1,51,70,29,47,47]
g=[4,75,55,25,65,12,85,75,80,22,31,37,69,24,1,90,58,46,96,57,100,100,27,78,28,59,87,65,20,71,18,29,48,83,46,67,30,80,61,54,25,12,72,15,29]
b=[89,93,90,75,4,72,60,55,86,87,79,56,72,20,60,96,66,48,25,6,81,13,25,55,40,30,13,7,11,65,36,76,10,91,94,25,1,8,54,29,26,40,73,71,70]

#int FindOptimalColoringWeight(const std::vector<int>&  r, const std::vector<int>&  g, const std::vector<int>&  b)


def FindOptimalColoringWeight(r,g,b):
  """
    i)  Root u is incident on edges e0, e1, e2
    ii) Vertex Vi is incident on
        1 - edges ei, e_{2i+3}, e_{2i+4} if edges e_{2i+3}, e_{2i+4} are present edges
        2 - edge  ei o.w.
    
    weights are expressed as r_{ei} = r[i]
  """
  nedges = len(r) #+ len(g) + len(b) 
  nodes = nedges + 1
  colors = 3
  nchild = 2
  nonLeafIdx = (nodes-4)/2-1 # index larger than the number is leaf node
  #print(a)
  #nonLeafIdx = ((nedges-1)-4)/2 # index larger than the number is leaf node
  print(nonLeafIdx)
  print(np.sum(r) + np.sum(g)+np.sum(b))
  #nonLeafIdx = int(((nedges-1)-4)/2) # index larger than the number is leaf node
  dp = np.zeros((nodes,colors))

  # Root node
  #dp[0,4] = # sum up

  # Child nodes
  for i in range(nodes-2,-1,-1): 
    # root node has non-index vertex
    if i > nonLeafIdx:
      """Case: Leaf nodes
      """
      dp[i,:] = 0

    else:
      """Case: node with child nodes
      """
      print(i, 2*i+3,2*i+4)
      for k in range(colors):
        if k == 0: 
          # red is missing
          dp[i,k] = max(dp[2*i+3,1] + dp[2*i+4,2] + g[2*i+3] + b[2*i+4], 
                           dp[2*i+3,2] + dp[2*i+4,1] + b[2*i+3] + g[2*i+4])
          #dp[i,k] = max(dp[2*i+3,1] + dp[2*i+4,2] + g[i+1] + b[i], 
          #                 dp[2*i+3,2] + dp[2*i+4,1] + b[i+1] + g[i])
        elif k == 1: 
          # green is missing
          dp[i,k] = max(dp[2*i+3,0] + dp[2*i+4,2] + r[2*i+3] + b[2*i+4], 
                           dp[2*i+3,2] + dp[2*i+4,0] + b[2*i+3] + r[2*i+4])
          #dp[i,k] = max(dp[2*i+3,0] + dp[2*i+4,2] + r[i+1] + b[i], 
          #                 dp[2*i+3,2] + dp[2*i+4,0] + b[i+1] + r[i])
        elif k == 2: 
          # blue is missing
          dp[i,k] = max(dp[2*i+3,0] + dp[2*i+4,1] + r[2*i+3] + g[2*i+4], 
                           dp[2*i+3,1] + dp[2*i+4,0] + g[2*i+3] + r[2*i+4])
          #dp[i,k] = max(dp[2*i+3,0] + dp[2*i+4,1] + r[i+1] + g[i], 
          #                 dp[2*i+3,1] + dp[2*i+4,0] + g[i+1] + r[i])
  # check
  print(dp[0,:], dp[1,:], dp[2,:])
  for (i,j,k) in itertools.permutations([l for l in range(colors)]):
      print(dp[0,i]+dp[1,j]+dp[2,k])

  # final
  opt_weight = 0
  tmp_weights = []
  for (i,j,k) in itertools.permutations([l for l in range(colors)]):
      #tmp_weights.append(dp[i,i]+r[i]+dp[j,j]+g[j]+dp[k,k]+b[k])
      tmp_weights.append(dp[0,i]+r[i]+dp[1,j]+g[j]+dp[2,k]+b[k])
  opt_weight = np.max(tmp_weights)
  print(tmp_weights)
  

  return opt_weight

if __name__ == "__main__":
  my_answer = FindOptimalColoringWeight(r,g,b)  

  print(" ###  My Answer {} | Correct Answer {} ###".format(my_answer, correct_answer))


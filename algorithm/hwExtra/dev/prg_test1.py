#
# ExtraHW
# 
import os
import numpy as np

correct_answer=5922
r=[4,64,25,3,9,15,85,69,53,66,65,90,42,21,8,97,30,11,91,77,92,52,99,91,47,38,9,38,23,65,18,35,100,12,25,39,38,83,96,80,24,79,72,61,34,69,15,69,23,55,30,22,10,73,54,17,22,25,12,32,42,18,59,78,29,54,22,40,27,90,50,46,91,100,100,13,49,21,57,65,95,12,96,76,26,3,45,100,12,72,71,49,50]
g=[7,23,27,37,78,45,18,46,54,32,12,12,84,90,5,29,96,29,12,22,79,87,34,45,24,66,52,22,56,53,6,1,100,3,46,82,66,42,99,12,74,71,67,35,78,5,54,78,15,37,53,40,72,82,78,69,95,9,29,86,76,82,42,63,47,65,39,4,45,79,23,47,5,74,65,9,70,49,86,56,99,37,52,18,86,38,2,84,7,62,35,34,56]
b=[11,95,63,25,41,94,37,20,71,38,93,52,38,92,85,8,8,70,84,67,25,23,88,95,8,18,83,14,46,47,71,40,49,19,53,53,98,20,21,84,93,100,99,14,13,9,28,45,38,58,90,45,80,23,73,82,71,27,49,18,12,65,98,74,81,93,86,38,12,15,47,72,5,96,56,79,63,44,57,51,33,79,37,44,26,11,98,14,11,95,91,26,44]

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
  nonLeafIdx = ((nedges-1)-4)/2 # index larger than the number is leaf node
  print(nonLeafIdx)
  print(np.sum(r) + np.sum(g)+np.sum(b))
  nonLeafIdx = int(((nedges-1)-4)/2) # index larger than the number is leaf node
  dp = np.zeros((nodes+1,colors))

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
      for k in range(colors):
        if k == 0: 
          # red is missing
          dp[i,k] = max(dp[2*i-3,1] + dp[2*i-4,2] + g[2*i-1] + b[i], 
                           dp[2*i-3,2] + dp[2*i-4,1] + b[i-1] + g[i])
        elif k == 1: 
          # green is missing
          dp[i,k] = max(dp[2*i-3,0] + dp[2*i-4,2] + r[i-1] + b[i], 
                           dp[2*i-3,2] + dp[2*i-4,0] + b[i-1] + r[i])
        elif k == 2: 
          # blue is missing
          dp[i,k] = max(dp[2*i-3,0] + dp[2*i-4,1] + r[i-1] + g[i], 
                           dp[2*i-3,1] + dp[2*i-4,0] + g[i-1] + r[i])

  # final
  opt_weight = 0
  for i in range(nodes-2,-1,-1): 
      opt_weight = max([ dp[i,k] for k in range(colors)])
  for k in range(3):
    opt_weight += dp[0,k]

  return opt_weight

if __name__ == "__main__":
  my_answer = FindOptimalColoringWeight(r,g,b)  

  print(" ###  My Answer {} | Correct Answer {} ###".format(my_answer, correct_answer))


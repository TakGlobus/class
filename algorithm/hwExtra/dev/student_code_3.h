///////////////////////////////////////////////////////////////////////////////
// You need to
//    1. Read the programming assignment in homework #3.
//    2. Implement function GetStudentName.
//    3. Implement function FindOptimalColoringWeight.
//    4. Compile your code as explained in the PDF file.
//    5. Run the executable.
//    6. Test and debug your code.
//    7. Submit your code ("student_code_3.h") and results ("solution_3.dat")
//       via Canvas.
///////////////////////////////////////////////////////////////////////////////

//required libraries
#include <string>
#include <vector>

//you can include standard C++ libraries here
#include <queue>
#include <algorithm>
#include <functional>
#include <iostream> // for debug

// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name
   your_name.assign("Takuya Kurihana");
}

int FindOptimalColoringWeight(const std::vector<int>&  r, const std::vector<int>&  g, const std::vector<int>&  b)
{

  // Const
  const int nedges = r.size(); 
  const int nodes  = nedges+1; 
  const int colors = 3;
  const int nonLeafIdx = (nodes-4)/2 - 1;

  // Vector
  // 2d dp array initialized by 0
  std::vector<std::vector<int>> dp(nodes,std::vector<int>(colors,0));
  //
  //----------------------------------------------------------------- 
  // ! Compute DP Table !
  //----------------------------------------------------------------- 
  //
  // Child nodes
  for(int i=nodes-2;i>-1;--i){
    if (i > nonLeafIdx){
      for(int k=0; k<colors; k++){
      // DP for Leaf nodes
        dp[i][k] = 0;
      }
    }else{
      // DP for non-Leaf nodes
        for(int k=0; k<colors; k++){
          if (k == 0){
            dp[i][k] = std::max(
              {dp[2*i+3][1] + dp[2*i+4][2] + g[2*i+3] + b[2*i+4],
              dp[2*i+3][2] + dp[2*i+4][1] + b[2*i+3] + g[2*i+4]}
            );
          } else if (k == 1){
            dp[i][k] = std::max(
              {dp[2*i+3][0] + dp[2*i+4][2] + r[2*i+3] + b[2*i+4],
              dp[2*i+3][2] + dp[2*i+4][0] + b[2*i+3] + r[2*i+4]}
            );
          } else if (k == 2){
            dp[i][k] = std::max(
              {dp[2*i+3][0] + dp[2*i+4][1] + r[2*i+3] + g[2*i+4],
              dp[2*i+3][1] + dp[2*i+4][0] + g[2*i+3] + r[2*i+4]}
            );
          }
      }// k color loop
    }
  } // i loop


  // Root node
  //TODO: Rewrite below poor man approach
  int opt_weight = std::max({
    dp[0][0]+r[0]+dp[1][1]+g[1]+dp[2][2]+b[2],
    dp[0][0]+r[0]+dp[1][2]+b[1]+dp[2][1]+g[2],
    dp[0][1]+g[0]+dp[1][0]+r[1]+dp[2][2]+b[2],
    dp[0][1]+g[0]+dp[1][2]+b[1]+dp[2][0]+r[2],
    dp[0][2]+b[0]+dp[1][0]+r[1]+dp[2][1]+g[2],
    dp[0][2]+b[0]+dp[1][1]+g[1]+dp[2][0]+r[2],
  });
  return opt_weight /* your answer */;
}

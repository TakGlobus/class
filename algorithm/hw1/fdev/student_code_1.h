///////////////////////////////////////////////////////////////////////////////
// You need to
//    1. Read the programming assignment in homework #1.
//    2. Implement function GetStudentName.
//    3. Implement function FindOptimalSubsequenceValue.
//    4. Compile your code as explained in the PDF file.
//    5. Run the executable.
//    6. Test and debug your code.
//    7. Submit your code ("student_code_1.h") and results ("solution_1.dat")
//       via Canvas.
///////////////////////////////////////////////////////////////////////////////

//required libraries
#include <string>
#include <vector>

//you can include standard C++ libraries here
#include <queue>
#include <iostream>
#include <algorithm>
#include <array>
#include <list>

// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name
   //your_name.assign("Firstname Lastname");
   your_name.assign("Takuya Kurihana");
}

int FindOptimalSubsequenceValue(const std::vector<int>&  a)
{
  //  Input
  //      a : example darray

  // Const
  const int n  = a.size() ;
  
  // Array
  // gen dp vector with 0 initialize
  std::vector<int> dp(n+1,0);
  
  //---------------------------------------------
  // Compute DP table
  //---------------------------------------------

  for(int i=1; i<n+1; i++){
    for(int j=1; j<n; j++){
      if(j < i){
        int tmp = a[i-1] * a[j-1];
        if( dp[j-1] + tmp > dp[i-1] ){
          // Update!          
          dp[i] = std:: max({ dp[j-1] + tmp,dp[i]});
        } else{
          dp[i] = std:: max({ dp[i-1], dp[i]});
        } // if-else
      } // if j < i
    } //j
  } //i
  
  // get max val 
  std::vector<int>::iterator overall_max; // store max
  overall_max = std:: max_element(dp.begin(), dp.end());
  
  //return 0 /* your answer */;
  return  *overall_max /* your answer */;
}

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
  //      a : example array
  //
  int n;
  int nk;
  int overall_max;
  int overall_k;
  int tmp_max;
  int tmp_k;
  n  = sizeof(table)/sizeof(*a) 
  nk = div(n,2)
  
  // /
  int dp[n+1][n+1][nk+1];
  int array[n+1][n+1]


   return 0 /* your answer */;
}

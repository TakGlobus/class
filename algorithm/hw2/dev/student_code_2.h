///////////////////////////////////////////////////////////////////////////////
// You need to
//    1. Read the programming assignment in homework #2.
//    2. Implement function GetStudentName.
//    3. Implement function FindLCLS.
//    4. Compile your code as explained in the PDF file.
//    5. Run the executable.
//    6. Test and debug your code.
//    7. Submit your code ("student_code_2.h") and results ("solution_2.dat")
//       via Canvas.
///////////////////////////////////////////////////////////////////////////////

//required libraries
#include <string>
#include <vector>

//you can include standard C++ libraries here
#include <queue>
#include <algorithm>
#include <iostream> // for debug

// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name
   //your_name.assign("Firstname Lastname");
   your_name.assign("Takuya Kurihana");
}

int FindLCLS(const std::string&  s, const std::string&  t)
{

// To allocate a one-dimensional vector M of length a, write
// std::vector<int> M(a);
//
// To allocate a two-dimensional table M of size a x b, write
//   std::vector<std::vector<int> > M(a);
//   for (int i = 0; i < a; i++)
//      M[i].resize(b);
// To access element (i, j) in the table, write M[i][j].
// Note that M[i, j] will not work! (M[i, j] means something else in C++.)
//
// You may use functions std::max(a, b) and std::min(a, b) that return the maximum and minimum 
// of numbers a and b, respectively. However, don't write std::max(a, b, c) or std::min(a, b, c),
// unless you know what this means in C++.

  // Documentation by Tak
  // Input 
  //    s: example of 1d string array
  //    t: example of 1d string array

  // Const
  const int nx = s.size();
  const int ny = t.size();

  // Vector
  // 2d dp array initialized by 0
  std::vector<std::vector<int>>  dp(nx+1,std::vector<int>(ny+1, 0));
  //
  //-------------------------------------------------------
  // ! Compute DP Table !
  //-------------------------------------------------------
  //
  // case ix , iy <= 1
  for(int iy=1; iy<ny+1;iy++){
    if ( s[0] == t[iy-1] ){
      dp[1][iy] = 1;
    } else {
      dp[1][iy] = std::max({dp[1][iy-1], dp[0][iy], dp[0][iy-1]}) ;
    }
  }
  for(int ix=1; ix<nx+1;ix++){
    if ( s[ix-1] == t[0] ){
      dp[ix][1] = 1;
    } else {
      dp[ix][1] = std::max({dp[ix][0], dp[ix-1][1], dp[ix-1][0]}) ;
    }
  }

  // case ix,iy >=2
  for(int ix=2; ix<nx+1; ix++){
    for(int iy=2; iy<ny+1; iy++){
      // psuedo pointer to avoid index confusion
      int i = ix-1;
      int j = iy-1;
      if ( dp[ix-1][iy-1] - dp[ix-2][iy-2]  == 0 ){
        if ( (s[i] == t[j]) && (s[i-1] != t[j-1]) ){
          dp[ix][iy] = std::max({dp[ix][iy-1], dp[ix-1][iy], dp[ix-1][iy-1]+1 }) ;
        } else if ((s[i] == t[j]) && (s[i-1] == t[j-1])){
          dp[ix][iy] = std::max({dp[ix][iy-1], dp[ix-1][iy], dp[ix-2][iy-2]+1 }) ;
        } else {
          dp[ix][iy] = std::max({dp[ix][iy-1], dp[ix-1][iy], dp[ix-1][iy-1]}) ;
        }
      } else{
        dp[ix][iy] = std::max({dp[ix][iy-1], dp[ix-1][iy], dp[ix-1][iy-1]}) ;
      }
    } //iy
  }  //ix

  // Get max dp
  int overall_max=0;
  for (int i=0; i<nx+1; i++){
    overall_max= std::max(overall_max, (int)*max_element(dp[i].begin(), dp[i].end()) );
  }
  
  return overall_max;
  //return 0 /* your answer */;
}

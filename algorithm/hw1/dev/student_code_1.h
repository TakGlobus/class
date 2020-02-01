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

  // Var 
  //int n;
  //int nk;
  int overall_max;
  int overall_k;
  int tmp_max;
  int tmp_k;

  // Const
  //n  = sizeof(a)/sizeof(*a) ;
  //const int n  = a.size() ;
  const int n  = 10000 ;
  //TODO use div correctly for nk = div(n,2);
  const int nk = n/2;   // integer so that 10/3 = 3 not 10.333
  std::cout<< n;
  
  // Array - Vector
  std::vector<int> loop(1000,0);
  std::vector<int> case1(1000,0);
  std::vector<int> case2(1000,0);
  
  int dp[n+1][n+1][nk+1];
  int darray[n+1][n+1];
  //std::array<std::array<std::array<int,n+1>,n+1>,nk+1> dp;
  //std::array<std::array<int,n+1>,n+1> darray;

  // Initialization
  for(int i=0; i<=n+1; ++i){
    for(int j=0; j<=n+1; ++j){
      for(int k=0; k<=nk+1; ++k){
          dp[i][j][k] = 0;
      }
    }
  };
  for(int i=0; i<=n+1; ++i){
    for(int j=0; j<=n+1; ++j){
          darray[i][j] = 0;
    }
  };

  // ------------------------------------------------------
  // Construct darray stored multiplication results
  // ------------------------------------------------------
  //
  for(int i=0; i<=n+1; ++i){
    for(int j=0; j<=n+1; ++j){
      if( i > j){
        if( (i >= 1) and (j >=1)){
          darray[i][j] = a[i-1] * a[j-1] ;
        }
      }
    }
  };

  // ------------------------------------------------------
  // Update DP table recursively
  // ------------------------------------------------------
  //
  
  overall_max = 0;
  overall_k   = 0;
  tmp_max     = 0;
  tmp_k       = 0;

  for(int i=1; i<=n+1; ++i){
    for(int j=1; j<=n+1; ++j){
      for(int k=1; k<=nk+1; ++k){
        if(i > j){
          if( k <= i/2){
          
            if( darray[i][j] > 0){
              // gen loop
              for(int jj=0; jj<=j-1; ++jj){
                loop.push_back(dp[j-1][jj][k-1]);
              };
              loop.push_back(0); // add 0 not to make blank darray
              
              // ---- First update ----
              int z = *max_element(std::begin(loop), std::end(loop));
              dp[i][j][k] = z + darray[i][j];
              
              loop.clear();

              //
            } else{
              // gen case1 and case2
              for(int jj=0; jj<=j+1; ++jj){
                case1.push_back(dp[j-1][jj][k]);
              };
              for(int jj=0; jj<=j; ++jj){
                case1.push_back(dp[j][jj][k]);
              };

              // ---- Second non-update ----
              int case1_max = *max_element(std::begin(case1), std::end(case1));
              int case2_max = *max_element(std::begin(case2), std::end(case2));
              dp[i][j][k] = std::max({case1_max, case2_max,0});

              case1.clear();
              case2.clear();
              
            } // if else for darray value is positive or negative

            // Store temporarily max value and index
            if(dp[i][j][k] > tmp_max ){ 
                tmp_max = dp[i][j][k];
                tmp_k   = k;
            }

          } // k div
        } // if i > j
      }
    }
  }

  // Compute overall score
  overall_max = tmp_max;
  overall_k = tmp_k;

   //return 0 /* your answer */;
   return  overall_max /* your answer */;
}

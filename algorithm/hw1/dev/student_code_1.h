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

  // Var 
  //int n;
  //int nk;
  int overall_max;
  int overall_k;
  int tmp_max;
  int tmp_k;

  // Const
  //n  = sizeof(a)/sizeof(*a) ;
  const int n  = a.size() ;
  //TODO use div correctly for nk = div(n,2);
  const int nk = n/2;   // integer so that 10/3 = 3 not 10.333
  
  // Array
  int loop[n*n+1];
  int case1[n+1];
  int case2[n+1];
  
  // Dynamic Array to avoid seg. fault
  //    1. int dp[n+1][n+1][nk+1];
  //    2. int darray[n+1][n+1];
  int ***dp = new int**[n+1]; 
  for(int i=0; i<n+1; i++){
    dp[i] = new int*[n+1];
    for(int j=0; j<n+1; j++){
      dp[i][j] = new int[nk];
    }
  }
  int **darray = new int*[n+1]; 
  for(int i=0; i<n+1; i++){
    darray[i] = new int[n+1];
  }

  // Initialization
  for(int i=0; i<n+1; i++){
    for(int j=0; j<n+1; j++){
      for(int k=0; k<nk+1; k++){
          dp[i][j][k] = 0;
      }
    }
  }
  for(int i=0; i<n+1; i++){
    for(int j=0; j<n+1; j++){
          darray[i][j] = 0;
    }
  }

  // ------------------------------------------------------
  // Construct darray stored multiplication results
  // ------------------------------------------------------
  //
  for(int i=0; i<n+1; i++){
    for(int j=0; j<n+1; j++){
      if( i > j){
        if( (i >= 1) and (j >=1)){
          darray[i][j] = a[i-1] * a[j-1] ;
        }
      }
    }
  }

  // ------------------------------------------------------
  // Update DP table recursively
  // ------------------------------------------------------
  //
  
  overall_max = 0;
  overall_k   = 0;
  tmp_max     = 0;
  tmp_k       = 0;

  for(int i=1; i<n+1; i++){
    for(int j=1; j<n+1; j++){
      for(int k=1; k<nk+1; k++){
        if(i > j){
          if( k <= i/2){
          
            if( darray[i][j] > 0){
              // initialize
              for(int l=0; l<n*n+1; l++){
                loop[l] = 0;
              }

              // gen loop
              int ij=0;
              for(int ii=0; ii<j; ii++){
                for(int jj=0; jj<j; jj++){
                  loop[ij] = dp[ii][jj][k-1];
                  ij+=1;
                }
              }
              
              // ---- First case ----
              int* z; 
              z = std :: max_element(loop, loop+n*n+1);

              int tmp1 = 0;
              tmp1 = *z + darray[i][j];

              // ---- Second case ----
              // initialize
              for(int l=0; l<n*n+1; l++){
                loop[l] = 0;
              }
              // gen loop
              for(int jj=0; jj<j; jj++){
                  loop[jj] = dp[j-1][jj][k];
              }
              int* tmp2; 
              tmp2 = std:: max_element(loop, loop+n*n+1);
              
              // ---- Third case ----
              // initialize
              for(int l=0; l<n*n+1; l++){
                loop[l] = 0;
              }
              // gen loop
              for(int jj=0; jj<j; jj++){
                  loop[jj] = dp[i][jj][k];
              }
              int* tmp3; 
              tmp3 = std:: max_element(loop, loop+n*n+1);

              // ---- Update ----
              //dp[i][j][k] = *z + darray[i][j];
              dp[i][j][k] = std::max({tmp1, *tmp2, *tmp3});

              //
              //
            } else{
              //
              //
              // initialize
              for(int l=0; l<n+1; l++){
                case1[l] = 0;
                case2[l] = 0;
              }

              // gen case1 and case2
              for(int jj=0; jj<j+1; jj++){
                case1[jj] = dp[j-1][jj][k];
              };
              for(int jj=0; jj<j-1; jj++){
                case2[jj] = dp[i][jj][k];
              };

              // ---- Second non-update ----
              int* case1_max; 
              case1_max = std:: max_element(case1, case1+n+1);
              int* case2_max; 
              case2_max = std:: max_element(case2, case2+n+1);
              dp[i][j][k] = std::max({*case1_max, *case2_max,0});

              
            } // if else for darray value is positive or negative

            // Store temporarily max value and index
            if(dp[i][j][k] > tmp_max ){ 
                //std:: cout << " Update dp i j k ==";
                //std:: cout <<  dp[i][j][k] << " " ;
                //std:: cout <<  i << " " ;
                //std:: cout <<  j << " " ;
                //std:: cout <<  k << std:: endl;
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

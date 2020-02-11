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

// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name
   your_name.assign("Firstname Lastname");
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

   return 0 /* your answer */;
}

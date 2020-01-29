////////////////////////////////////////////////////////////////////////////
// DO NOT EDIT THIS FILE
//

#include <string>
#include <vector>
#include "test_framework.h"
#include "student_code_1.h"

const char* inputFilename = "problem_set_1.in";
const char* outputFilename = "solution_1.dat";

const char* strNotice = "##################################\n"
                        "# Do not edit this file!\n"
                        "##################################\n";

constexpr int problem_set_id = 1;

struct ProblemN1 : public TestFramework::BasicProblem
{
   std::vector<int> a;
};

int main(int argc, char *argv[])
{
   using namespace TestFramework;

   static_assert (GetTestFrameworkVersion () == 6, "TestFramework version 6 is required. Please, update test_framework.h.");
   ExitIfConditionFails((argc == 1) || (argc == 2), "This program takes at most one parameter.");

   std::cout << std::endl << "Problem set #" << problem_set_id << ". ";

   ProblemSetHeader header;
   RecordAdapter<ProblemSetHeader> psAdapter(header);
   AddDefaultProblemSetColumns(psAdapter);

   std::vector<ProblemN1> problems;
   TableAdapter<ProblemN1> prAdapter(problems);
   AddDefaultProblemColumns(prAdapter);

   AddColumn<ProblemN1>(prAdapter, "a", &ProblemN1::a);

   BasicYamlParser parser(dynamic_cast<ITable*>(&psAdapter), dynamic_cast<ITable*>(&prAdapter));
   parser.ParseFile(inputFilename, true);

   GetStudentName(header.student_name);

   PreprocessProblemSet(problem_set_id, problems, header);

   bool isDebugMode = (argc == 2);

   if (!isDebugMode)
   {
      for (int i = 0; i < header.problem_count; i++)
      {
         ProblemN1& theProblem = problems[i];
         theProblem.student_answer = FindOptimalSubsequenceValue(theProblem.a);
      }

      ProcessResults(problems, header);

      TableAdapter<ProblemN1> prOutAdapter(problems);
      AddDefaultProblemColumnsForOutput(prOutAdapter);

      WriteTableToFile(outputFilename, &prOutAdapter, &psAdapter, false, strNotice);
      std::cout << "Don't forget to submit your source code and file '" << outputFilename << "' via Canvas.";
      std::cout << std::endl << std::endl;
   }
   else
   {
      int problemToSolve = atoi(argv[1]);

      ExitIfConditionFails(problemToSolve != 0,
         "Invalid parameter. Please, specify the number of the problem you want to solve. The number of the first problem is 1.");

      std::cout << "Solving problem #" << problemToSolve << "." << std::endl;

      ExitIfConditionFails(problemToSolve <= header.problem_count, "The problem you specified does not exist.");
      ProblemN1& theProblem = problems[problemToSolve - 1];
      theProblem.student_answer = FindOptimalSubsequenceValue(theProblem.a);

      if (problemToSolve <= header.test_problems)
      {
            std::cout << "Correct answer: " << theProblem.correct_answer << "." << std::endl;
      }

      std::cout << "Your answer: " << theProblem.student_answer << "." << std::endl;
      std::cout << std::endl;
   }

   return 0;
}
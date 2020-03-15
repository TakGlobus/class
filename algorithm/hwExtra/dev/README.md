### HW3


#### How to compile
- Orthodox compile method  
  `g++ -std=c++11 problem_solver_1.cpp -g -o results`  
  
  
- Fast compile method: Very fast!!  
  `clang++ -std=c++11 -O3 -mtune=native -march=native problem_solver_3.cpp -g -o results_fast`  

#### How to debug with 
Website : [Qita:  Debug gdb in C/C++ -Japanese-](https://qiita.com/Aqua_ix/items/2e9d4fd2eb0fc4db22cb)  

#### How to use fast option in C++  
Website : [Qita: Magics to make your C++ code faster](https://qiita.com/kotauchisunsun/items/84e01c6fb621fcc1a647)

##### Procedure  
- `gdb results core`    
  Show debug result and identify position

- `backtrace`  
  More detailed information  

- `frame 1`  
  Show wihch method does have the error 

- `quit`   
  End of the debugging

#### For better code
- Modify computation for root node

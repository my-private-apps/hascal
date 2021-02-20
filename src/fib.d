
import std.stdio;



int fib (int n) {
if(n <= 2){return 1 ; }else {return fib(n-1)+fib(n-2) ; }
}

int main(string[] args){
  
auto nn = 4;

writeln(fib(nn));

return 0;}
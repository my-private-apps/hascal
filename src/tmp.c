
typedef char* string;
#include<stdbool.h>
#include<string.h>


int fib (int n) {
if(n <= 2){return 1 ; }else {return fib(n-1)+fib(n-2) ; }
}
    int main(int argc, char *argv[]){
  
int nn = 4;

printf("%d" , fib(nn)) ;

return 0;
 }
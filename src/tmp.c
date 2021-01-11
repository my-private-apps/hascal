
typedef char* string;
#include<stdbool.h>
#include<string.h>


#include <stdio.h>

#include <conio.h>

 


string ReadStr (void) {
string temp ;
scanf("%s",&temp);return temp ; }int ReadInt (void) {
int temp ;
scanf("%d",&temp);return temp ; }int Length (string s1) {return strlen(s1) ; }


 


bool isAlpha (char ch) {
if(ch >= 'a' || ch <= 'z'){return true ; }else {return false ; }
return false ; }bool isNumber (char ch) {
if(ch >= '0' || ch <= '9'){return true ; }else {return false ; }
return false ; }



    int main(int argc, char *argv[]){
  
printf("Hello world\n") ;

string x = "Hello";

printf("%d" , Length(x)) ;

return 0;
 }
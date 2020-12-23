typedef char* string;
#include<stdbool.h>

#include <stdio.h>

typedef char* string;
#include<stdbool.h>

#include <dir.h>

#include <stdlib.h>

#include <stdio.h>

#include <conio.h>



void ReadStr (string str) {gets(str);}void ReadInt (int a) {scanf("%d",&a);}void mkdir (string a) {mkdir("%s",a);}



    int main(int argc, char *argv[]){
  
char s [] = "abcdefgh" ;

ReadStr(s);

printf("%s" , s);

mkdir(s);

return 0;
 }
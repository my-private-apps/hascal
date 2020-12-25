# Hascal Syntax Example

### hello world :
```
use "hascal.core";
print("Hello World");
// or :
print "Hello World" ;
```
### variables :
```
var x = 1;
var str = "Hascal";
var pi = 3.14 ;
var testBool = true;
var ch = 'h';
```
or:
```
use "hascal.core";
var x : int = 1 ;
var str : string = "Hascal";
var pi : float = 3.14;
var testBool : bool testBool = true;
var ch : char = 'h';
```
### arrays:
```
var ages : int[4] = 12,13,14,15;
var strs : string[2] = "hello" , "bye" ;
var fls : float[3] = 1.0,1.1,1.3;
var bls : bool[3] = true , false,false;
var chs : char[6] = 'h','a','s','c','a','l'; 

var ages2 : int[3,3] = 1,2,3,4,5,6;
print(ages2[3,3]);//output : 6
```
### read values :
```
use "hascal.core";
var x = 0;
ReadInt(x);

var str = "";
ReadStr(str);
```
### comments :
```
// this is a single line comment

/*
  this is a multi line comment
*/

Comment "this is a comment";
```
### if...else :
```
use "hascal.core";
var x = 1;
if x== 1 then
  print("x==1");
else
  print("x!=1");
end;
```
### for loop :
```
use "hascal.core";
var x = 0;
for x=0 to 10 do
  print(x);
end;
```
### while loop :
```
use "hsacal.core";
var x = 1;
while x==1 do
  print("loop");
end;
```
### functions :
```
use "hascal.core"
function sayHello()
  print("hello");
end;

function ret() as string
  return "hello";
end;

function ret2(ss string) as string
  print(ss);
end;
```
### structs
```
use "hascal.core";

struct Student 
  var age : int;
  var name : string ;
end;

Student johnDoe = new Student ;
johnDoe.age = 36 ;
johnDoe.name = "john doe";
```
or :
```
use "hascal.core";

record Student 
  var age : int;
  var name : string ;
end;

Student johnDoe = new Student(36,"john doe") ;

print(johnDoe.age);//output : 36
```
### use modules:
```
use "your_module_name";
```
for use c header files :
```
ccode use "stdio.h";
```
### use C code in Hascal :
```
use "hascal.core";
ccode "printf(\"this is ccode in hascal\");";
```

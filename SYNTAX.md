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
var x : int ;
x = 1 ;
var str : string;
str = "Hascal";
var pi : float ;
pi = 3.14;
var testBool : bool;
testBool = true;
var ch : char;
ch = 'h';
```
### arrays:
```
array ages : int[4]{ 12,13,14,15};
array strs : string[2] { "hello" , "bye"} ;
array fls : float[3] { 1.0,1.1,1.3};
array bls : bool[3] {true , false,false};
array chs : char[6] {'h','a','s','c','a','l'}; 

var ages2 : int[3,3] { 1,2,3,4,5,6};
print(ages2[3,3]);//output : 6
```
### read values :
```
use "hascal.core";
var x = 0;
x = ReadInt();

var str = "";
str = ReadStr();

var fl = 0.0;
fl = ReadFloat();
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
if x == 1 {
  print("x==1");
}
else {
  print("x!=1");
}

```
### for loop :
```
use "hascal.core";
var x = 0;
for x = 0 to 10 {
  print(x);
}
```

or :
```
use "hascal.core";
var x = 0;
for x = 100 downto 1 {
  print(x);
}
```
### while loop :
```
use "hsacal.core";
var x = 1;
while x == 1 {
  print("loop");
}
```
### functions :
```
use "hascal.core"
function sayHello() {
  print("hello");
}

function ret() as string {
  return "hello";
}

function ret2(ss string) as string {
  print(ss);
}
```
### structs
```
struct Student {
  var name = "";
  var age = 0;
  
  function WhatIsYourName() {
    print("My name is ",name);
  }
  
}

var John = new Student;
John.name = "John";

John.WhatIsYourName() ; # or : John.WhatIsYourName ;
# output : My name is John
```

### use modules:
```
use "your_module_name";
```
for example :
```
use "hascal.core";
```

use local hascal module(library):
```
local use "mylib";
```

# Hascal
<b>HASCAL IS CURRENTLY IN DEVELOPMENT</b><br>
This repository contains the Hascal compiler, Hascal's Standard Libraries, tools, and documentation. 

Hascal is a statically typed programming language. \
You can Countribute to this repo anytime.



[Hascal Official Website](https://hascal.github.io)
## Hascal Features:
1. Cross Platform (Linux, Windows,MacOS,Web)
2. High Performane as fast as C (Hascal's main backend compiles to human readable C)
3. Simple syntax (combination of Pascal and ruby)
3. Fast & Powerful
4. Safe
5. Support System Programming
6. Support Functional Programming
7. Develop front-end with Hascal
8. C and JavaScript backends
9. Translation to C and JavaScript
## Get Started
On Windows : \
[Download Hascal for Windows](#)

On Linux : \
[Download Hascal for Linux](#)\
or :
```
sudo apt install hascal
```
\
On MacOS : \
[Download Hascal for MacOS](#)

## Examples
hello world :
```
use "hascal.core";
print("Hello World");
```
variables :
```
use "hascal.core";
int x = 1;
string str = "Hascal";
float pi = 3.14;
bool testBool = true;//or <bool testBool = false;>
char ch = 'h';
```
arrays:
```
int[] ages = 12,13,14,15;
string[] strs = "hello" , "bye" ;
float[] fls = 1.0,1.1,1.3;
bool[] bls = true , false,false;
char[] chs = 'h','a','s','c','a','l'; 

int[3,3] ages2 = 1,2,3,4,5,6;
print(ages2[3,3]);//output : 6
```
read values :
```
use "hascal.core";
int x = 0;
ReadInt("",x);

string str = "";
ReadStr("",str);
```
comments :
```
// this is a single line comment

/*
  this is a multi line comment
*/

Comment "this is a comment";
```
if...else :
```
use "hascal.core";
int x = 1;
if x== 1 then
  print("x==1");
else
  print("x!=1");
end;
```
for loop :
```
use "hascal.core";
int x = 0;
for x=0 to 10 do
  print(x);
end;
```
while loop :
```
use "hsacal.core";
int x = 1;
while x==1 do
  print("loop");
end;
```
functions :
```
use "hascal.core"
function sayHello();
  print("hello");
end;

function ret() as string;
  return "hello";
end;

function ret2(string ss)  as string;
  print(ss);
end;
```
use modules:
```
use "your_module_name";
```
use C code in Hascal :
```
use "hascal.core";
ccode "
printf("this is ccode in hascal");
";
```
## Standard Libraries
```
- hascal.core : main Hascal standard library
- hascal.math : a library for work with math
- hascal.string : a library for work with strings
- hascal.regex : a regex engine for Hascal
- hascal.hlm : create HLM packages
- hascal.convert : convert variables type
- hascal.TrEx : try/except library
- hascal.io : work with files and directories
- hascal.time : work with time and date
- hascal.micro : programming AVR micros and arduino boards (Comming Soon!)
- hascal.sqlite : work with sqlite databases
```
## Contributors
This project exists thanks to all the people who contribute. 

## License
The compiler and the standard library are licensed under the GNU general public license,
Please read the [License](https://github.com/hascal/hascal/blob/main/LICENSE) for more details.

Copyright © 2019-2020  Hascal Development Team, all rights reserved.


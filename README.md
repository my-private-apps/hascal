# Hascal
![draw](https://raw.githubusercontent.com/hascal/hascal/main/img/has.png)
<br>
<b>HASCAL IS CURRENTLY IN DEVELOPMENT</b><br>
This repository contains the Hascal compiler, Hascal's Standard Libraries, tools, and documentation.

[Hascal Official Website](https://hascal.github.io)
## Hascal Features:
1. Cross Platform (Linux, Windows,MacOS,Web)
2. High Performane
3. Fast & Powerful
4. Safe
5. System Programming
6. Support Functional Programming
...
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
bool testBool = true;//or bool testBool = false;
char ch = 'h';
```
read values :
```
use "hascal.core";
var x = 0;
ReadInt("",x);

var str = "";
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
var x = 1;
if x== 1 then
  print("x==1");
else
  print("x!=1");
end;
```
for loop :
```
use "hascal.core";
var x = 0;
for x=0 to 10 do
  print(x);
end;
```
while loop :
```
use "hsacal.core";
var x = 1;
while x==1 do
  print("loop");
end;
```
functions :
```
use "hascal.core"
function sayHello()
  print("hello");
end;

function ret() as string
  return "hello";
end;

function ret2(string ss)  as string
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

## Hascal VS C\C++
<img style="display:inline-block" width="482px" height="298px" src="https://raw.githubusercontent.com/hascal/hascal/main/img/hasca_what_is_your_name.png">
<img style="display:inline-block" width="482px" height="298px" src="https://raw.githubusercontent.com/hascal/hascal/main/img/c_what_is_your_name.png">

## Standard Libraries
```
- hascal.core : main Hascal standard library+
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


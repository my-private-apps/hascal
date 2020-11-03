# Hascal
This repository contains the Hascal compiler, Hascal's Standard Libraries, tools, and documentation.

## Examples
hello world :
```
use "hascal.core.h";
print "Hello World";
```
variables :
```
use "hascal.core.h";
var x = 1;
var str = "Hascal";
```
if...else :
```
use "hascal.core.h";
var x = 1;
if x== 1 then
  print "x==1";
else
  print "x!=1";
end;
```
for loop :
```
use "hascal.core.h";
var x = 0;
for x=0 to 10 do
  print x;
end;
```
while loop :
```
use "hsacal.core.h";
var x = 1;
while x==1 do
  print "loop";
end;
```
functions :
```
use "hascal.core.h"
function sayHello
  print "hello";
end;

function ret as str
  return "hello";
end;

function ret2 : var str = "" as str
  print str;
end;
```
use modules and c headers :
```
use "your_module_name";
```
use C code in Hascal :
```
use "hascal.core.h";
ccode "
printf("this is ccode in hascal");
";
```

## Contributors
This project exists thanks to all the people who contribute. 

## License
The compiler and the standard library are licensed under the GNU general public license,
Please read the [License](https://github.com/hascal/hascal/blob/main/LICENSE) for more details.

Copyright © 2019-2020  Hascal Development Team, all rights reserved.


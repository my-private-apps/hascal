# Hascal Documentation
Read the following content for learning Hascal Programming Language.

**Before you begin, you must have the Hascal compiler installed on your system**

[install Hascal](#)


## How to compile a Hascal code ?
For compile a program enter following command :
```
hascal <your_code.has>
```
if you want to compile your program to JavaScript enter following command:
```
hascal js <your_code.has>
```
## hello world
a hello world program in Hascal :
```
use "hascal.core";
print "Hello World";
```
**NOTE:** `use"hascal.core";` must be mentioned at the beginning of each program ,default functions are inside this library.

## Variables
Variables are like containers in which values can be inserted or changed.

variable defining :
```
var name : type ;
```
name : your variable name
type : your variable type

**Types :**
- int : an integer number
- string : a string literal
- bool : a boolean value(true or false)
- float : a decimal number

example :
```
var myvar : string ;
var my_var : int ;
var _myvar : float;

```

**NOTE:** names should not start with a number.
By compiling this code, you will receive an error :
```
var 6Apple : int;
```

## variable assignment
Do the following to give a value to the variable :
```
name = value ;
```

example :
```
var x : int;
x = 14 ;
```

You can not assign a value  to a variable as opposed to the original type ,this code have error :
```
var myInt : int;
myint = 1.1; # error
```

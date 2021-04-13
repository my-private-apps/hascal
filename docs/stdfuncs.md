# Hascal Standard Functions

## print(...)
Standard Hascal print function

example :
```
print("Hello World");
```
## ReadStr() : string
Read string values from user

example :
```
print("What's your name ?");
var name = ReadStr();
print("Hi,",name);
```

## ReadInt() : int
Read int values from user

example :
```
print("What's your age ?");
var name = ReadInt();
print("your age :",name);
```

## ReadChar() : char
Read a character from user

example :
```
print("char :",ReadChar());
```

## ReadBool() : bool
Read a bool values from user

example :
```
print("bool :",ReadBool());
```

## ReadFloat() : float
Read float values from user

example :
```
print("float :",ReadFloat());
```

## to_int(input:auto) : int
Convert values to int

example :
```
print(to_int("123456"));
```

## to_string(input:auto) : string
Convert values to string

example :
```
print(to_string(123));
```

## to_float(input:auto) : float
Convert values to float

example :
```
print(to_float("3.14"));
```

## RemoveFile(name:string)
Removes a file

example :
```
RemoveFile("todo.txt");
```

## CloseFile(file:File)
Closes a file

example :
```
var file = File("todo.txt","w");
CloseFile(f);
```

## ReadFromFile(file:File) : string
Reads a file and returns a string value

example:
```
var myfile = File("todo.txt","r");
print(ReadFromFile(myfile));
```

## WriteToFile(file:File,data:string)
Writes a string to a file

example :
```
var file = File("todo.txt","w");

WriteToFile(file,"1-test");
CloseFile(f);
```



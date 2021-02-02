# Input & Output

## Print values

You can print everything with just passing it to the `print` function:

```hascal
print("Hello World"); # String
print(1 + 1); # Integer
print(1.2); # Float
print(true); # Boolean
print('$'); # Character
```

## Read values from user

You can read any type of values from user with one of this functions:
- `ReadStr`
- `ReadInt`
- `ReadFloat`
- `ReadChar`

**NOTE:** You should import `hascal.core` library before using Read functions, with `use "hascal.core";`.

This is an example for `ReadInt` function:

```hascal
use "hascal.core";
var x = 0;
x = ReadInt();
```

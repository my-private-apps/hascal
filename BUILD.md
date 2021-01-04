# Build from source

Prequistes :
```
- python v3.8 or higher
- pyinstaller 
- a build of tcc compiler # see : https://bellard.org/tcc/
```

## Install Pyinstaller
Enter following command in your cmd :
```
pip install pyinstaller
```

if use Linux :
```
pip3 install pyinstaller
```

## TCC Compiler
Hascal for generate binary code use tcc you should put a version of tcc compiler in the folder of Hascal compiler.

## Build
For build Hascal enter following command in terminal :
```
pyinstaller hascal.py --onefile
```

Excutable file compiled in src/dist folder.

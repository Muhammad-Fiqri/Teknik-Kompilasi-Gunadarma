# Simple Compiler That Convert Infix to Postfix
Author: Muhammad Fiqri
Python Version: 3.12.4
Library Used:
- argparse
- os

This project is made as a task for compilation technic college subject
https://rps.gunadarma.ac.id/file/1678337194509_teknik_kompilasi_ak045335.pdf

version 2: now compiler accept triple operand infix operation
---
# How To Use

Make a file name .fiq extension which signify that it's a fiqri code and insert infix operation that ends with semicolon ";" on each line like this:
```
A+B;
B*A;
A/B*C-D;
```
save that file

run the fiqri code throught fiqri compiler by running this on your Command Prompt (make sure to be on the same directory as the code):
```
python fiqri_compiler.py filename.fiq
```

and then the compiler will output a new file called output.fiq with the source file like this:
```
AB+;
BA*;
AB/C*D-;
```

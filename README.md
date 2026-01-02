# Simple Compiler That Convert Infix to Postfix

Author: Muhammad Fiqri

Python Version: 3.12.4

Library Used:
- argparse
- os
- string
- pyinstaller (to build into an exe file)
- re

This project is made as a task for compilation technic college subject taught by Ms. Sulistyo Puspitodjat
https://rps.gunadarma.ac.id/file/1678337194509_teknik_kompilasi_ak045335.pdf
This project is a compiler that can convert infix to postfix.

version 5: according to my Lecturer Ms. Sulistyo Puspitodjati, my compiler still accept other wrong input like:
```
AB+ 
-AB
ab;;
```

When I checked with verbose mode, this is what it say:
```
AB+
```
Output:
```
Compiling: kode.fiq! with verbose mode: False
Error: tidak ada ; pada baris 1
```

```
-AB
```
Output:
```
Compiling: kode.fiq! with verbose mode: False
Error: tidak ada ; pada baris 1
```

```
ab;;
```
Output:
```
Compiling: kode.fiq! with verbose mode: False

ERROR! Pada line 1
Operand ke-2 tidak di temukan, hasil menjadi kosong!
Operand ke-1: ['a', 'b']
Operand ke-2: []
Operator: []
Hasil: []
```

It seems like lecturer want each input to be 100% similar to syntax of infix, therefore I will use a RegEx to check the input before being compiled:
```
^([A-Za-z0-9]|[\+\-\*\/])+;$
```
She said this thing is called a "Scanner" or some short, therefore I will apply it on version 5.
<hr>

# Language Represantation:
https://docs.google.com/document/d/1wDsrLG6YnahcNPYhHjhIGD6TDS_hMmYYSthpdU8KMGw/edit?usp=sharing

<hr>

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
python fiq_compiler.py filename.fiq
```

and then the compiler will output a new file called output.fiq with the source file like this:
```
AB+;
BA*;
AB/C*D-;
```
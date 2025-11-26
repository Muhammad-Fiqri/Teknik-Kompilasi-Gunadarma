# Simple Compiler That Convert Infix to Postfix

Author: Muhammad Fiqri

Python Version: 3.12.4

Library Used:
- argparse
- os
- string
- pyinstaller

This project is made as a task for compilation technic college subject
https://rps.gunadarma.ac.id/file/1678337194509_teknik_kompilasi_ak045335.pdf

version 4: compiler when getting input in already postfix format (AB+;) will still accept it and return ";", need to be fix.
apparently when I checked using verbose mode this is what it says:
```
Passed: File ditemukan
Passed: ektensi file benar .fiq
Baris 1:
AB+;
operand:A
operand:B
operator:+
EOL:;
Hasil:  []
```
the result/hasil list is empty, therefore to fix this I just need to give an error on the CLI when it's already EOL, but the 2nd operand is empty or the result is empty.
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
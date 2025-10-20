import argparse
import os
import string

def compile(filename,verbose_mode):
    check_if_file_exist(filename,verbose_mode)
    check_if_extension_correct(filename,verbose_mode)

    result_list = []
    with open(filename) as file:
        lines = file.readlines()
        line_count = 1
        for i in lines:
            line = i.strip() #remove \n on the end of each line
            if verbose_mode:
                print(f"Baris {line_count}:")
                print(line)
            
            check_if_each_line_end_with_semicolon(line,line_count)

            operator_list = ["+","-","*","/"]
            alphanumeric_list = list(string.ascii_letters + string.digits)

            tokens = list(line)
            operands1 = []
            operands2 = []
            operators = []
            result = []
            for token in tokens:
                #I need to find away that this thing run only when operands are fully scanned
                #Note 2: it does work now, but it only can accept 2 operands and then just go to the next line
                if len(operators) > 0 and len(operands1) > 0 and len(operands2) > 0 and (token == ";" or token in operator_list):
                    if verbose_mode:
                        print("=======================")
                        print("Initiating Result Making:")
                        print("Operands 1: ", operands1)
                        print("Operands 2: ", operands2)
                        print("Operator: ", operators)
                        print("=======================")
                    result.append(operands1.copy()) #if I dont use .copy() it will only link the array instead of hardcopy making the result lose it's operator
                    result.append(operands2.copy())
                    result.append(operators[0])
                    operands1.clear()
                    operands2.clear()
                    operators.clear()

                if token in operator_list:
                    if verbose_mode:
                        print(f"operator:{token}")
                    operators.append(token)
                if token in alphanumeric_list:
                    if verbose_mode:
                        print(f"operand:{token}")
                    
                    # if operators is empty that mean we scanning for 1st operand, if not, the 2nd operand
                    if len(operators) == 0:
                        operands1.append(token)
                    else:
                        operands2.append(token)
                if token == ";":
                    if verbose_mode:
                        print(f"EOL:{token}")
            
            if verbose_mode:
                print("Hasil: ",result)
            result_list.append(result)


            line_count += 1
            print()

    with open("output.fiq", "w") as file:
        for line in result_list:
            stringified_line = str(line)
            file.write(stringified_line+";\n")

def check_if_file_exist(filename,verbose_mode):
    isExist = os.path.exists(filename)

    if isExist:
        if verbose_mode:
            print("Passed: File ditemukan")
    else:
        print(f"Error: File {filename} tidak di temukan")
        exit()

def check_if_extension_correct(filename,verbose_mode):
    split_tup = os.path.splitext(filename)

    file_extenstion = split_tup[1]

    if file_extenstion != ".fiq":
        print("Error: ektensi kode harus berakhiran .fiq \nContoh: nama_kode.fiq")
        exit()
    else:
        if verbose_mode:
            print("Passed: ektensi file benar .fiq")

def check_if_each_line_end_with_semicolon(line,line_count):
    if not line.endswith(";"):
        print(f"Error: tidak ada ; pada baris {line_count}")
        exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Fiqri Compiler",
        description="A simple infix to postfix compiler.")
    parser.add_argument("filename", type=str, help="nama kode file yang ingin di compile")
    parser.add_argument("-v", "--verbose_mode", type=bool, default=False, help="mode verbose: jika aktif akan mengoutput seluruh proses satu-persatu, cocok untuk debugging, default: false")

    args = parser.parse_args()

    print(f"Compiling: {args.filename}! with verbose mode: {args.verbose_mode}")

    compile(args.filename,args.verbose_mode)
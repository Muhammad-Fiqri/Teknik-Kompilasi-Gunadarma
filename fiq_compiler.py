import argparse
import os
import string
from sys import exit
import re

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
            
            scanner(line,line_count,verbose_mode)
            check_if_each_line_end_with_semicolon(line,line_count)

            operator_list = ["+","-","*","/"]
            alphanumeric_list = list(string.ascii_letters + string.digits)

            tokens = list(line)
            operands1 = []
            operands2 = []
            operators = []
            result = []
            for token in tokens:
                #Append the 3rd+ operand and operator if result is already there
                if len(result) > 0 and len(operators) > 0 and len(operands2) > 0 and (token == ";" or token in operator_list):
                    if verbose_mode:
                        print("=======================")
                        print("3rd+ Operand Result Making")
                        print("Operator: ",operators)
                        print("Operand 2: ", operands2)
                        print("=======================")
                    result.append(operands2.copy())
                    result.append(operators[0])
                    operands2.clear()
                    operators.clear()

                #Append the 1st and 2nd operand and operator to the result list
                if len(operators) > 0 and len(operands1) > 0 and len(operands2) > 0 and (token == ";" or token in operator_list):
                    if verbose_mode:
                        print("=======================")
                        print("Initiating 1st Result Making:")
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
                    if check_if_2nd_operand_or_result_is_empty(operands2,result):
                        print()
                        print(f"\033[91mERROR! Pada line {line_count}\033[0m")
                        print("Operand ke-2 tidak di temukan, hasil menjadi kosong!")
                        print(f"Operand ke-1: {operands1}")
                        print(f"Operand ke-2: {operands2}")
                        print(f"Operator: {operators}")
                        print(f"Hasil: {result}")
                        exit()

                    if verbose_mode:
                        print(f"EOL:{token}")
            
            if verbose_mode:
                print("Hasil: ",result)
            result_list.append(result)


            line_count += 1
            print()

    convert_result_list_to_string(result_list)

#this function is a scanner that will check if each line follow the infix operation rules using Regular Expression just like the lecturer wanted
def scanner(line,line_count,verbose_mode):
    print("Scanning line: ",line)
    # Regular expression pattern for infix operations
    pattern = r'^([A-Za-z0-9]|[\+\-\*\/])+;$'
    match = re.match(pattern, line)
    if not match:
        print(f"\033[91mError: Line tidak sesuai format infix pada baris {line_count}\033[0m")
        exit()
    if match and verbose_mode:
        print("Passed: Line sesuai format infix")

def check_if_2nd_operand_or_result_is_empty(operands2,result):
    if len(operands2) == 0 and len(result) == 0:
        return True
    else:
        return False


def convert_result_list_to_string(result_list):
    with open("output.fiq", "w") as file:
        for line in result_list:
            #flatten each list (which is a line) in result_list
            flattened_list = []
            for item in line:
                if isinstance(item, list):
                    flattened_list.extend(item)
                else:
                    flattened_list.append(item)

            #turn the flattened list into a string and write it into output.fiq
            stringified_line = "".join(flattened_list)
            file.write(stringified_line+";\n")

def check_if_file_exist(filename,verbose_mode):
    isExist = os.path.exists(filename)

    if isExist:
        if verbose_mode:
            print("Passed: File ditemukan")
    else:
        print(f"\033[91mError: File {filename} tidak di temukan\033[0m")
        exit()

def check_if_extension_correct(filename,verbose_mode):
    split_tup = os.path.splitext(filename)

    file_extenstion = split_tup[1]

    if file_extenstion != ".fiq":
        print("\033[91mError: ektensi kode harus berakhiran .fiq \nContoh: nama_kode.fiq\033[0m")
        exit()
    else:
        if verbose_mode:
            print("Passed: ektensi file benar .fiq")


def check_if_each_line_end_with_semicolon(line,line_count):
    if not line.endswith(";"):
        print(f"\033[91mError: tidak ada ; pada baris {line_count}\033[0m")
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
import argparse
import os

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
            tokens = list(line)
            operands = []
            operators = []
            result = []
            for token in tokens:
                if token in operator_list:
                    if verbose_mode:
                        print(f"operator:{token}")
                    operators.append(token)
                if not token in operator_list and token != ";":
                    if verbose_mode:
                        print(f"operand:{token}")
                    operands.append(token)
                if len(operands) == 2:
                    result.append(operands[0])
                    result.append(operands[1])
                    result.append(operators[0])
                    operands.clear()
                    operators.clear()
            
            if verbose_mode:
                print("Hasil: ",result)
            result_list.append(result)


            line_count += 1
            print()

    with open("output.fiq", "w") as file:
        for line in result_list:
            stringified_line = "".join(line)
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
import os
import re

def filter_out_do(text: str) -> str:
    do_pattern = re.compile(r'don\'t\(\).*(?=do\(\))', re.M)
    matches = do_pattern.findall(text)
    result = text
    for m in matches:
        result = result.replace(m, '')
    return result

def filter_out_do2(text: str) -> str:
    tasks = text.split("do()")
    result: str = ""
    for task in tasks:
        inner_tasks = task.split("don't()")
        result = result + inner_tasks[0]
    return result

def multiply_all_text_entries(text: str) -> int:
    mul_pattern = re.compile(r'mul\((\d*),(\d*)\)')
    matches = mul_pattern.finditer(text)
    mul_sum: int = 0
    for m in matches:
        mul_sum = mul_sum + (int(m.group(1)) * int(m.group(2)))
    return mul_sum


def main():
    """Main function for day3"""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file = open(os.path.join(file_dir, 'dataset/day3.txt'), "r")
    text = file.read()
    print ("Sum of entries: {0}".format(multiply_all_text_entries(text)))
    do_text = filter_out_do2(text)
    multiplications = multiply_all_text_entries(do_text)
    print ("Sum of entries after do(): {0}".format(multiplications))
    print ("Day3 done!")

if __name__ == "__main__":
    main()
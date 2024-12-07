import os


def main():
    """Main function for day3"""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(file_dir, 'dataset/day3.txt')) as file:
        for line in file:
            row: str = line.rstrip()
            print(row)
    print ("Day3 done!")

if __name__ == "__main__":
    main()
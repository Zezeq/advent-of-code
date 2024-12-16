import os


def find_number_of_xmas(matrix: list[list]) -> int:
    result: int = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "X":
                result += find_number_of_xmas_from_x(matrix, i, j)
    return result

def find_number_of_xmas_from_x(matrix: list[list], x:int, y:int) -> int:
    count:int = 0
    # Search forward
    if (len(matrix[x]) - y > 3):
        if (matrix[x][y+1] == "M" and matrix[x][y+2] == "A" and matrix[x][y+3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x][y+1], matrix[x][y+2], matrix[x][y+3]))
            count += 1
    # Search right-down-diagonally
    if (len(matrix[x]) - y > 3 and len(matrix) - x > 3):
        if (matrix[x+1][y+1] == "M" and matrix[x+2][y+2] == "A" and matrix[x+3][y+3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x+1][y+1], matrix[x+2][y+2], matrix[x+3][y+3]))
            count += 1
    # Search downward
    if (len(matrix) - x > 3):
        if (matrix[x+1][y] == "M" and matrix[x+2][y] == "A" and matrix[x+3][y] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x+1][y], matrix[x+2][y], matrix[x+3][y]))
            count += 1
    # Search left-down-diagonally
    if (y > 2 and len(matrix) - x > 3):
        if (matrix[x+1][y-1] == "M" and matrix[x+2][y-2] == "A" and matrix[x+3][y-3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x+1][y-1], matrix[x+2][y-2], matrix[x+3][y-3]))
            count += 1
    # Search backward
    if (y > 2):
        if (matrix[x][y-1] == "M" and matrix[x][y-2] == "A" and matrix[x][y-3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x][y-1], matrix[x][y-2], matrix[x][y-3]))
            count += 1
    # Search left-up-diagonally
    if (y > 2 and x > 2):
        if (matrix[x-1][y-1] == "M" and matrix[x-2][y-2] == "A" and matrix[x-3][y-3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x-1][y-1], matrix[x-2][y-2], matrix[x-3][y-3]))
            count += 1
    # Search upward
    if (x > 2):
        if (matrix[x-1][y] == "M" and matrix[x-2][y] == "A" and matrix[x-3][y] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x-1][y], matrix[x-2][y], matrix[x-3][y]))
            count += 1
    # Search right-up-diagonally
    if (x > 2 and len(matrix[x]) - y > 3):
        if (matrix[x-1][y+1] == "M" and matrix[x-2][y+2] == "A" and matrix[x-3][y+3] == "S"):
            #print("{0}{1}{2}{3}".format(matrix[x][y], matrix[x-1][y+1], matrix[x-2][y+2], matrix[x-3][y+3]))
            count += 1
    return count

def find_number_of_word(matrix: list[list], word:str) -> int:
    directions: list[list] = [
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1]
    ]
    result: int = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            for direction in directions:
                dx:int = direction[0]
                dy:int = direction[1]
                chars = [
                    matrix[new_x][new_y] 
                    for i, unused in enumerate(word)
                    if is_in_bounds(matrix, new_x := x + i * dx, new_y := y + i * dy)
                ]
                if ''.join(map(str, chars)) == word:
                    result += 1
    return result

def is_in_bounds(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[x])

def main():
    """Main function for day4"""
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    text:str = ""
    word_search:list[list[str]] = list()
    with open(os.path.join(file_dir, 'dataset/day4.txt')) as file:
        for line in file:
            row:list[str] = list()
            for char in line:
                row.append(char)
            word_search.append(row)
    #Alternative 1
    print(find_number_of_xmas(word_search)) #2718
    # Alternative 2
    print(find_number_of_word(word_search, "XMAS"))
    print ("Day4 done!")

if __name__ == "__main__":
    main()
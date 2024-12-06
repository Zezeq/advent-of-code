import os


def calculate_similarity_score(left: list[int], right: list[int]) -> int:
    result: int = 0
    for item in left:
        result += (item * find_occurrences_in_list(item, right))
    return result

def find_occurrences_in_list(number: int, data: list[int]) -> int:
    return data.count(number)

def calculate_length(left: list[int], right: list[int]) -> int:
    result: int = 0
    for index, item in enumerate(left):
        result += abs(left[index]-right[index])
    return result

def split_dataset(dataset: str) -> list[int]:
    return list(map(int, dataset.split()))

def sort_array(numbers: list[int]) -> list[int]:
    """Sorts the array and returns it in ascending order"""
    return sorted(numbers)

def main():
    """Main function for day1"""
    list1: list[int] = []
    list2: list[int] = []
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(file_dir, 'dataset/day1.txt')) as file:
        for line in file:
            values = split_dataset(line.rstrip())
            list1.append(values[0])
            list2.append(values[1])
    list1 = sort_array(list1)
    list2 = sort_array(list2)
    print ("Total length is: {0}".format(calculate_length(list1, list2)))
    print ("Similarity score is: {0}".format(calculate_similarity_score(list1, list2)))

if __name__ == "__main__":
    main()
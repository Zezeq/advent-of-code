import os


def calculate_report_safety(report: str) -> bool:
    """Returns true if report is safe, false otherwise"""
    levels = get_levels(report)
    return validate_level_difference(levels) if is_sorted(levels) else False

def calculate_report_safety_with_dampener(report: str) -> bool:
    """Returns true if report is safe with dampener (removing one item still meets criteria), false otherwise"""
    if calculate_report_safety(report):
        return True
    levels = get_levels(report)
    pos = 0
    while pos < len(levels):
        dampened_numbers = levels.copy()
        dampened_numbers.pop(pos)
        if sorted(dampened_numbers) == dampened_numbers or sorted(dampened_numbers, reverse=True) == dampened_numbers:
            if validate_level_difference(dampened_numbers):
                return True
        pos += 1
    return False

def validate_level_difference(levels: list[int]) -> bool:
    """validates if the difference of the levels are within tolerance (maximum 3 minimum 1)"""
    pos = 1
    while pos < len(levels):
        value = abs(levels[pos] - levels[pos-1])
        if (value > 3 or value < 1):
            return False
        pos += 1
    return True

def is_sorted(numbers: list[int]) -> bool:
    """Returns true if the integer list is sorted, else false"""
    if sorted(numbers) == numbers or sorted(numbers, reverse=True) == numbers:
        return True
    return False

def get_levels(report: str) -> list[int]:
    return list(map(int, report.split()))

def main():
    """Main function for day2"""
    safety_number: int = 0
    safety_number_dampened: int = 0
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    with open(os.path.join(file_dir, 'dataset/day2.txt')) as file:
        for line in file:
            report: str = line.rstrip()
            if (calculate_report_safety(report)):
                safety_number += 1
            if (calculate_report_safety_with_dampener(report)):
                safety_number_dampened += 1
    print ("Safe reports: {0}".format(safety_number))
    print ("Safe reports dampened: {0}".format(safety_number_dampened))

if __name__ == "__main__":
    main()
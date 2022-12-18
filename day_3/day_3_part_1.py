
def test_get_priority():
    assert get_priority('p') == 16

def get_priority(input):
    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return 1 + priorities.find(input)

def test_find_duplicate_char():
    assert find_duplicate_char('vJrwpWtwJgWr','hcsFMMfFFhFp') == 'p'
    assert find_duplicate_char(
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg') == 'r'

def find_duplicate_char(string_1, string_2, string_3 = None):
    duplicates = set(string_1).intersection(set(string_2))
    if string_3 is not None:
        duplicates = set(string_3).intersection(duplicates)
    if len(duplicates) != 1:
        raise ValueError
    else:
        return duplicates.pop()

def test_split_in_half():
    assert split_in_half('vJrwpWtwJgWrhcsFMMfFFhFp') == ('vJrwpWtwJgWr','hcsFMMfFFhFp')

def split_in_half(input):
    middle = len(input) // 2
    return input[:middle], input[middle:]

def test_sum_of_priorities_of_duplicates():
    assert sum_of_priorities_of_duplicates('sample_data.txt') == 157   

def sum_of_priorities_of_duplicates(input_filename):

    priorities = []
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()

        # Iterate over the lines in the file
        for line in lines:
            #split into two strings
            string_1, string_2 = split_in_half(line.rstrip())
            duplicate_char = find_duplicate_char(string_1, string_2)
            priority = get_priority(duplicate_char)
            priorities.append(priority)


    total_score = sum(priorities)
    print(f'part 1: total score for input file {input_filename} is {total_score}') 
    return total_score

def test_sum_of_priorities_of_common_item_in_groups():
    assert sum_of_priorities_of_common_item_in_groups('sample_data.txt') == 70

def sum_of_priorities_of_common_item_in_groups(input_filename):
    priorities = []
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()

        # Iterate over the lines in the file
        subsets = [lines[i:i+3] for i in range(0, len(lines),3)]
        for subset in subsets:
            #split into two strings
            duplicate_char = find_duplicate_char(
                subset[0].rstrip(), 
                subset[1].rstrip(), 
                subset[2].rstrip())
            priority = get_priority(duplicate_char)
            priorities.append(priority)


    total_score = sum(priorities)
    print(f'part 2: total score for input file {input_filename} is {total_score}') 
    return total_score

if __name__ == '__main__':
    test_get_priority()
    test_find_duplicate_char()
    test_split_in_half()
    test_sum_of_priorities_of_duplicates()
    test_sum_of_priorities_of_common_item_in_groups()
    sum_of_priorities_of_duplicates('input_data.txt')
    sum_of_priorities_of_common_item_in_groups('input_data.txt')
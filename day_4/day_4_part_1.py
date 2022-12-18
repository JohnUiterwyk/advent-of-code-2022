
def test_count_fully_contained_pairs():
    assert count_fully_contained_pairs('sample_data.txt') == 4


def count_fully_contained_pairs(input_filename):
    # Open the file with the 'open' function, which returns a file object
    fully_contained_count = 0
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()
        for line in lines:
            pairs = line.rstrip().split(',')
            elf_1_min, elf_1_max = tuple(int(item) for item in tuple(pairs[0].split('-')))
            elf_2_min, elf_2_max = tuple(int(item) for item in tuple(pairs[1].split('-')))
            if any([
                elf_1_min >= elf_2_min and elf_1_max <= elf_2_max,
                elf_2_min >= elf_1_min and elf_2_max <= elf_1_max,
                elf_2_min <= elf_1_max and elf_2_max >= elf_1_max,
                elf_1_min <= elf_2_max and elf_1_max >= elf_2_max,
                ]):
                fully_contained_count = fully_contained_count + 1


    print(f'part 1: found {fully_contained_count} fully contained pairs in {input_filename} ') 
    return fully_contained_count

if __name__ == '__main__':
    test_count_fully_contained_pairs()
    count_fully_contained_pairs('input_data.txt')
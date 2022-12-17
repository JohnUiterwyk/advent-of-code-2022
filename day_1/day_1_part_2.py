def test_get_max_calories():
    input_filename = 'sample_data.txt'
    expected_result = 45000
    actual_result = get_max_calories(input_filename)
    assert actual_result == expected_result


def get_max_calories(input_filename):

    elves = []
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()
        current_elf = 0
        # Iterate over the lines in the file
        for line in lines:
            # Process the line, such as by printing it to the console
            if(len(line.rstrip()) == 0):
                # update max with current elf if greater
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf = current_elf + int(line.rstrip())
        elves.append(current_elf)
    elves.sort(reverse=True)
    top_3_sum = sum(elves[:3])
    print(f'sum of top 3 elves calories for input file {input_filename} is {top_3_sum}') 
    return top_3_sum

if __name__ == '__main__':
    test_get_max_calories()
    get_max_calories('actual_data.txt')
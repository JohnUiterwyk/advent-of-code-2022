from typing import List
import os

def test_parse_input_file():
    stacks = parse_input_file('sample_data.txt')
    expected_result = 'CMZ'
    actual_result = get_top_crates_message(stacks)
    assert actual_result == expected_result


def parse_input_file(input_filename, reverse_on_move:bool = True):
    list_of_stacks = []
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()
        num_of_stacks = calc_number_of_stacks(lines[0].rstrip(os.linesep))
        stacks = [[] for _ in range(num_of_stacks)]
        for line in lines:
            if '[' in line:
                row_of_stacks = parse_row_of_stacks(line.rstrip(os.linesep))
                for stack, new_value in zip(stacks, row_of_stacks):
                    if new_value is not None:
                        stack.append(new_value)

            elif line.startswith(' 1'):
                # reached the end of the stack parsing
                pass
            elif line.startswith('move'):
                move_count, source, destination = parse_move_instruction(line.rstrip(os.linesep))
                stacks = modify_stacks(stacks, move_count, source, destination, reverse_on_move)

    return stacks

def test_modify_stacks():
    test_data = [['A','B','C','D'],['E','F'],['G','H']]
    expected_result = [['C','D'],['E','F'],['B','A','G','H']]
    actual_result =  modify_stacks(test_data,2,1,3) 
    assert actual_result == expected_result

def modify_stacks(stacks: List[List[str]], move_count: int, source: int, destination: int, reverse_on_move:bool = True) -> List[List[str]]:
    moving = stacks[source-1][:move_count]
    stacks[source-1] = stacks[source-1][move_count:]
    if(reverse_on_move):
        moving.reverse()
    moving.extend(stacks[destination-1])
    stacks[destination-1] = moving
    return stacks


def test_parse_row_of_stacks():
    assert parse_row_of_stacks("    [D]    ") == [None, 'D', None]
    assert parse_row_of_stacks("[N] [C]    ") == ['N', 'C', None]
    assert parse_row_of_stacks("[Z] [M] [P]") == ['Z', 'M', 'P']


def parse_row_of_stacks(row):
    result_row = list()
    stacks = calc_number_of_stacks(row)
    for i in range(stacks):
        if row[i*4] == '[':
            result_row.append(row[i*4+1])
        else:
            result_row.append(None)
    return result_row

def test_get_top_crates_message():
    test_data = [['A','B','C','D'],['E','F'],['G','H']]
    expected_result = 'AEG'
    actual_result =  get_top_crates_message(test_data) 
    assert actual_result == expected_result

def get_top_crates_message(stacks):
    return ''.join([stack[0] for stack in stacks])
        


def calc_number_of_stacks(row):
    return (len(row)+1) // 4


def test_parse_move_instruction():
    assert parse_move_instruction('move 1 from 2 to 1') == (1, 2, 1)
    assert parse_move_instruction(
        'move 123 from 345 to 678') == (123, 345, 678)


def parse_move_instruction(instruction):
    parts = instruction.split()
    return int(parts[1]), int(parts[3]), int(parts[5])


if __name__ == '__main__':
    test_parse_row_of_stacks()
    test_parse_move_instruction()
    test_modify_stacks()
    test_get_top_crates_message()
    test_parse_input_file()
    print(f"Part 1: {get_top_crates_message(parse_input_file('input_data.txt'))}")
    print(f"Part 2: {get_top_crates_message(parse_input_file('input_data.txt', reverse_on_move=False))}")
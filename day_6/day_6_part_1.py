from typing import List
import os

def test_find_start_of_packet():
    assert find_start_of_packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb',4) ==7
    assert find_start_of_packet('bvwbjplbgvbhsrlpgdmjqwftvncz',4) ==5
    assert find_start_of_packet('nppdvjthqldpwncqszvftbrmjlhg',4) ==6
    assert find_start_of_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',4) == 10
    assert find_start_of_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',4) ==11
    assert find_start_of_packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb',14) ==19
    assert find_start_of_packet('bvwbjplbgvbhsrlpgdmjqwftvncz',14) ==23
    assert find_start_of_packet('nppdvjthqldpwncqszvftbrmjlhg',14) ==23
    assert find_start_of_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',14) == 29
    assert find_start_of_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',14) ==26


def find_start_of_packet(input_string:str, header_length:int = 4):
    for i in range(0,len(input_string)-header_length):
        if len(set(input_string[i:i+header_length])) == header_length:
            return i+header_length
    

def find_start_of_packet_in_file(input_filename:str, header_length:int = 4):
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()
        input_string = lines[0].rstrip(os.linesep)
        start_index =  find_start_of_packet(input_string, header_length)
        print(f'The start index is {start_index} with header length {header_length}')

    return start_index


if __name__ == '__main__':
    test_find_start_of_packet()
    find_start_of_packet_in_file('input_data.txt',4)
    find_start_of_packet_in_file('input_data.txt', 14)
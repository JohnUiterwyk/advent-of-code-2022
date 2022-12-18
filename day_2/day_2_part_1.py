def test_get_score():
    assert get_score('A Y') == 8
    assert get_score('B X') == 1
    assert get_score('C Z') == 6


def get_total_score(input_filename, max_rounds = None):

    current_round = 0
    total_score = 0
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()

        if max_rounds is None:
            max_rounds = len(lines)

        # Iterate over the lines in the file
        for line in lines:
            current_round = current_round+1
            if current_round > max_rounds:
                break
            round_data = line.rstrip()
            round_score = get_score(round_data)
            total_score = total_score + round_score
            
    print(f'total score for input file {input_filename} is {total_score}') 
    return total_score

def get_score(round_data):
    # rock = 1, paper = 2, scissors = 3
    # loss = 0, draw = 3, win = 6
    score_dict = {
        'A X':4, # Rock Rock - draw
        'B X':1, # Paper Rock - loss
        'C X':7, # Scissors Rock - win
        'A Y':8, # Rock Paper - win
        'B Y':5, # Paper Paper - draw
        'C Y':2, # Scissors Paper - loss
        'A Z':3, # Rock Scissors - loss
        'B Z':9, # Paper Scissors - win
        'C Z':6  # Scissors Scissors - draw
    }
    return score_dict[round_data]



if __name__ == '__main__':
    test_get_score()
    get_total_score('input_data.txt')
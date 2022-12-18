def test_get_total_score():
    assert get_total_score('sample_data.txt') == 12


def get_total_score(input_filename):

    current_round = 0
    total_score = 0
    # Open the file with the 'open' function, which returns a file object
    with open(input_filename, 'r') as f:
        # Use the file object's 'readlines' method to read all the lines in the file
        lines = f.readlines()

        # Iterate over the lines in the file
        for line in lines:
            encrypted_round_data = line.rstrip()
            round_data = get_play(encrypted_round_data)
            round_score = get_score(round_data)
            total_score = total_score + round_score
            
    print(f'total score for input file {input_filename} is {total_score}') 
    return total_score


def get_play(encrypted_round_data):

    # a = rock, b = paper, c = scissors
    # x = loss, y = draw, z = win
    play_dict = {
        'A X':'Rock Scissors',
        'B X':'Paper Rock', 
        'C X':'Scissors Paper',
        'A Y':'Rock Rock', 
        'B Y':'Paper Paper', 
        'C Y':'Scissors Scissors',
        'A Z':'Rock Paper', 
        'B Z':'Paper Scissors', 
        'C Z':'Scissors Rock'  
    }
    return play_dict[encrypted_round_data]

def get_score(round_data):
    # rock = 1, paper = 2, scissors = 3
    # loss = 0, draw = 3, win = 6
    score_dict = {
        'Rock Rock':4, # draw
        'Paper Rock':1, # loss
        'Scissors Rock':7, # win
        'Rock Paper':8, # win
        'Paper Paper':5, # draw
        'Scissors Paper':2, # loss
        'Rock Scissors':3, # loss
        'Paper Scissors':9, #win
        'Scissors Scissors':6  # draw
    }
    return score_dict[round_data]



if __name__ == '__main__':
    test_get_total_score()
    get_total_score('input_data.txt')
from data_fetcher import get_data

scores = {'A X': 1 + 3,
          'A Y': 2 + 6,
          'A Z': 3 + 0,
          'B X': 1 + 0,
          'B Y': 2 + 3,
          'B Z': 3 + 6,
          'C X': 1 + 6,
          'C Y': 2 + 0,
          'C Z': 3 + 3}

moves = get_data(2).split('\n')[:-1]

print(moves)

moves_scored = [scores[move] for move in moves]

print(len(moves_scored) == len(moves))
print(moves_scored)
print(sum(moves_scored))

responses = {'A X': 3 + 0,
             'A Y': 1 + 3,
             'A Z': 2 + 6,
             'B X': 1 + 0,
             'B Y': 2 + 3,
             'B Z': 3 + 6,
             'C X': 2 + 0,
             'C Y': 3 + 3,
             'C Z': 1 + 6}

responses_scored = [responses[move] for move in moves]

print(len(responses_scored) == len(moves))
print(responses_scored)
print(sum(responses_scored))

def score(game):
    spare = '/'
    strike = "Xx"
    result = 0
    turn = 1
    max_turns = 10
    max_points_per_try = 10
    first_try = True
    for i in range(len(game)):
        if turn < max_turns and get_value(game[i]) == max_points_per_try:
            result += get_value(game[i+1])
            if not (game[i] is spare): 
                result = game_is_spare(i+2, game, spare, result, max_points_per_try)
        result = game_is_spare(i, game, spare, result, max_points_per_try)
        if not first_try:
            turn += 1
        first_try = not first_try
        if game[i] in strike:
            first_try = True
            turn += 1
    return result


def get_value(char):
    if char in map(str, range(1, 10)):
        return int(char)
    elif char in "Xx/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def game_is_spare(i, game, spare, result, max_points_per_try):
    if game[i] is spare:
        return result + max_points_per_try - get_value(game[i-1])
    else:
        return result + get_value(game[i])


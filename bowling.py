def score(game):
    spare = '/'
    strike = "Xx"
    result = 0
    turn = 1
    max_turns = 10
    first_try = True
    for i in range(len(game)):
        if game[i] is spare:
            result += max_turns - last
        else:
            result += get_value(game[i])
        if turn < max_turns and get_value(game[i]) == 10:
            if game[i] is spare:
                result += get_value(game[i+1])
            elif game[i] in strike:
                result += get_value(game[i+1])
                if game[i+2] == spare:
                    result += max_turns - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if first_try:
            first_try = False
        else:
            first_try = True
            turn += 1
        if game[i] in strike:
            first_try = True
            turn += 1
    return result

def get_value(char):
    if char.isnumeric():
        return int(char)
    elif char in "Xx/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

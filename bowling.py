def score(game):
    result = 0
    turn = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if turn < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            turn += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            turn += 1
    return result

def get_value(char):
    if char in "123456789":
        return int(char)
    elif char in "Xx/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

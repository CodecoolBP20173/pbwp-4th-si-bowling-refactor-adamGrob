def score(game):
    spare = '/'
    strike = "Xx"
    result = 0
    turn = 1
    max_turns = 10
    max_points_per_try = 10
    first_try = True
    for i in range(len(game)):
        
        # This part executes unless it is the last turn
        if turn < max_turns and get_value(game[i]) == max_points_per_try:
            result += get_value(game[i+1])
            if not (game[i] is spare): 
                if game[i+2] is spare:
                    result += max_points_per_try - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        # This parts executes at the last turns
        if game[i] is spare:
            result += max_points_per_try - get_value(game[i-1])
        else:
            result += get_value(game[i])
    
        # This part decides if the turn is over.
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



def main():
    print(score("1/35XXX458/X3/XX6"))

#main()

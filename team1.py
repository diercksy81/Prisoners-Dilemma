import random

team_name = 'percent betray'
strategy_name = 'no'
strategy_description = 'no'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0:
        return 'c'
    elif len(my_history)>0:        
        c = their_history.count('b')
        t = float(c)/len(their_history)
        if random.random()<t:
            return 'b'
        else:
            return 'c'
    else:
        return 'c'
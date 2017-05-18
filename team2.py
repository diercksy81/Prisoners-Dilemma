import random

team_name = 'b and c count'
strategy_name = 'yes'
strategy_description = 'yes'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0:
        return 'c'
    elif len(my_history)>0:        
        b = their_history.count('b')
        c = their_history.count('c')
        t = (float(b)/len(their_history))-.1
        r = (float(c)/len(their_history))-.1
        if random.random()<t:
            return 'b'
        elif random.random()<r:
            return 'b'
        else:
            return 'c'
    else:
        return 'c'
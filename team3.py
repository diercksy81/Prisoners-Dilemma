import random

team_name = 'b if <35'
strategy_name = 'maybe'
strategy_description = 'maybe'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0:
        return 'c'
    elif len(my_history)>0:        
        c = their_history.count('b')
        t = float(c)/len(their_history)
        if t>.35:
            if random.random()<t:
                return 'b'
            else:
                return 'c'
        else:
            return 'c'
    else:
        return 'c'
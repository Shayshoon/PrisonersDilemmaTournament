import random

def strategy(history, memory):
    """
    Start with cooperation, and then make random moves from opponents playbook
    """
    turns_taken = len(history[0])
    random_move = random.randrange(turns_taken) if turns_taken else 0

    move_choice = history[1][random_move] if turns_taken else 1
    
    return move_choice, None
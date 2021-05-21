import numpy as np

def strategy(history, memory):
    """
    Start with cooperation, and then make the average move of the opponent
    """
    turns_taken = len(history[0])
    move_choice = round(np.mean(history[1])) if turns_taken > 0 else 1
    
    return move_choice, None
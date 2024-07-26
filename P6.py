def rational_decision(info_table, person):
    if person not in info_table:
        return None
    
    outcomes = info_table[person]
    
    no_confess_outcome = outcomes[0]  # [both no confess, other confesses, they confess, both confess]
    confess_outcome = outcomes[1]     # [both no confess, other confesses, they confess, both confess]
    
    no_confess_sentence = no_confess_outcome[1]  # Sentence if the other confesses
    confess_sentence = confess_outcome[0]       # Sentence if the other does not confess

    if confess_sentence < no_confess_sentence:
        return 1  # index for 'confess'
    
    if no_confess_sentence < confess_sentence:
        return 0  # index for 'not confess'
    
    return None

if __name__ == "__main__":
# Example usage
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]} 
    p = 'Lobha' 
    r = rational_decision(s, p) 
    print(p, ':', choices[r])


def non_existing_letters(g,w):
    """this function checks for non corresponding letters between the two words
        and returns a list of them"""
    result = []                     #a list to hold the result
    for l in g:
        if l not in w:
            result.append(l)        #if the letter doesn't exist in the target word
                                    #add it to the list
    return result
            
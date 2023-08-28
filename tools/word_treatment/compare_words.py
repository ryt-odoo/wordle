def compare_words(g,w):
    """this function compares the entered by the user word with the word to guess
        and returns the corresponding letters in upper case if the letter is in the 
        right position and in lower case if it is misplaced"""
    
    result = []                         #a list to hold the result
    for l in g:                         #iterate over the letters of the given word
        if l in w:                      #check if the letter is in the target word
            if g.index(l) == w.index(l):#if so check if their positions are the same
                l = l.upper()
            else:
                l = l.lower()
        else:
            l = "*"
        result.append(l)
    return result

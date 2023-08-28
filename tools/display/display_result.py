def display_result(word):
    """this function displays a five letter word in a manner that
        every letter is put in a box"""
    
    print("="*11)               # print the upper border
    for l in word:
        print (f"|{l}", end='') # for every letter print a vertical line followed by
                                # letter and stay on the same line
    print ("|")                 # close the boxes
    print ("="*11)              # print the lower border


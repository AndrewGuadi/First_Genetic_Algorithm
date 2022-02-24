import random
import string 





def create_random_word():
    ##change this number to expand the length of possible words
    number = random.randrange(1, 45)
    ##<checkstep>print(number)
    
    ## number will be the length of the word produced
    selection = ""
    selection += string.ascii_letters
    selection += " "
    selection += string.digits
    selection += string.punctuation
    word_produced = ""

    len_of_selection = len(selection)

    for i in range(number):
        rand_number = random.randrange(0,len(selection))
        letter = selection[rand_number]
        word_produced += letter
    

    return(word_produced)

    

def create_random_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rand_number = random.randrange(1,26)

    random_letter = alphabet[rand_number]

    return random_letter

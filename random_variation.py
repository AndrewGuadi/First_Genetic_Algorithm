import random

def create_new_child(parent1, parent2):
    dna1 = parent1[0]
    dna2 = parent2[0]
    dna3 = ""

    counter = 2
    for i in range(len(dna1)):

        variation = random.randrange(1,50)
        if variation == 2:
            letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"
            lenofletters = len(letters)
            number =  random.randrange(1,lenofletters)
            random_letter = letters[number]
            dna3 += random_letter
        
        else:
            if counter % 2 == 0:
                dna3 += dna1[i]
                counter += 1

            
            else:
                dna3 += dna2[i]
                counter += 1

    return dna3
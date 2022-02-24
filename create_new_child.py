def create_new_child(parent1, parent2):
    dna1 = parent1[0]
    dna2 = parent2[0]
    dna3 = ""

    if len(dna1) == len(dna2):
        counter = 2
        for i in range(len(dna1)):
            
            if counter % 2 == 0:
                dna3 += dna1[i]
                counter += 1

            else:
                dna3 += dna2[i]
                counter += 1

        return dna3

    else:
        length_of_shorter_dna = 0
        if len(dna1) > len(dna2):
            length_of_shorter_dna = len(dna2) - 1
        else:
            length_of_shorter_dna = len(dna1) - 1 

        counter = 2
        for i in range(length_of_shorter_dna):
            
            if counter % 2 == 0:
                dna3 += dna1[i]
                counter += 1

            else:
                dna3 += dna2[i]
                counter += 1

        return dna3
        



def check_gen_til_found(generation, target_word):
    if generation[0][0][0] == target_word:
        check_word = generation[0][0][0]
        print(f"Found: {check_word}")
    

    else:
        check_word = generation[0][0]
        fitness_score = generation[0][1]

        return(check_word, fitness_score)
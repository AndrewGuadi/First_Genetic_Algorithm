from create_random_word import create_random_word
from fitness_score import fitness_score, fitness_score_post
from check_word import check_two_words
from check_gen_til_found import check_gen_til_found

from random_variation import create_new_child

## Ask user for random number input

##This should be a constant after the alpha testing is complete
NUMBER = 10000-

#Ask for Target Word (Between 1-20 characters/No numbers)
target_word = input("Target Word (1-45 characters): ")
check_word = ""
age = 1
best_score_found = 0
##----------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------##
##Establish the initial population
initial_population = []

for i in range(NUMBER):
    new_member = []
    new_word = create_random_word()
    new_member.append(new_word)
    initial_population.append(new_member)

##----------------------------------------------------------------------------------##
##print(initial_population)



##----------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------##
##Rate the fitness of each member and assign it to the proper member

refined_init_population = []

for member in initial_population:
    refined_init_population.append(member)

initial_population = []
for member in refined_init_population:
    new_member = []
    fitness = fitness_score(member, target_word)
    new_member.append(member[0])
    new_member.append(fitness)
    initial_population.append(new_member)


initial_population.sort(key=lambda member : member[1], reverse=True)

#######
##print(initial_population)
#######

##---------------------------------------------------------------------------------------##
##---------------------------------------------------------------------------------------##

most_fit_member = check_gen_til_found(initial_population, target_word)
generation_age = 1

new_generation = []

for member in initial_population:
    new_generation.append(member)

##print(new_generation)

while most_fit_member[0] != target_word:

    old_generation = []
    for member in new_generation:
        old_generation.append(member)
    
    new_generation= []
    
    most_fit_dna = most_fit_member[0]
    most_fit_fitness = most_fit_member[1]
    print(f"Generation {generation_age}: Most Fit DNA: {most_fit_dna} || Fitness: {most_fit_fitness}", end="\r")
    
    if most_fit_fitness > best_score_found:
        print(f"Generation {generation_age}: Most Fit DNA: {most_fit_dna} || Fitness: {most_fit_fitness}")
        best_score_found = most_fit_fitness
    generation_age += 1

    for i in range(1, 200):
        parent1 = old_generation[i]
        parent2 = old_generation[i+1]
        parent3 = old_generation[i+2]


        first_child_dna = create_new_child(parent1, parent2)
        second_child_dna = create_new_child(parent1, parent3)

        first_child_fitness = fitness_score_post(first_child_dna, target_word)
        second_child_fitness = fitness_score_post(second_child_dna, target_word)

        first_new_member = []
        second_new_member = []
        
        first_new_member.append(first_child_dna)
        first_new_member.append(first_child_fitness)

        second_new_member.append(second_child_dna)
        second_new_member.append(second_child_fitness)

        #print(first_child_dna, second_child_dna)

        new_generation.append(first_new_member)
        new_generation.append(second_new_member)

    new_generation.sort(key=lambda member : member[1], reverse=True)


    most_fit_member = new_generation[0]


    if most_fit_member[0] == target_word:
        final_word = most_fit_member[0]
        final_fitness = most_fit_member[1]
        print(f"Generation {generation_age}: FOUND: {final_word} || Fitness: {final_fitness}")
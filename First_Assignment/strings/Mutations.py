
def mutate_string(string, position, character):
    mutated_string = string[:position] + str(character) + string[position+1:]
    return mutated_string


'''
sudocode from instruction:

  For each character in the input string:
    Form a simpler string by removing the character from the input string
    Generate all permutations of the simpler string recursively (i.e. call the perm_gen_lex function with the simpler string)
    Add the removed character to the front of each permutation of the simpler string, and add the resulting permutation to the list 
'''

#string => list of strings
#generate all the permutations of the characters in a string
def perm_gen_lex(a): 
    #base case
    if len(a) == 0:
        return []
    elif len(a) == 1:
        return [a]
    #reduce case
    i = 0
    #indicate that the result is a list
    result = []
    #iterate through the string
    while i < len(a):
        #reduced string is the string without the selected charactor
        reduced = a[0:i] + a[i+1:]
        all_reduced_permutations = perm_gen_lex(reduced)
        for string in all_reduced_permutations:
            #add the selected charactor to each string of the semi-result string
            result_string = a[i] + string
            #append result string to the list
            result.append(result_string)
        i += 1
    return result
        

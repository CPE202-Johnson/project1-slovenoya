#int => string
#return the string of the b base of num
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    #basecase
    if num < b:
        return correct_form(num)
    #reduced case = quotient of num / b
    reduced = num // b
    #return the recursion of reduced + the remainder of num / b
    return convert(reduced, b) + correct_form(num % b)



#int => string
#return the string of a number, if greater or equals 10,
#return A, B, C, D, E, F
def correct_form(number):
    if(number < 10):
        return str(number)
    elif(number == 10):
        return "A"
    elif(number == 11):
        return "B"
    elif(number == 12):
        return "C"
    elif(number == 13):
        return "D"
    elif(number == 14):
        return "E"
    else:
        return "F"
    

#int -> bool
#return true or false if bears can be made to be exactly 42 according to the rules
def bears(n):
    #base cases:
    #return true if n is 42
    if n == 42:
        return True
    
    #return false if n is not devisible by any of those numbers: 2, 3, 4, and 5
    elif n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0:
        return False
    
    #special case: when the bear is not divisible by one of 2, 3, 4, 5 
    elif n < 42:
        return False
    
    #reduce
    #case of even number
    if n % 2 == 0:
        bear_2 = int(n / 2)
    else:
        bear_2 = -1

    #case of divisible by 3 or 4
    if n % 3 == 0 or n % 4 == 0:
        last_two_dig = n % 100
        last_digit = n % 10
        second_last_digit = (last_two_dig - last_digit) / 10
        multiply = last_digit * second_last_digit
        bear_3_4 = n - multiply
        #in case of dead loop
        if multiply == 0:
            bear_3_4 = -1
    else:
        bear_3_4 = -1
    
    
    
    if n % 5 == 0:
        bear_5 = n - 42
    else:
        bear_5 = -1
    
    #combine
    return bears(bear_2) or bears(bear_3_4) or bears(bear_5)
    
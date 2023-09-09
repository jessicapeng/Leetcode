def sumOfTwo(a, b):
    while(b != 0): # while carry isn't 00000000 aka no more left to carry
        a_temp, b_temp = a, b
        # first get what value are when you add
        add = a_temp ^ b_temp
        # now figure out what carry by & and shifting over
        carry = (a_temp & b_temp) << 1
        # now need to repeat and xor carry to a so change
        # a to add and b to carry
        a = add
        b = carry
    print(a)
    return a
    
# important concept: adding is just & << 1 and xor
sumOfTwo(2,-5)
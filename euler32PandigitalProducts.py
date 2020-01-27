#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



def IsUniques(list_new):
    result = False
    if len(list_new) == len(set(list_new)):
        result = True
    return result

def PandigitalProducts():
    final_list = []
    for a in [x for x in range(1, 9876 +1) if (IsUniques(str(x)) and "0" not in str(x))]:
        #print(a)
        for b in [y for y in range(1, int(9876//2)+1) if (IsUniques(str(y)) and y != a and "0" not in str(a*y) and "0" not in str(y))]:
         #   print(a,b)
            if len(str(a)) + len(str(b)) + len(str(a*b)) == 9 and IsUniques(str(a)+str(b)+str(a*b)):
                new_number = a*b
                if new_number not in final_list:
                    final_list.append(new_number)
    return sum(final_list)


#final = IsUniques([1,2,3,4])
final = PandigitalProducts()
print(final)



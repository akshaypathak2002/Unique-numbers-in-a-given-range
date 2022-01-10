# In this we will see how to find unique numbers in the give range
def is_unique(number):
    s = {}
    while(number != 0):
        rem = number % 10  # To get the floor value
        # s[rem] += 1  # If we find same element next time the increase count by one
        if rem in s.keys(): #If remainder of that number is already in  dictionary then use increase its count by 1 else 1 
            s[rem] += 1
        else:
            s[rem] = 1
        number //= 10
    for v in s.values():
        if v > 1:  # If we have same numbers then for some numbers value must be greater then 1
            return False
    return True


def unique_numbers(L, R):
    number = []
    for i in range(L, R+1):
        if is_unique(i) == True:
            number.append(i)
    return number        


L, R = input().split()
numbers = unique_numbers(int(L), int(R)) #Typecasting the input to the int 
print(numbers)

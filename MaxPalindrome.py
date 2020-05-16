

maximum = int("9"*int(input("How many digits would you like the products to be? >>> ")))

minimum = int((len(str(maximum))-1)*"9")

max2 = 0
palindrome = 0

for i in range(maximum, minimum, -1):
    if i % 11 == 0:
       max2 = i
       break

print("done thinking about step 1. Max:", maximum, " Min:", minimum, "Max2:", max2)

for x in range(maximum,minimum,-1):
    if x % 11 == 0:  
        step = -1
        roof = maximum
    else:
        step = -11
        roof = max2
    for y in range(roof,x,step):
        prod = x * y
        if prod <= palindrome:
            break
        prodstr = str(prod)
        if prodstr == prodstr[::-1]:
            palindrome = prod

print(palindrome)


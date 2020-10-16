# variables
name =  "John Cena"
number = 12

# loops
# for loop
for i in range(4):
    number += 1
    print(number)

print("*********************")

# while loop
while number < 20:
    number += 1
    print(number)
    # conditionals
    if number%2 == 0:
        print("even!")
    else:
        print("odd!")    

# functions
def greeting():
    print("hello")

greeting()

# return function
def addition(n1, n2):
    return n1+n2

print(addition(number, number))

sum = addition(number, number)
print(sum)
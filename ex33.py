i = 0
x = 0
numbers = []

def num_function(i, j, x, numbers):
    if(i < j):
        print("At the top of i is %d" % i)
        numbers.append(i)
    
        i = i + x
        print("Numbers now: ", numbers)
        print("At the bottom i is % d" % i)
        num_function(i, j, x, numbers)
    return numbers
        
numbers = num_function(0, 50, 15, [])
for num in numbers:
    print(num)
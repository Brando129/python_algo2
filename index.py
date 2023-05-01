#Create a function that takes all the numbers from 0 through a users input number and
#adds each number to next until the users number is reached.

def get_sum(num):
    sum = 0

    for i in range(0,num+1):
        sum += i 
    return sum

print(get_sum(2))

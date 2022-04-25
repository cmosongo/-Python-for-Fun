'''
Return a series of prime integers from 2 to the last value input
'''

def is_prime(x):
    prime = True
    for i in range(2,x):
        if x%i == 0:
            prime = False
            break
    return(prime)
    
while True:
    end = int(input("Enter last value of range: "))
    for i in range(2,end):
        if is_prime(i):
            print(i)

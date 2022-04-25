import turtle
import math
import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

count = 0
row = 0
turtle.penup()
turtle.hideturtle() 
font = ('arial',5)
while count< 10000:
    for deg in [0,90,180,270]:
        if deg in [0,180]:
            move = font[1] *1
            row += 1
        else:
            move =5
        turtle.seth(deg)
        for i in range(row):
            turtle.forward(move)
            if is_prime(count):
                turtle.write('0',font=font)
            count +=1
    
                
  

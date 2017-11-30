import math

a = int(input("First element of quadratic equation: "))
b = int(input("Second element of quadratic equation: "))
c = int(input("Third element of quadratic equation: "))


def quadratic_equation_elements(a,b,c):

    delta = b**2 - (4*a*c)

    if(a == 0):
        print("This is not a quadratic equation")
    else:
        if(delta < 0):
            print ("Lack of solution")
        elif(delta == 0):
            x1 = -1*b/(2*a)
            print ("Solution: " + str(x1))
        else:
            x1 = (-1*b - math.sqrt(delta))/(2*a)
            x2 = (-1*b + math.sqrt(delta))/(2*a)
            print ("Solutions: " + str(x1) + ", " + str(x2))


quadratic_equation_elements(a,b,c)
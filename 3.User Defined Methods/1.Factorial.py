#Q1. Find the factorial of a given number
def fact(n):
    if n == 0 or n ==1 :
        return 1
    else:
        return (n * fact(n-1))
        
n = int(input("Enter the  number below  : "))
print(fact(n))
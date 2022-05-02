
a = int(input( "Enter a number:"))
b = int(input( "Enter another number:"))
def divideNum():
    try:
        c=a/b
    except ZeroDivisionError:
         c = "You cannot divide by zero."
    print(c)
   
    
divideNum()
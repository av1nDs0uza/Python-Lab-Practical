#Q4.Print all the numbers between 100 to 200 which are divisible by 4 and 7
lower = 100
upper = 200
for i in range(lower, upper+1):
   if((i%4==0) & (i%7==0)):
      print(i)
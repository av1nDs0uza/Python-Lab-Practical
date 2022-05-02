#Q3.Sort list elements; press 1 for ascending order and, press 2 for descending order (choice based)
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
     
print(list)
x = int(input("Enter 1 to sort in accending or 2 to sort in descending : "))
if x == 1: 
    list.sort()
    print("Accending Sorted List : ",list )
     

elif x == 2:
    list.sort(reverse=True)
    print("Descending Sorted List : ",list) 

else: 
    print("Invalid response")
    exit() 
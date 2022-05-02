list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    list.append(ele)
     
print(list)
x = int(input("Enter the index : "))
try:   
    
    print (list[x])  
except LookupError:  
    print ("Index Error Exception Raised, list index out of range")
else:  
    print ("Success, no error!")

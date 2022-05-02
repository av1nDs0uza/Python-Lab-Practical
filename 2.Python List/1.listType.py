#Q1.Find number of list elements of different data types
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    list.append(ele)
     
print(list)
num= len(list)
print("Number of elements in the list: ", num)

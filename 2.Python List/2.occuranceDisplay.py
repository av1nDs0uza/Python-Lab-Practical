list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print(list)
x = int(input("Enter the number to be checked : "))
def check(list, x):
  count = 0
  for ele in list:
     if (ele == x):
         count = count + 1
         
  return count
print('{} has occurred {} times'.format(x, check(list,x)))

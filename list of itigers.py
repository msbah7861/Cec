list1=[]
list2=[]
m=int(input("enter the limit of list1:"))
print("enter the elements")
for i in range(0,m):
    value=int(input())
    list1.append(value)
n=int(input("enter the limit of list2:"))
print("enter the elements")
for i in range(0,m):
    value=int(input())
    list1.append(value)
print(list1,list2)
if len(list1)==len(list2):
    print("both list 1 and list2 are of the same length")
else:
    print("both list 1 and list2 are not of the same length")
if sum(list1)==sum(list2):
    print("the sum of both list 1 and list2 are same")
else:
    print("the sum of both list 1 and list2 are not same")
list3=[each for each in list1 if each in list2]
print("same members are:",list3)

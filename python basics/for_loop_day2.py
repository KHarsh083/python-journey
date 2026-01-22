from numpy import *

nums = [1,2,3,4,5]


# string ='abc'
# string1=array(list(string))
for num in nums:
    if num == 3:
        print("found")
        continue
    print(num)



# print(string1)

#range
for i in range(10):
    print(i)
#same
for i in range(1,10):
    print(i)

#while loop
i = 0
while i <10:
    if i == 5:
        break
    print(i)
    i +=1 
# import array as arr
from array import *

# val = arr.array('i',[1,2,3,4,5,6])
val = array('i',[1,2,3,4,5,6])
val2 =array('d',[1,2,3,2.4,5,6,])
# val3 = array('u',['a','b'])

# print(val)
# a = len(val)
# # for i in range(0,6):
# #     print(val[i], end="")
# for i in range(0,a):
#     print(val[i], end="")
# print("\n")

# for i in val:  #enhanced for loop doesnt need last element so even if the the size of array is increased
#     print(i, end="")

# print("\n")

# for j in val2:
#     print(j, end=',')

# print("\n")

# for j in val3:
#     print(j, end='')

# print("\n")

# print(val.typecode)

# val.reverse()

# for i in val:
#     print(i, end=",")

# print("\n")

# val.insert(0,2)
# val.append(55)
# val[1]=22 #overwrite
# for i in val:
#     print(i, end=",")

# coppyArray = array(val.typecode , (i for i in val )) #value of i in copyarray == value of in val
# coppyArray = array(val.typecode , (i*3 for i in val ))
# for i in coppyArray:
#     print(i, end=",")
# print("\n")
# coppyArray.pop(3) #deletion(index)
# coppyArray.remove(6) #deletion(particular element)
# for i in coppyArray:
#     print(i, end=",")
print("\n")
#slicing
# a = araay_name[startindex : end index]
# abc = val[3:6] #also [0:-3] can happen meaning last 3 element are ot present
# for i in abc:
#     print(i, end=",")
# abcc =val[::-1] #reverse
# print("\n")
# for i in abcc:
#     print(i, end=",")

#user input
# n=int(input("how many elements"))
# input_array= array('i',[])
# for i in range(0,n):
#     input_array.append(int(input(f"enter the element {i} ")))

# i=input_array.index(45)   #index of particular element
# print(i)

arr =array('i',[1,2,3,4,5,6])
print(arr)
for i in arr:
    print (i,end='')
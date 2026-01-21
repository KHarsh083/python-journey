names = ["Harsh", "Katiyar"]

names.append("Btech")
# print(names[:2])
names.insert(0,"Mr")
# print(names[:2])
# print(names)

n=len(names)
names.insert(n,"cse")
# print(names)
n=len(names)


names_3=["noida"]


names.extend(names_3)
# print(names)

#remove
names.remove('Harsh')
# print(names)
poped_item=names.pop()
print(poped_item)

#reverse and sort of list

names.reverse()

print(names)
# number =[1,5,3,4]
# number_sorted=sorted(number)
# print(number,number_sorted)
# print(number,min(number_sorted))
# print(max(number),min(number_sorted),max(number)+min(number_sorted),sum(number))

# print(5 in number)
# print(number.index(1))

# for num in number:
#     print(num)

# for num, index in enumerate(number,start=1):
#     print(num,index)

names_str=', '.join(names)
print(names_str)
new_list=names_str.split(', ')
print(new_list)
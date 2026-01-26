student = {}
student1= {'name':'john', 'age':16, 'course': ['math','english']}
print(student1)
print(student1['name'])
print(student1.get('name'))
print(student1.get('hello'))  #doesnt give error if the key doesnt exists while [] does
print(student1.get('hello','NOT FOUND')) #will give NOT found if key doesnt exist rather than none

#but if want to add hello key

student1['hello'] = 'Guys'
print(student1)

#update used to update values of values for keys
print(student.update({'name':'Harsh', 'ph-no': 9989899}))
print(student)

del student['ph-no']
print(student)

val = student.pop('name')
print(student)
print(val)

#length
print(len(student1)) #give no of keys in dict
print(student1.keys())
print(student1.values())
print("\n here\n")
print(student1.items())   #gives key value pairs
print("\n")
#for loop
for keys in student1:
    print(keys)  #gives only keys

for keys,value in student1.items():
    print(keys,value)   #gives key value pair
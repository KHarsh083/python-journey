# if, elseif, else
language='python'
if language == 'Python':
    print("True")
elif language == 'python':
    print("True but python")
else: 
    print("False")

user = 'Amit'
logged_in = False
if user == 'Harsh' and logged_in:
    print('Harsh has logged in')
else:
    print("Harsh has not logged in")

if user == 'Harsh' or logged_in:
    print('someone logged in')
else:
    print("None has logged in")

if not logged_in :
    print("pls log in ")
else:
    print("logged in")

print(id(user))  #give location of the variable stores data and 'is' operator checks whether the two are same
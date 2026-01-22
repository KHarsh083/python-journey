from numpy import *


val = array([1,2,3]) #it will not take typecode and will give error
for x in val:
    print(x)

#hetrogeneous array can be created using numpy stirng, float and int in one array
val= array([1,2,3,'a',2.5])
for x in val:
    print(x,end=',')

val = array([1,2,3],float) #typecasting converts everything in array to float
for x in val:
    print(x,end=',')
print('\n')
val =linspace(10,20,5) #array using linspace(startpoint(included),endpoint(included),howmany partitions)
for x in val:
    print(x,end=',')
print('\n')


#dimenesions
d1 = array(10)
d2 = array([[1,2],[1,2]])
d3 = array([[[1,2],[1,2]],[[1,2],[1,2]]])
print(d1)
print('\n')
print(d2)
print('\n')
print(d3)
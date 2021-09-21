#!/bin/python3

# hello 
# i hope you are good
# here i want to talk about "set" in python

# "set" is looks like list

# here like list when we write some number in it it print for us the number


set0 = {1 , 2 , 3 , 4 , 5 , 6 , 7}
print(set)
# output == {1 , 2 , 3 , 4 , 5 , 6 , 7}

# here we write string in it 
set2 = {"nima" , "shayan" , "danyal"}
print(set2)
# output == {'nima' , 'shayan' , 'danyal'}

# here we write mix of every thing 
# set can also write flout in it and it can also write string and it can also write touple in it whit together
set3 = {0.2 , "nima" , (43 , 23 , 234)}
print(set3)
# output == {0.2, (43, 23, 234), 'nima'}

# we can also write "set([])" insted {}
different = set([1, 2, 3, 4, 5, 6])
print(different)
# output == {1, 2, 3, 4, 5, 6}

# set has removed the duplicates and returned only one of each duplicate items
set4 = {1 , 2 , 3 , 3 , 2 , 2 , 2 , 2 , 1 , 1 , 2 , 1 , 3 , 3}
# it only write {1,2,3}
print(set4)
# output == {1, 2, 3}

# we can also understand type of command
type0 = set()
print(type(type0))
# output == <class 'set'>

# here we can also ask set
number = {312 , 24 , 643 , 634 , 589 , 346 , 234 , 758 , 4684 , 85 , 56}
# and if it was it print true and when it was not it print false
print(85 in number)
# output == true
print(6575186 in number)
# output == false


# thanks for rading (:

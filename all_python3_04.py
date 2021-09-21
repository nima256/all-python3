#!/bin/python3

# hello 
# i hope you are good
# today we want to talk about "list" in python
# how to creat a list
list = []
print(list) 
# output == []


# here we also write number in list
list_num = [12,34,23,14,35,76,87]
print("here we can write number in list :")
print(list_num)
# output == here we can write number in list :
#           [12, 34, 23, 14, 35, 76, 87]        


# here we can knowing the size of list
# with "len" 
list_empty = []
print(len(list_empty)) 
# output == 0

list1 = [132 , 123 ,346 , 34 , 67]
print(len(list1))
# output == 5


# also we can add something in list
# with "append"
list_add = []
print(list_add)
# output == []
# now the list is empty 
# now we write append

# first we write list name
# second write .append() 
# and in bracket write every thing that you want to add to your list
list_add.append(2)
list_add.append(13)
list_add.append("nima")
print(list_add)
# output == [2, 13, 'nima']


# we can also add tuple in list
list_tuple = [1,2,6,5,9,85,12]
print(list_tuple)
# output == [1,2,6,5,9,85,12]
list_tuple.append((5,6))
print("list after add tuple")
print(list_tuple)
# output == [1, 2, 6, 5, 9, 85, 12, (5, 6)]


# ".append()" add evey thing end of the list 
# but when we want to add somewhere that we want 
# we have to use ".insert()"
list_insert = [12,43,67,58,14] 
print(list_insert)
# output == [12,43,67,58,14]

# for writing insert 
# first we have to write list name 
# second write ".insert()"
# third in bracket we have to write sit place that we want and write "," after that
# !!do not forget python is zero index!!
# fourth you have to write something that you want to sit in list
list_insert.insert(3, "nima")
list_insert.insert(0, 9)
print(list_insert)
# output == [9, 12, 43, 67, 'nima', 58, 14]

# we can also print something that we want in list
list2 = [3,6,5,98,52,36,62,42,59,85]
# this print , print all the list
print(list2)
# output == [3,6,5,98,52,36,62,42,59,85]

# but this print write something that i want
# this print write second place in list
print(list2[2])
# output == 5


# when you want write last place of the list 
# you have to write -1 when you want to write one left to last you have to liste -2 and .....
list3 = [3,6,5,98,52,36,62,42,59,8,65]
print(list3)
# output == [3, 6, 5, 98, 52, 36, 62, 42, 59, 8, 65]

# it write last place in list 
print(list3[-1])
# output == 65
print(list3[-3])
# output == 59

# but when we have to remove something in list what do we have to do?
# we have to use ".remove()"
list_remove = [1, 8, 5, 9, 2, 3, 62, 98, 59, 8, 65]
print(list_remove)
# output == [1, 8, 5, 9, 2, 3, 62, 98, 59, 8, 65]
# for removing something in list we have to do this
# first we have write list name
# second write ".remove()"
# third in bracket write something you want to remove it
list_remove.remove(5)
print(list_remove)
# output == [1, 8, 9, 2, 3, 62, 98, 59, 8, 65]
# there is not any 5 in list


# when you want to remove a pace that you want
# you have to use "pop()"
list_pop = [1, 7, 5, 9, 3, 2, 62, 98, 59, 8, 65]
print(list_pop)
# output == [1, 7, 5, 9, 3, 2, 62, 98, 59, 8, 65]

# for writing "pop" 
# first you have to write your list name
# second you have to write ".pop()"
# third in bracket you have to write place that you want remove it 
list_pop.pop(2)
list_pop.pop(7)
print(list_pop)
# output == [1, 7, 9, 3, 2, 62, 98, 8, 65]
# there is not any 5 and 59


# you can also sort your list
# with using "sort()" command
list_sort = [5,8,2,4,6,7,3,1,58,56,15,29,64,75,26]
# this print write list messed up 
print(list_sort)
# but this command my list will be sort
# how to write it?
# first write list name 
# second write ".sort()"
list_sort.sort()
print(list_sort)
# output == [1, 2, 3, 4, 5, 6, 7, 8, 15, 26, 29, 56, 58, 64, 75]


# you can also reverse your list 
# with ".reverse()" command
list_reverse = [1, 7, 9, 3, 2, 62, 98, 8, 65]
# this print write list as it same 
print(list_reverse)
# output == [1, 7, 9, 3, 2, 62, 98, 8, 65]

# how write ".reverse()"
# first you have write list name
# second you have to write ".reverse()"
list_reverse.reverse()
print(list_reverse)
# output == [65, 8, 98, 62, 2, 3, 9, 7, 1]
# now it reverse

# you can also sums your number in list
list_sum = [1, 8, 9, 2, 3, 62, 98, 59, 8, 65]
# for creat this command  
# you have to write it in you "print"
# how?
print(sum(list_sum))
# like this
# output == 315


# we can also write minimum and maximum in list
list_min_max = [1, 8, 9, 2, 3, 62, 0 , 98, 59, 8, 65 , 6848961984158915]
# how write it?
# you have to write it print like sum
# command is "min()"
print(min(list_min_max))
# output == 0

# command is "max()"
print(max(list_min_max))
# output == 6848961984158915



# thank you for reading (:

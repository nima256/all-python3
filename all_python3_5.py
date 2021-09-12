# hello , here i want to write code with for
# what is 'for'?
# 'for' is loop makes work easy for you , for example if you want to ..
# .. give 10 imported of your user you have to writ ..
# .. 10  , example = int(input("please enter a number")) ..
# .. to give it 
# but with 'for' you can only write one .. 
# .. example = int(input("please enter a number"))
# to give 10 imported 

# how write 'for'?
# for every_thing_you_want in "if you want it rotate in list ..
# you have to write your list name  if you dont you have to
# write" range(number that you want your loop rotate) :
# lets see 


# when you print your variable that in it you ask user to ..
# .. enter number it only give you last number that user enter it
# if you want to have all of the number that user enter it ..
# you have to do this

# you have to creat 2 variable
a = []
number = []
# a loop
for x in range(10):
    # a list 
     List = int(input("please enter 10 number:"))
     # variable to saved number of user
     a = List
     # if you print a it again print last number that user enter 
     # so we bring it in another variable
     number.append(a)
print(number)
# output ==> [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]




# well , here we want to go 'for' that rotate in list
# creat a list
number2 = [-2 , 2 , 5 , 21 , -2 , 21 , 22 , -3]
# a loop
for x in number2 :
    # we say that x biger than 10 print it
    if x < 10 :
        print(x)
# output ==> -2 , 2 , 5 , -2 , -3

# with for we can write odd number and even number
# odd number 
# in range (we write start of range , we write end of range , we write turn of it)

for x in range(1 , 100 , 2):
    print(x)

# even number
for x in range(0 , 100 , 2):
    print(x)


# thanks for reading 💓

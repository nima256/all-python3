# here we want to open a file with python

# first we write 'with'
# then write 'open'
# after we open braces and open single cotation and write file name foe example =  ('test.txt')
# then we write 'as'
# after we enter a name that if you want to use it in your code you will say it with that name for---
# ---example = open_file
# after that we creat a variable to say open file
# then in variable we write file name that we enter it to use it in our code if you remember i write---
# ---'open_file' for my code
# then it should read it so we write '.read()' after our code name
# finaly we print the variable
with open('test.txt') as open_file:
    information = open_file.read()
print(information)
# output = 'hello its a test file for open file in python'     this is what i write in my txt file


# also we can wirte addres of the file insted the name of the file
# for doing this we just have to enter addres of file insted name of the file
with open('/home/nima/python3/test.txt') as open_file:
    information = open_file.read()
print(information)

# we can also do something new 
# insted using a file addres we can write file addres in a variable and we just have to write ---
# ---variable name insted file address
file = '/home/nima/python3/test.txt'
with open(file) as open_file:
    information = open_file.read()
print(information)

# also we can use for file 
# what 'for' do for us
# it do a 
#
# space for somthing that you write
file = '/home/nima/python3/test.txt'
with open(file) as open_file:
    for line in open_file:
        print(line)
# for example i write this for my file == 

# hello its a test file for open file in python
# it is 
# for 
# testing 
# space of
# for
# but it write this for me==

# hello its a test file for open file in python

# it is 

# for 

# testing 

# space of

# for



# now we can also remove the space that 'for' write it
# by 'rstrip()'
# when you want to print it add '.rstrip()' after that
file = '/home/nima/python3/test.txt'
with open(file) as open_file:
    for line in open_file:
        print(line.rstrip())
# 'for' write this ==

# hello its a test file for open file in python

# it is 

# for 

# testing 

# space of

# for

# now when i add '.rstrip()'
# it write == 

# hello its a test file for open file in python
# it is 
# for 
# testing 
# space of
# for


# thanks for reading this script 




















# python mega course on udemy
# section 2 - Variables, Datatypes and Functions

## 11 - Variables
## you can use some special characters to name a variable, but you can`t start
## the variable name with a number!
## 2greeting  is not a valid variable name

# # user interation
# user_string = input("write a personal greeting: ")
# print(user_string)

# # 12 - numbers
# # introduction to basic math operations in python
# a = 2
# b = 3
# print(a + b)
# # variable types
# print(type(a))
# print(type(2.4))
# print(type("2"))
# print(2+3)
# print("2"+"3")

# # this prints an error becaus age is setted as a string and can not be added to a number
# age = input("Enter your age: ")
# new_age = age + 50
# print(new_age)

# # you need to convert the string into an into
# age = input("Enter your age: ")
# new_age = int(age) + 50
# print(new_age)

# # 13 - Operations with numbers
# # order of operations is, power first, division and multiplication are in the same
# # priority, exectue what comes firts, and them plus and minus operations are the last ones
# print(20-10/5*3**2)
# # division returns a float
# # naturally, you can use parenthesis to define the priority of operations

# # 14 - Strings
# # defined using double quotes or single quotes
# my_string = "something written here"
# # methods associated with the string type/class
# # using . notation we can access usefull methods
# my_string = my_string.replace("e","eee")
# # note that this method doesn't modify the string object, that is why we need
# # to return it to another variable, or updtate the variable with the new string
# print(my_string)
# # how to see all methods associated with an object?
# # use the dir() function to list them all and the help function to get information
# # on specific methods
# print(dir(my_string))
# help("".replace)
# help("".ljust)

# # 15 - String indexing and spliting
# # indexing is a very important concept
# c = "Hi there!"
# # python assigns a number to each character in the string, starting from 0
# # you can access any index using square brakets, []
# print(c[0], c[4])
# # the last character can be accessed by counting from the end
# print(c[-1], c[-2])
# # to extract more than one character we use the : notation, from the first indexing
# # excluding the upper bound -> 0:1 only takes the 0 indexing
# print(c[0:1], c[0:2])
# # if you want all the interval below or above that can be done like [:4], [4:]
# print(c[:3])
# print(c[3:])

# # 16 - Lists
# # important datatype that can store multiple elements of different types
# # the elements are stored in a ordered way and each element can be accessed by an
# # unique index
# c = ["Hi", "haha", 3, "Last strin", 4.56]
# print(c)
# print(c[:2])
# print(c[2:])
# # the list is typed as list, but its specific elements can be of various types
# print(type(c), type(c[2]))
# # lists also have methods associated with them
# # you can see the entire list by using the dir function
# print(dir(c))
# print(help(c.append))
# # you can add new elements to the end of the list using the append methods
# c.append("new element to the end")
# # that will modify the existing list
# print(c)

# 17 - How to make programming questions
# not a code section
# guideline is: search on google first, usually the answer is on stackoverflow
# in case it is not there you can ask in the QA forum of the course
# put your entire code, explain what you are trying to do and what is the
# unespected result. If there is an error, copy the entire error message and post
# it with your question.

# # 18 - Tuples
# # very similar to lists. Big difference -> Tuples are not mutable!
# # syntax
# t = (1, 2, "x", "y")
# print(t[0])
# print(t[-1], t[2:], t[:2])
# # it has methods associated, but not as many as a list, as the tuple defined is
# # not mutable. You can't add or remove items to it!
# print(dir(t))
# print(help(t.index))

# # 19 - Dictionaries
# # hash list, with values associated with keys
# # not an ordered list, mutable, index associated with keys that extract specific values
# dic = {"Name":"Felipe", "LastName":"Oliveira", "Age":25}
# # "Name", "Age", etc, are the keys used for accessing the values
# # key:values
# print(dic["Name"])
# print(dic["Age"])
# # you can associate a list, or a tuple as a value for a specific key
# new_dic = {"Name":"Felipe", "LastName":"Oliveira",
#             "Age":25, "Skills":["Python", "Electronics", "Piano"],
#             "Coordinates":(43.2233, 27.5432)}
# print(new_dic["Skills"], new_dic["Coordinates"])

# # 20 - Functions
# # notation def functionname(input, variables, whatever):
# # the function code goes below
# # ex: function to convert currency
# def currency_converter(rate, euros):
#     # note the identation determins the function block
#     dollars=euros*rate
#     return dollars
#
# # you need to call the function somehow to see the results
# print(currency_converter(1.4, 500))

# # Section 3 - Dealing with Programming Errors
# # new course section added later on
# # that is why the numbering of the sections is strange
# # 3.1 - Syntax Errors
# # To understand the errors that occur when running a code is very important
# # There are basically two types of errors? Syntax and Exception errors
# # in the error log, printed into the terminal, python points to the token that has
# # an error. It can point either to the end of the token (line\comand) or to the
# # begining. Sometimes the syntax error is right before the pointed statement
#
# # 3.2 - Runtime Errors
# # Exceptions are runtime errors
# # the python interpreter looks for syntax errors first, and then starts running
# # the code and executing the comands. It will run every statement before an
# # exception errors, that is why they are called ruintime errors.
# # The exception erros can be one of many different kinds, type, name, zero division
# # are possible examples of kinds of errors.
#
# # 3.3 - Fixing Difficult Errors
# # Method for fixing errors: coppy error message (last line) and search on google
# # usually the answer is on stackoverflow forum
# # If it is not ask a question, in a well structured way.
#
# # 3.4 - The Structure of a good Programming question
# # that class has already been done...
#
# # 3.5 - Exception Handling in Python
# # The syntax is
# try:
#     # ... code you want to try to execute bellow
#     a = 'a'
#     b = 2
#     print(a+b)
# # in case that the code you put in try gives a runtime error the except statement
# # is going to run
# except:
#     # you can specify the kind of the error to deal, using except NameOfTheError:
#     # when the error name is not specified it will accept all kinds of errors
#     # what to do in case of an error
#     print('it is not possible to sum {} and {}'.format(a,b))

# Section 4 - Functions and Conditionals
# 21 - Section introduction
# functions are usefull to make a modular organize code
# you can write a function to deal with codes that are repeated multiple times
# conditionals are the ways to make your code to make decisions, giving different outputs
# depending on variables values or specific conditions previously setted

# # 22 - Functions: the basics
# # ex: minutes to hours currency_converter
# def min_2_hours(minutes):
#     return minutes/60
#
# # call the function to return the float number of hours
# print(min_2_hours(820))
# # print is a built in function, as the functions that we define are custom

# # 23 - Advanced Function Features
# # function with multiple parameters
# def min_sec_2_hours(minutes, seconds=0):
#     return minutes / 60 + seconds / 3600
#
# # we have to pass both parameters, otherwise we will have an error
# # we can make an argument optional by assigning a default value to it
# # like def myfunc(arg1, optional=somevalue):
# print(min_sec_2_hours(360, 320))
# print(min_sec_2_hours(360))
#
# # the function is not required to return some value
# # you can have a function that returns nothing, but might modify some variables
# # or print something directly
# def print_sometext(text):
#     print(text)
#
# print_sometext("this is my special secret: ...")

# # 24 - Functions and user input
# def age_foo(age):
#     print("The age you passed is: {}".format(age))
# age = input("Enter your age: ")
# age_foo(age)

# 25 - Exercise note
# nothing here...

# # 26 - Coding Exercise 1
# # create a function that converts celsius degrees into fahrenheit
# def celsius_2_fahrenheit(temp_celsius):
#     return temp_celsius*1.8+32
# # test the function
# def test_function():
#     test_list = [(30, 86), (0, 32), (-40, -40)]
#     for C,F in test_list:
#         if (celsius_2_fahrenheit(C)!=F): return "Your function doesn't work!!"
#     return "Your function seems to be working properly!"
# print(test_function())
#
# # 27 - Solution
# def c_2_f(c):
#     f=c*9/5+32
#     return f
# print(c_2_f(10))

# # 28 - Coding Exercise 2
# # print number 10 from the following dictionay
# money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
# print(money["under_bed"][1])
#
# # 29 - Solution 2
# # two ways
# # first
# lst=money["under_bed"]
# print(lst[1])
# # second
# # the exat samething I wrote
# print(money["under_bed"][1])

# # 30 - Conditionals
# # decision making statements
# a = int(input("Tell me your age: "))
# if a<5:
#     print("you are still a toddler!")
# elif a>=5 and a<=14:
#     print("you are still a child")
# else:
#     print("you are not a child or a baby anymore")

# 31 - Conditionals: Advanced
# this is supposed to be an advanced contitional tutorial
# I am not going to write anything here if it doesn't have anything new for me
# nope, absolutely nothing new here...
# it is a disgrace to call this advanced...

# # 32 - Coding Exercise 3
# # modify the temperature conversion function to display a message in case the
# # input passed is lower then -273.15°C
# def c_2_f(c):
#     if c>=-273.15: return c*1.8+32
#     return "That is not a valid temperature, it is bellow absolute zero!"
# print(c_2_f(-270),c_2_f(-40),c_2_f(-274))
#
# # 33 - Solution 3
# # basically the same code I wrote, but with more lines

# # 34 - Loops
# # a way to repeat a statement or a bunch of lines of code multiple times
# # you can execute those lines inside the loop a specific number of times
# # or check for a condition being met to stop the loop
# # You can use a loop to iterate trhough list, array, dictionay or tuple elements
# # a while loop execute the code inside it as long the chosen condition is method
# # a for loop execute a specific number of times
#
# # 35 - For Loops
# # several types of objects can be seen as iterables!
# # for example, you can iterate trhough all caracters in a string, or elements in a list
# # you can put conditions in the loop, call functions, or execute any other code or statement
# for char in "This is a big big big big string that seems to never end":
#     if char == 'b': print("Hahaha")
#     else: print(char)
#
# # you can check if some item, char, element is in a list, or iterable with
# # the in operator
# emails = ["m@gmail.com", "you@hotmail.com", "they@gmail.com"]
# for email in emails:
#     # checking if the string 'gmail' is in the list element, which is an email address
#     if 'gmail' in email:
#         print(email)

# # 36 - User input
# # a way to interact with users
# # the lesson from the tutorial was boring, I wrote this code instead
# secret_password = "I want to be a Python Master!"
# typed_password = input("Type the ultra secret password to have access to this program: \n")
# correct = secret_password==typed_password
# print("The password that you type was: {}\n".format(typed_password))
# if correct:
#     print("That is correct, you may enter!")
# else:
#     print("That is not the right password. Go away!")

# # 37 - While Loops
# # check if the password typed is correct, dynamically
# password = ""
# correct_password = '12345'
# while password != correct_password:
#     password=input("Enter the password: ")
#     if password == correct_password:
#         print("You are logged in!")
#     else:
#         print("sorry, try again...")

# # 38 - For loop with multiple lists
# # sometimes it is useful to iterate through multiple lists at the same times
# # that can be acomplished with the zip function
# names=['jim','ken','john']
# emails = ['gmail','hotmail','yahho']
#
# for name, email in zip(names,emails):
#     print("{}@{}.com".format(name,email))]

# # 39 - Coding Exercise 4
# # consider the following list
# temperatures = [10,-20,-289,100]
# # iterate over the temperature converter funciton and print the outputs
# def c_2_f(c):
#     if c>=-273.15: return c*1.8+32
#     return "That is not a valid temperature, it is bellow absolute zero!"
#
# for temp in temperatures:
#     print(c_2_f(temp))
#
# # 40 - Solution 4
# # an uglyer compact version of my code

# Section 5 - Introduction of File Handling
# 41 - Introduction to file Handling
# open, write and modify text files

# # 42 - Opening and reading a file
# # big video! Hahaha
# # lets say you want to send automatic e-mails based on a template text file
# # you need to open and read that file to acomplish that
# # We can use python to handle binary files (.dll) or text files (.tex)
# # binary files are incomprehensible, so usually we will be working with text files
# # first thing is open the file using the open method
# # we want to open the file to read on it, so we have to pass an argument 'r', meaning
# # that we are reading it. for writing it will be 'w'
# # you can omit the path for the file if you are executing in the same path as the file you're Opening
# file=open("text_file.txt",'r')
# # you can see that file is a text wrapper type
# print(type(file))
# # to pass the content of the file to a variable that we can work on, we will use the read method
# content = file.read()
# # you can see that the content is stored as a string, so it is easy to manipulate it
# print(type(content))
# print(content)
# # if the file is too big it might be a good ideia to pass each line as an element to a list
# # we can't do that in sequence because the pointer of the reader method already finished the file
# # so it will read an empty list
# content = file.readlines()
# print(content)
# # we have to come back to pointing to the beginning of the file to be able to read all the lines
# file.seek(0)
# content = file.readlines()
# print(content)
# # you have the new line character beeing recorded, \n
# # if we don't want that we need to have a differnt strategy
# # or we can strip down the \n characters from the existing list
# # using list comprehension notation
# content = [line.rstrip("\n") for line in content]
# print(content)
# # it is always a good ideia to close the file after working with it
# file.close()
# # alternativly you can do, and not having to worrry about closing the file
# content = []
# with open("text_file.txt", 'r') as file:
#     for line in file:
#         content.append(line.rstrip("\n"))
#
# print(content)

# # 43 - Writing text to a file
# # create a file with python and store it in a variable
# file = open('write_text.txt','w')
# file.write("Line 1\n")
# file.write("Line 2\n")
# file.close()
# # to add more lines we need to append new content into the file
# # opening the file again and writing into it would overwrite the content previously written
# content_list = ["{} squared is equal to {}".format(i, i**2) for i in range(201)]
# file = open('write_text.txt','w')
# for el in content_list:
#     file.write(el+"\n")
# file.close()

# # 44 - Appending to a text file
# # adding new elements to the end of the file we need to use the argument 'a' instead of 'w' or 'r'
# file = open('write_text.txt', 'a')
# file.write("That all for now folks!")
# file.close()

# 45 - The rest of file handling methods
# all the possible arguments for opening a file:
# 'r' opens for read only
# 'r+' opens for read and write. Doesn't overwrite the existing file.
# 'w' opens for read only
# 'w+' opens a file for writing and reading. Overwrite the existing file.
# 'a' opens a file for appending. The file pointer would be in the end of the file
# 'a+' opens a file for appending and reading

# # 46 - The with statement
# # you don't need to worry about close the file
# # it is a better practice for pythonic clean code
# with open('text_file.txt', 'a+') as file:
#     # the pointer is in the end of the file
#     # so we will not read anything with the read methods
#     # we need to go back to the begining, using seak
#     file.seek(0)
#     content=file.read()
#     file.write("Line4")
#
# print(content)

# # 47 - Coding Exercise 5
# # create a text file that stores the temperatures converted from celsius to fahrenheit
# # invalid temperatures are not supposed to be written
# t_c = [10, -20, -289, 100]
# with open('ex_5.txt', 'w') as file:
#     file.write("".join(["{}\n".format(c*1.8+32) for c in t_c if c>-273.15]))
# # 48 - Solution 5
# # it uses a function to write the the file and then calls the function with the temperature list
# # it uses 8 lines of code to do something that only takes 3 lines....
# temperatures=[10,-20,-289,100]
#
# def writer(temperatures):
#     with open("temps.txt", 'w') as file:
#         for c in temperatures:
#             if c>-273.15:
#                 f=c*9/5+32
#                 file.write(str(f)+"\n")
#
# writer(temperatures)

# Section 6 - More Funcionalities
# 49 - Introduction
# using external libraries, handling dates and time, comment code

# # 50 - Modules, libraries and Packages
# # there are a lot of external libraries
# # it is not a good idea to load them all into memory
# # we only load the external libraries that we are going to use for that specific script
# # to do that we use the import statement
# import os
# # get a list with all the file names in the current directory
# os.listdir()
# # all methods
# print(dir(os))
# # we can see all the modules and libraries avalible in the lib directory in the python instalation
# # and we can open those files and see the code in it
# # the list of all installed modules can be seen with the following:
# help('modules')
#
# # packages are 3 party modules
# # you can install these modules using pip comand in the apropriate folder
# # We have to open the cmd line in the python installation folder, specifically the Scripts folder
# # inside the python installation folder
# # in the comand line just type pip module_name to install any module
# # you need to know the exat package name and sometimes the version as well

# # 51 - Commenting and documenting your code
# # use # char to add any comment related to the code
# # you can use it to explain parts of your code
# # it is a good practice to add a comment before a function to explain its use and functionalities
# # doc strings are the documentation related to a module, method, function or file
# # we can access that with the module_name.__doc__ command
# # we can write it with triple quotes
# """ This is a doc string
#     it can have multiple lines
#     We can write a big text here
# """
# import module_ex
# print(module_ex.__doc__)
# # or you can access the doc string of fuctions within your module_ex
# print(module_ex.dummy_function.__doc__)

# # 52 - Wroking with Dates and Times
# # Lets say you want do a program to create files automatically every datatype
# # and put the date in the file name
# # We can use date and time objects to do that
# # we have basically two modules for that
# # datetime and time
# import datetime as dt
# # datetime is a module, we can import it as a shorter variable name for convenience
# # in the datetime module we have a datetime class, which contains several usefull methods
# # now is one of those methods, and it returns the current date and time from the computer
# print(dt.datetime.now())
# # lets say you want the difference of the current time and a specific time
# # we create a datetime object and perform subtraction operations with it
# other_time = dt.datetime(2017,5, 16, 12, 0)
# difference = dt.datetime.now()-other_time
# print(difference)
# # we can access only the days, or have it in total seconds
# print(difference.days)
# print(difference.total_seconds())
# # we can have a custom formating of the time using the strftime methods
# time_now = dt.datetime.now()
# print(time_now.strftime("%Y-%m-%d-%H-%M"))
#
# # so, lets write now a script that creates txt files with the current date as the name
# current_time=dt.datetime.now()
# filename = "{}-{}-{}_dt-sample.txt".format(current_time.year, current_time.month, current_time.day)
# # or
# filename = "{}_dt-sample.txt".format(current_time.strftime("%Y-%m-%d"))
# # function to create empty files
# def create_file():
#     with open(filename,'w') as file: file.write("")
#
# create_file()
#
# # we can add specific time intervals to a date by using the timedelta method
# print(dt.datetime.now()+dt.timedelta(days=2, hours=6))
#
# # we also have the module time
# # useful for delaying operations, waiting specific amounts of time
# # and measuring code running time
# import time
# # add datetime to a list separated by 2 seconds intervals
# time_list = []
# for i in range(5):
#     time_list.append(dt.datetime.now())
#     time.sleep(2)
# for el in time_list:
#     print(el)

# # 53 - Coding Exercise 6: Merging Text Files
# # download the zip file containing the 3 text files for this Exercise
# # write a script that merges all three files into a new text file
# # the file name should be the current timestamp down to the millisecond level
# # like "2017-06-01-13-57-39-170965.txt"
# import datetime, os
# # save the current project directory
# project_path, _ = os.path.split(os.path.abspath(__file__))
# print(project_path)
# # change the dir to the folder with the text files
# os.chdir(r".\Ex 6")
# # create an empty list to store those files
# content_list = []
# # iterates through all files in that folder and save the content into the list
# for f in os.listdir():
#     with open(f, 'r') as file:
#         content_list.append(file.read())
# # defines the new file name based on the current time
# now_object = datetime.datetime.now()
# file_name = "{}.txt".format(now_object.strftime("%Y-%m-%d-%H-%M-%S-%f"))
# # change the dir again to the original project folder
# os.chdir(project_path)
# # creates a new file to store the content
# with open(file_name, 'w') as file:
#     for el in content_list:
#         file.write(el+"\n")
#
# # 55 - Solution 6
# # it uses glob2.glop to get the file names
# # saves the new file into the samefolder
# # so it can iterate through the files to read without saving the content into a list
# # puting it directly into the new file
# # much cleaner solution but you have to be carfully running the code multiple times as
# # the content from the new gereneated file will be stored into the new ones
# import glob2
# import datetime
#
# filenames=glob2.glob("*.txt")
#
# with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
#     for filename in filenames:
#         with open(filename,"r") as f:
#             file.write(f.read()+"\n")

# print("Time passing in training!")

# a=20
# print(type(a))

#de = "nothing to do"
# print(de.upper())
# print(de.strip())
# print(de.lstrip())
# print(de.rstrip())
# print(de.title())
# print(de.removeprefix("nothing"))
# print(de.removesuffix("do"))

# string = "Time passing in training"
# print(string[0:20:1])
# print(string[-1:-20:-1])

# lst = [1,2,"Daya",False,30.30]
# print(type(lst))
# print(lst)
# lst.append(4)
# print(lst)
# print(lst.extend(["green","yellow"]))
# print(lst)

# lst2 = [3,2,7,8,1,4]
# lst2.sort(reverse=True)
# print(lst2)
# print(lst2[::-1])
# lst2.insert(1,9)
# print(lst2)
# lst2.insert(1,9)
# print(lst2)
# lst2.pop(1)
# lst2.remove(4)
# print(lst2)

# tpl = (1,)
# print(type(tpl))

# set1 = {1,2,True,"daya","daya"}
# print(set1)

# dct = {
#     "name":"dayachand",
#     "age":19,
#     "year":2025,
#     "DEPT":"CSE"
# }
# print(dct)
# print(dct["age"])
# print(dct)
# print(dct.keys())
# print(dct.values())
# dct.update({"DEPT":"CSE","Branch":"AI & ML"})
# print(dct)

# for i,y in dct.items():
#     print(i,y)


# Odd or Even
# n = int(input("Enter a number:"))
# if(n%2 == 0):
#     print("Given number is even")
# else:
#     print("Given number is odd")


# Prime number programe
# n = int(input("Enter a number:"))
# for i in range(2,n-2):
#     if(n%i == 0):
#         print("Given number is non Prime")
#         break
#     else:
#         print("Given number is a prime number")


# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     if(i == 5):
#         continue
#     if(i == 9):
#         break
#     print(i,end=' ')

# i=1
# while i<6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# check how many times a given number can be devided by 3
# before it is less than or equal to 10
# n = int(input("Enter a number n:"))
# count = 0
# while(n > 10):
#     n /= 3
#     count += 1
# print(count)


# lst = [1,2,3,4,5,6,7]
# size = len(lst)
# i=0
# while(i<size):
#     print(lst[i])
#     i += 1


# def hello():
#     print("hello from function")
# hello()

# def name(fname):
#     print("hello!",fname,"here")
# name("daya")


''' Arbitary Arguments(args*) -> When we don't know that how many arguments, we have to pass'''
# def my_function(*kids):
#     print("The youngest child is",kids[2])

# my_function("mohan","rohan","sohan")


'''Keyword Arguments -> When we pass the arguments's value as a key value pair'''
# def children(child1,child2,child3):
#     print("The youngest child is",child2)

# children(child2="mohan",child3="rohan",child1="sohan")


''' Arbitary keyword Arguments(**kwargs)'''
# def children(**child):
#     print("The youngest child is",child["fname"])

# children(fname='Lodu',lname='Lalit')

'''Default parameter Value'''
# def name2(name='India'):
#     print("my country is",name)
# name2()

# def avR(lst):
#     return sum(lst)/len(lst)

# lst=[1,2,3,4,5,6]
# print(avR(lst))


# def sqrList(lst):
#     newLst = []
#     for i in lst:
#         newLst.append(i*i)
#     return newLst
# lst = [1,2,3,4,5]
# print(sqrList(lst))


''' map() function -> (function,iterable)'''
# lst = [1,2,3,4,5]
# newl = list(map(lambda a:a*a,lst))
# print(newl)

'''filter() function -> (function.iterable)'''
# def ff(a):
#     return a%2 == 0
# lst = [2,5,4,7,6,1]
# newl = list(filter(ff,lst))
# print(newl)


''' reduce() function'''
# from functools import reduce
# lst = [2,3,4,5,6,7]
# newl = reduce(lambda x,y:x+y,lst)
# print(newl)


'''enumerate() function'''
# name = ["python","java","c"]
# enum_list = list(enumerate(name))
# print(enum_list)


''' Modules Vs Package Vs Library '''
# Modules -> Files of python which is written by another and we uses it in our programe.
#            (built-in,user-def,third-party)
# Packages -> Package is a directory which is the Collection of modules.
# Library -> Combination of modules and packages.

#import os 
# print(os.getcwd())
# print(os.listdir())
# os.chdir(r'C:\Users\DAYACHAND\OneDrive\Desktop\javap')
# print(os.getcwd())
# os.mkdir('test1')
# os.rmdir('test1')
# os.chdir(r'C:\Users\DAYACHAND\OneDrive\Desktop\Training')
# print(os.getcwd())
# os.makedirs("parentf/childf")
# os.removedirs("parentf/childf")


''' To import in _init_ file'''
# def add(a,b):
#     return a+b


''' Exception handling -> try,except,else,finally'''
# try:
#     print(10/0)
# except Exception as e:
#     print("Exception:",e)
# else:
#     print("ok")
# finally:
#     print("Exception handled")


''' File Handling '''
# b -> binary files
# + -> read and write

# ->
# file = open("demo.txt","r")
# print(file.read())
# file.close()

# ->
# with open("demo.txt","r") as file:
#     print(file.read())
#     print(file.readline())
#     print(file.readlines())

# ->
# with open("demo.txt","w") as file:
#     file.write("Good guy")

# creating a JSON file ->
import json
data = {
    "name":"upflairs",
    "year":2020
}
# with open ("data.json","w") as file:
#     json.dump(data,file)

# with open ("data.json","r") as file:
#     content = json.load(file)
#     print(content)

### Create a csv file
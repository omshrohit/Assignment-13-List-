# write a python script to create  a list,where each elements of  the list is a digit of a given number.

list=[eval(element) for element in   input("enter the digits seperated by comma").split(",")]
print(list)
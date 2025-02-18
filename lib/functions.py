#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return(num1 + num2)

#   If the function is called with an argument that isn't a number, it should return null:
#   const result = halve("two")
#   => null

def halve(number):
    if type(number) not in [float, int]: 
        return (None)
    return number / 2


print(halve(4))
print(halve("4"))
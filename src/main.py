#BINARY DECIMAL TWO WAY CONVERTER SOURCE CODE
#WRITTEN BY JOSH PHILIP

import os
import time

def binaryToDecimal(binary):
    if binary == "":
        raise ValueError("INVALID INPUT DETECTED")
    nums = [int(x) for x in binary]
    nums.reverse()
    decimal = 0
    for num in nums:
        if num != 0 and num != 1:
            raise ValueError("INVALID INPUT DETECTED")
    for idx in range(len(nums)):
        decimal = decimal + (nums[idx] * (2 ** idx))
    return decimal

def decimalToBinary(decimal):
    acc = []
    if decimal == 0:
        return "0"
    while(decimal != 0):
        acc.append(decimal % 2)
        decimal = decimal // 2
    acc.reverse()
    binary = ""
    for x in acc:
        binary = binary + str(x)
    return binary

def ones_complement(binary):
    if binary == "":
        raise ValueError("INVALID INPUT DETECTED")
    nums = [int(x) for x in binary]
    nums.reverse()
    decimal = 0
    for num in nums:
        if num != 0 and num != 1:
            raise ValueError("INVALID INPUT DETECTED")
    for idx in range(len(nums)):
        if idx == len(nums) -1 and nums[idx] == 1:
            decimal = decimal + (nums[idx] * ((-2 ** idx) + 1))
        else:
            decimal = decimal + (nums[idx] * (2 ** idx))
    return decimal

def twos_complement(binary):
    if binary == "":
        raise ValueError("INVALID INPUT DETECTED")
    nums = [int(x) for x in binary]
    nums.reverse()
    decimal = 0
    for num in nums:
        if num != 0 and num != 1:
            raise ValueError("INVALID INPUT DETECTED")
    for idx in range(len(nums)):
        if idx == len(nums) -1 and nums[idx] == 1:
            decimal = decimal + (nums[idx] * (-2 ** idx))
        else:
            decimal = decimal + (nums[idx] * (2 ** idx))
    return decimal

def run_converter(decision):
    string = "ynYN"
    if(decision == 4):
        while(True):
            print("TWO'S COMPLEMENT CALCULATOR")
            binary = input("Enter a binary string: ")
            decimal = twos_complement(binary)
            print(binary + " in two's complement is " + str(decimal))
            cont = input("Continue? (y/n): ")
            if(cont not in string):
                raise ValueError("INVALID INPUT")
            print("\n")
            if(cont == 'n' or cont == 'N'):
                break
    elif(decision == 3):
        while(True):
            print("ONES' COMPLEMENT CALCULATOR")
            binary = input("Enter a binary string: ")
            decimal = ones_complement(binary)
            print(binary + " in ones' complement is " + str(decimal))
            cont = input("Continue? (y/n): ")
            if(cont not in string):
                raise ValueError("INVALID INPUT")
            print("\n")
            if(cont == 'n' or cont == 'N'):
                break
    elif(decision == 2):
        while(True):
            print("DECIMAL TO BINARY CONVERTER")
            decimal = int(input("Enter a number: "))
            binary = decimalToBinary(decimal)
            print(str(decimal) + " in binary is " + binary)
            cont = input("Continue? (y/n): ")
            if(cont not in string):
                raise ValueError("INVALID INPUT")
            print("\n")
            if(cont == 'n' or cont == 'N'):
                break
    elif(decision == 1):
        while(True):
            print("BINARY TO DECIMAL CONVERTER: ")
            binary = input("Enter a binary string: ")
            decimal = binaryToDecimal(binary)
            print(binary + " in decimal is " + str(decimal))
            cont = input("Continue? (y/n): ")
            if(cont not in string):
                raise ValueError("INVALID INPUT")
            print("\n")
            if(cont == 'n' or cont == 'N'):
                break

    else:
        raise ValueError("INVALID INPUT")
os.system("cls" if os.name == 'nt' else "clear")             
print("Welcome to my really cool and awesome program!")
print("\n")
time.sleep(2)
while(True):
    os.system("cls" if os.name == 'nt' else "clear")
    print("------------ THE BINARY DECIMAL TWO-WAY CONVERTER ----------------")
    print("\n")
    print("Choose one of these 4 options:")
    decision = input("Enter 1 for Binary-to-Decimal:\nEnter 2 for Decimal-to-Binary:\nEnter 3 for Ones' Complement of Binary String\nEnter 4 for Two's Complement of Binary String\n")
    print("\n")
    os.system("cls" if os.name == 'nt' else "clear")
    run_converter(int(decision))
    zero = int(input("Type 0 if you want to end the program (Type 1 if you still want to play): "))
    print("\n")
    if(zero == 0):
        break
    elif(zero == 1):
        os.system("cls" if os.name == 'nt' else "clear")
        
os.system("cls" if os.name == 'nt' else "clear")

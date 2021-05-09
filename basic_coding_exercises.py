#1. Calculate the sum of three given numbers if given numbers is equal then their sum should be twice the sum

# def summing(a, b, c):
#     result = 0
#     if a == b == c:
#         result = 2*(a+b+c)
#     else:
#         result = (a+b+c)
#     return result
#
# a = int(input("Please enter the number1: "))
# b = int(input("Please enter the number2: "))
# c = int(input("Please enter the number3: "))
# print("The sum of three numbers is : ",summing(a,b,c))
#
# #2. Calculate the square root of a number
# import math
# def square_root(num):
#     return math.sqrt(num)
# print("The square root of the number is : ",square_root(25))


#3 Retrun the quotient and the remainder
# def quot_rem(dividend, divisor):
#     try:
#         quotient = dividend/divisor
#         remainder = dividend%divisor
#         return "q= {}, r = {}".format(round(quotient,2), remainder)
#     except:
#         return "Enter divisor greater than zero"
#
# print(quot_rem(179, 176))

# print(quotient_remainder(20, 0))

#4 check whether a number is even or odd
# def even_odd_check(num):
#     try:
#         if num%2 == 0:
#             return "Even Number"
#         else:
#             return "Odd Number"
#     except Exception as exc:
#         # return exc.args
#         return exc
#
# print(even_odd_check({10}))

#5 Determine the factors of a number
# def factors(number):
#     factors_result = []
#     non_factors = []
#     for num in range(1, number+1):
#         if number%num == 0:
#             factors_result.append(num)
#         else:
#             non_factors.append(num)
#     return "The factors for the number is : {}".format(factors_result)
#
# number = int(input("please enter any number for finding out the factors: "))
# print(factors(number))

#6 Find the power of any number x^y
# def power_of_any_number(number, power):
#     return number ^ power
#
# print(power_of_any_number(10, 3))

# rounding of the decimal part if no decimal part then should display Integer
# def display_decimal(num):
#     result = round((num%1),2)
#     if result != 0:
#         print("Yes it is decimal")
#         print(str(result)[-2:])
#     else:
#         print("It is Integer")
# display_decimal(1.02)

# calculate the number of numerical numbers in a string

def str_add(str1):
    result = 0
    for i in str1:
        if i.isnumeric():
            result += int(i)

    print(result)

str_add("cha1245")

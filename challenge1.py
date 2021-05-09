# To Calculate the sum of three given numbers
# if the variables are equal then sum should be double

# def sum_of_three(a,b,c):
#     result = 0
#     if a == b == c:
#         result = 2*(a+b+c)
#     else:
#         result = a+b+c
#     print("The result of three is : ",result)
#
# sum_of_three(10,10,20)

# To Swap two strings
#ex: s1 = '123456' S2 = 'abcdef'

def swap_two_strings(s1,s2):
    #first way
    # s1,s2 = s2,s1
    #second way
    temp = s1
    s1 = s2
    s2 = temp
    print("Swapped results is s1: {}, s2: {}".format(s1,s2))

s1 = '12345'
s2 = 'abcde'
swap_two_strings(s1,s2)
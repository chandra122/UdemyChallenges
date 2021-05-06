# To Calculate the sum of three given numbers
# if the variables are equal then sum should be double

def sum_of_three(a,b,c):
    result = 0
    if a == b == c:
        result = 2*(a+b+c)
    else:
        result = a+b+c
    print("The result of three is : ",result)

sum_of_three(10,10,20)
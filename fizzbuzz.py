def fizz_buzz(num):
    if(num <= 0):
        return ""
    return fizz_buzz(num-1)+str(fizzer(num))
def fizzer(n):
    if (n % 15 == 0):
        return "fizzbuzz" 
    elif (n %  3 == 0):
        return "fizz"
    elif (n %  5 == 0):
        return "buzz" 
    else:
        return n
print(fizz_buzz(100))







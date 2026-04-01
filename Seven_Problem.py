def prime_fact(num):
    if num <=2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i*i <= num:
        if num %i ==0:
            return False
        i+=2
    return True
num=1 #int(input("Enter the number:"))
count = 0
while count < 10001:
    num+=1
    if prime_fact(num):
        count +=1
print(num)
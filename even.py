def summation_prime(num):
    if num < 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
count = 2000000
total = 0

for i in range(2,count):
    if summation_prime(i):
        total+=i
print(total) 
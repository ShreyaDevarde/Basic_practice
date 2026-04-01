def evenly_divisible(number):
    for i in range(1,21):
        if number % i !=0:
            return False
    return True
number = 1
while True:
    if evenly_divisible(number):
        break
    number+=20
print(number)      
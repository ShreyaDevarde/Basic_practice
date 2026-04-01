def palindrome(num):
    return str(num) == str(num)[::-1]
result = 0 
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if palindrome(product):
            result =max(result,product)
print("result")
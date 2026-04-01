def Odd_Squares(limit):
    
    if not isinstance(limit,int) or limit <= 0:

        raise ValueError ("Number should be positive")
        
    k = (limit + 1) // 2
    total_sum = k *(2* k  - 1) *(2 * k + 1) //3
    return total_sum
        
limit = 905000
result = Odd_Squares(limit)
print(result)
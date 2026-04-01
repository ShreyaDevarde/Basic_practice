import timeit

s = """"HelloWorld" *1000"""
 
execution_time =timeit.timeit(stmt=s)
print(f"Execution time: {execution_time:.6f} seconds")
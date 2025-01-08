def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(3, increment) # increment no se ejecuta con () porque se pasa como parámetro
# 3 + (3 + 1) = 7
print(result) # 7

increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)

result_v2 = high_ord_func_v2(3, increment_v2)
print(result) # 7

# También se puede pasar como parámetro una función anónima lambda
result_v3 = high_ord_func_v2(3, lambda x: x * 2)
print(result_v3)
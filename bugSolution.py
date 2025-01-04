def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return "Undefined"
    elif a == 0:
        return "Division by zero"
    elif b == 0:
        return "Division by zero"
    else:
        return a / b

result = function_with_uncommon_error_solution(0, 10)
print(result)
result = function_with_uncommon_error_solution(10, 0)
print(result)
result = function_with_uncommon_error_solution(0, 0)
print(result)
result = function_with_uncommon_error_solution(10, 2)
print(result)
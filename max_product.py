def max_product(sequence: str, span: int) -> int:
    try:
        int(sequence)
    except:
        raise ValueError("El primer argumento ha de ser un número entero") 
    if span > len(sequence):
        raise ValueError("El segundo argumento no puede ser mayor que el primero")
    if span <= 0:
        raise ValueError("El segundo argumento no puede ser menor o igual a 0")
    
    max_result = 0
    for i in range(len(sequence) - span + 1):
        result = 1
        for n in sequence[i : i + span]:
            result *= int(n)
        if result > max_result:
            max_result = result
    return max_result

# def max_product(number: str, span: int, i: int, max_res: int):
#     res = 1
#     for n in number[i:i+span]:
#         res *= int(n)
#     if res > max_res:
#         max_res = res
#     i += 1
#     return max_product(number, span, i, max_res) if (len(number) - i >= span) else max_res

# print(max_product(number, span, 0, 0))
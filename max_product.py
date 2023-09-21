# import sys

# sequence = sys.argv[1]
# distance = int(sys.argv[2])

def max_product(sequence: str | int, distance: str | int) -> int:
    try:
        int(sequence)
        distance = int(distance)
    except:
        raise ValueError("Los dos argumentos han de ser números enteros")
    
    if isinstance(sequence, int):
        sequence = str(sequence)
    if distance >= len(str(sequence)):
        raise ValueError("El segundo argumento no puede ser mayor que el primero")
    if distance <= 0:
        raise ValueError("El segundo argumento no puede ser menor o igual a 0")
    
    max_result = 0
    for i in range(len(sequence) - distance + 1):
        result = 1
        for n in sequence[i : i + distance]:
            result *= int(n)
        if result > max_result:
            max_result = result
    return max_result

print(max_product("6516549", "2"))

# def max_product(number: str, distance: int, i: int, max_res: int):
#     res = 1
#     for n in number[i:i+distance]:
#         res *= int(n)
#     if res > max_res:
#         max_res = res
#     i += 1
#     return max_product(number, distance, i, max_res) if (len(number) - i >= distance) else max_res

# print(max_product(number, distance, 0, 0))
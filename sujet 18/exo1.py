def multiplication(n1, n2):
    result = 0
    if n1 == 0 or n2 == 0:
        return 0

    for _ in range(abs(n2)):
        result += n1

    if n1 < 0 and n2 < 0:
        result = abs(result)
    return result


print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

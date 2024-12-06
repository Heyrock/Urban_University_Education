digit = 'Простое'
summa = sum((2, 3, 6))
for i in range(2, summa // 2 + 1):
    if summa % i == 0:
        digit = 'Составное'
        break
print(digit)
# Простое

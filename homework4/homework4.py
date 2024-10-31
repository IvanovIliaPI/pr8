def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:

    input_a = input("Введите число a: ")
    input_b = input("Введите число b: ")

    if not (is_number(input_a) and is_number(input_b)):
        print("Некорректный ввод. Пожалуйста, введите корректные числа.")
        continue

    a = float(input_a)
    b = float(input_b)

    if a > b:
        a, b = b, a

    print("Целые числа между a и b:")
    for num in range(int(a) + 1, int(b)):
        print(num)
    break

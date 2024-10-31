def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def correct_input(user_input):
    user_input = user_input.replace(',', '.')
    correct = ''.join(filter(lambda x: x.isdigit() or x in ['-', '.'], user_input))
    return correct if correct else '0'

total = 0
while True:
    user_input = input("Введите число (или 'stop' / 'end' для завершения): ")
    if user_input.lower() in ["stop", "end"]:
        break

    corrected_input = correct_input(user_input)
    if not is_number(corrected_input):
        print("Некорректный ввод. Пожалуйста, введите корректные числа.")
        continue

    total += float(corrected_input)
print("Сумма введённых чисел:", total)

def main():
    while True:
        try:
            num1 = int(input("Введите первое целое число (Любой не корректный ввод приведет к выходу из программы): "))
            num2 = int(input("Введите второе целое число (Любой не корректный ввод приведет к выходу из программы): "))
            result = num1 + num2
            print(f"Сумма: {result}")
        except ValueError:
            print("Вы вышли из программы.")
            break
main()
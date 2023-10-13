


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка"

print("Выберите действие :")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")

d = input("Введите действия: ")

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)

    if d == 'Сложение':
        print(num1, "+", num2, "=", add(num1, num2))
    elif d == 'Вычитание':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif d == 'Умножение':
        print(num1, "*", num2, "=", mult(num1, num2))
    elif d == 'Деление':
        print(num1, "/", num2, "=", div(num1, num2))
    else:
        print("Неверный ввод")
else:
    print("Неверный ввод чисел")
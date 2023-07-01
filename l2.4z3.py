operations = []

def deposit(amount):
    global balance
    balance += amount
    operations.append(f"Пополнение: +{amount} у.е.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Ошибка: Сумма снятия превышает доступные средства.")
        return
    
    if amount % 50 != 0:
        print("Ошибка: Сумма пополнения и снятия должна быть кратной 50 у.е.")
        return
    
    if amount > 5000000:
        amount -= amount * 0.1

    if amount < 30:
        print("Ошибка: Сумма снятия слишком мала.")
        return

    if amount > 600:
        print("Ошибка: Сумма снятия слишком велика.")
        return
    
    fee = amount * 0.015
    if fee < 30:
        fee = 30
    if fee > 600:
        fee = 600
    
    balance -= (amount + fee)
    operations.append(f"Снятие: -{amount} у.е., комиссия: -{fee} у.е.")

def calculate_interest():
    global balance
    interest = balance * 0.03
    balance += interest
    operations.append(f"Начисление процентов: +{interest} у.е.")

def print_balance():
    global balance
    print("Текущий баланс: ", balance)

def print_operations():
    print("Операции поступления и снятия средств:")
    for operation in operations:
        print(operation)

def start_program():
    global balance
    balance = 0

    while True:
        print("Доступные действия:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Введите сумму пополнения: "))
            if amount % 50 == 0:
                deposit(amount)
                calculate_interest()
            else:
                print("Ошибка: Сумма пополнения должна быть кратной 50 у.е.")
            print_balance()

        elif choice == "2":
            amount = float(input("Введите сумму снятия: "))
            if amount % 50 == 0:
                withdraw(amount)
                calculate_interest()
            else:
                print("Ошибка: Сумма снятия должна быть кратной 50 у.е.")
            print_balance()

        elif choice == "3":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: Неверный выбор действия.")
            print_balance()

start_program()
print_operations()

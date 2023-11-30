import time

def Task1():
    n = int(input("input n: "))
    print(n > 100)

def Task2():
    x = int(input("input x: "))
    y = int(input("input y: "))

    if x > y:
        print("x > y")
    elif x < y:
        print("x < y")
    else:
        print("x = y")

def Task3():
    msg = str(input("input message\t"))
    x3 = int(0);
    while x3 == 0:
        if msg == "Spathiphyllum":
            print("Yes - Spathiphyllum is the best plant ever!")

        elif msg == "spathiphyllum":
            print("No, I want a big Spathiphyllum!")

        elif msg == "exit":

        else:
            print(f"Spathiphyllum! Not {msg}")
        x3 = x3 + 1;


def Task4():
    coins = float(input("input coins: "))
    scam = 0

    if coins < 85528:
        scam = (coins * 0.18) + 556.2
    else:
        scam = (coins * 0.32) + 14839.2

    if coins - scam < 0:
        scam = 0

    print(f"Scam: {round(scam, 0)}")


def Task5():
    y = int(input("input year: "))

    if y < 1582:
        print("Not within the Gregorian calendar period")

    elif y % 4 != 0:
        print("Leap year")

    else:
        print("Common year")


def Task6():
    num = int(input("inpyt secret number: "))
    print(
        """
        +=====================================+
        | Ласкаво просимо до моєї гри, магле! |
        | Введіть ціле число                  |
        | і вгадай, яке число я маю           |
        | вибрано для вас.                    |
        | Отже, яке секретне число?           |
        +=====================================+
        """)
    while True:
        x = int(input("input number: "))

        if x == num:
            print("Молодець, магле! Тепер ти вільний")
            return

        print("Ха-ха! Ви застрягли у моїй петлі!")

def Task7():
    for i in range(6):
        print(f"{i} Mississippi")
        time.sleep(1)

    print("Ready or not, here I come!")

def Task8():
    while True:
        msg = str(input("input msg: "))

        if msg == "chupacabra":
            break

        print("You've successfully left the loop.")

def Task9():
    msg = str(input("input msg: "))
    msg = msg.upper()

    for i in range(0, len(msg), 1):
        if msg[i] != "A" and msg[i] != "E" and msg[i] != "I" and msg[i] != "O" and msg[i] != "U":
            print(msg[i])

def Task10():
    msg = str(input("input msg: "))
    msg = msg.upper()
    r = ""

    for i in range(0, len(msg), 1):
        if msg[i] != "A" and msg[i] != "E" and msg[i] != "I" and msg[i] != "O" and msg[i] != "U":
            r += msg[i]

    print(r)

def Task11():
    x = int(input("input blocks: "))
    sep = 0
    result = 0

    for i in range(1, x, 1):
        if x >= i:
            x -= i
            result += 1

    print(f"The height of the pyramid: {result}")

def Task12():
    c = int(input("input c: "))
    steps = 0

    while True:
        if c % 2 == 0:
            c /= 2
        else:
            c = 3 * c + 1

        print(c)
        steps += 1

        if c == 1:
            break

    print(f"Steps = {steps}")

print("Task1:")
Task1()
print("\n")
print("Task2:")
Task2()
print("\n")
print("Task3:")
Task3()
print("\n")
print("Task4:")
Task4()
print("\n")
print("Task5:")
Task5()
print("\n")
print("Task6:")
Task6()
print("\n")
print("Task7:")
Task7()
print("\n")
print("Task8:")
Task8()
print("\n")
print("Task9:")
Task9()
print("\n")
print("Task10:")
Task10()
print("\n")
print("Task11:")
Task11()
print("\n")
print("Task12:")
Task12()
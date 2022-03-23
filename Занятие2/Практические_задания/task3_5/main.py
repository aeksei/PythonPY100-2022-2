mount = int(input())

if mount in [3, 4, 5]:
    print("Весна")
elif mount in [6, 7, 8]:
    print("Лето")
elif mount in (9, 10, 11):
    print("Осень")
elif mount in {12, 1, 2}:
    print("Зима")
else:
    print("Не правильный месяц")

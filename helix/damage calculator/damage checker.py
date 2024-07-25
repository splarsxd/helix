from os import system as sys

value = float(input("Enter value: "))
count = 1
print("Damage | Hits")

while True:
    if (value * count).is_integer():
        print(f"{value * count} | {count}")
        sys("timeout -1 >nul")
        break
    count += 1
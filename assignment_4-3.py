def price():
    money1=int(input("Input amount of money: "))
    appleP=int(input("Input apple price: "))
    return money1, appleP

def main_code(money1, appleP):
    total1=money1//appleP
    total2=money1%appleP
    print(f"You can buy amount of apples: {total1}")
    print(f"Your change is: {total2}")


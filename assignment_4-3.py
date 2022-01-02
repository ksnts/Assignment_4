#function for inputting money and apple price
def price():
    money1=int(input("Input amount of money: "))
    appleP=int(input("Input apple price: "))
    return money1, appleP
#putting the data to the function
money1, appleP = price()
#main function for computing the amount and change
def main_code(total1, total2):
    total1=money1//appleP
    total2=money1%appleP
    print(f"You can buy amount of apples: {total1}")
    print(f"Your change is: {total2}")
#call
main_code(money1, appleP)



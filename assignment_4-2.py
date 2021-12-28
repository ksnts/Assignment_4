print("Note that: Apples: 20 pesos each, Orange: 25 pesos each")
#main code for inputting data 
def main_code():
    orange1=int(input("Input amount of oranges: "))
    apple1=int(input("Input amount of apples: "))
    total=price_code(orangeP=orange1, appleP=apple1)
    print(f"Total amount is: {total} pesos")

#function for computing the total price
def price_code(orangeP, appleP):
    orangeA=25*orangeP
    appleA=20*appleP
    total1=orangeA+appleA
    return total1
#call
main_code()


    

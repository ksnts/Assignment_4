#main code for gathering and returning data
def main_code():
    name1=input("Input your name: ")
    age1=input("Input your age: ")
    add1=input("Input your address: ")
    return name1, age1, add1
#move all inputs to one function
input1, input2, input3 = main_code()


#print output
print(f"Hi, my name is {input1}. I am {input2} years old and I live in {input3}.")
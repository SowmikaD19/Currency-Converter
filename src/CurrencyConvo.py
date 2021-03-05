def currency(userchoice):
    return userchoice * 0.014
    print(currency(float(input())))


def currency2(userchoice):
    return userchoice * 0.011
    print(currency2(float(input())))


def currency3(userchoice):
    return userchoice * 1.47
    print(currency3(float(input())))


userchoice = input("what do you want to convert? \n1) INR to USD \n2) INR to Euro \n3) INR to Yen\n")
if (userchoice == "1"):
    print("Enter the amount you want to convert: ")
    print(currency(float(input())))

elif (userchoice == "2"):
    print("Enter the amount you want to convert: ")
    print(currency2(float(input())))

elif (userchoice == "3"):
    print("Enter the amount you want to convert: ")
    print(currency3(float(input())))

else:
    print("Invalid input. Please try again.")
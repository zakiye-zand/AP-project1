import pandas as pd
from logistic import *
from random import randint
class Payment():
    def __init__(self, wares: list, buyer: list):
        self.wares = wares
        self.buyer = buyer

    # gets all needed information with calling logistick and returns that as buyer information #
    def get_info(self):

        first_name = input("enter your first name : ")
        last_name = input("enter your last name : ")
        number = input("enter your phone number : ")
        temp = Logistic()
        address = Logistic.get_address(temp)
        delivery_method = Logistic.Delivery_method(temp)
        delivery_time = Logistic.Delivery_time(temp)
        purchaseNo = ''.join([str(randint(0, 9)) for _ in range(11)])
        print(f"Your purchase number is : {purchaseNo} ")
        print("Moving to payment portal...")
        self.card = input("enter your 16 digit credit cart number : \n")
        self.buyer = [first_name, last_name, number,
                      address, delivery_method, delivery_time, purchaseNo]
        return self.buyer

    def confirmation(self):         # saves a txt file for confirmation #

        f = open(
            f"C:/Users/LENOVO/Desktop/Ap/project 1/configration_{self.buyer[6]}.txt", mode="w")
        if len(self.card) == 16:
            f.write(f"Your purchase No.{self.buyer[6]} was successfull!")
        else:
            f.write(
                f"Sorry! Your purchase No.{self.buyer[6]} wasn't successfull!\nyour card number was not valid ")
        f.write(
            f"\nName :{self.buyer[0]} {self.buyer[1]} \nCard number :{self.card}")
        f.close()
        print(f"\nYour purchase No.{self.buyer[6]} conformation file  saved.")
        if len(self.card) != 16:
            print("\nyour card number was unavailable ! \nThanks for visiting :)")
            return 0
        else:
            return 1

    def Invoice(self):      # prints invoice as txt if purchase be successfull

        f = open(
            f"C:/Users/LENOVO/Desktop/Ap/project 1/Invoice_{self.buyer[6]}.txt", mode="w")
        f.write(
            f"***Thanks for trusting us***\n\nPurchase number {self.buyer[6]}\nName: {self.buyer[0]} {self.buyer[1]}\n")
        f.write(
            f"Address: {self.buyer[3][0]}-{self.buyer[3][1]}-{self.buyer[3][3]}z\n{self.buyer[3][2]}\n")
        f.write(
            f"Delivery: {self.buyer[4]}-{self.buyer[5][0]}\n")
        for i in self.wares:
            f.write(f"{i[0]}({i[2]}): {i[1]}\n")
        f.close()


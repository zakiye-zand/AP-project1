import pandas as pd
class Logistic:
    def __init__(self):
        self.ds = pd.read_csv(   # ds : delivery schedual
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv")
        pass

    def get_address(self):      # gets and checks and returns the address #
        buyer_address = []

        while (True):
            self.State = eval(
                input("Enter your state code (Tehran: 1, Isfahan: 2, Tabriz: 3): "))
            scode = [1, 2, 3]
            if self.State in scode:
                break
            else:
                print("Wrong code!")

        while (True):
            City = eval(input("Enter your city code (1, 2): "))
            Ccode = [1, 2]
            if City in Ccode:
                break
            else:
                print("Wrong code!")

        Details = input("Enter the details if you want :")
        while (True):
            PostCode = input("Enter your post code (must be 10 digits) :")
            if len(PostCode) != 10:
                print("the post code is not correct!")
            else:
                break

        buyer_address.extend([self.State, City, Details, PostCode])
        return buyer_address

    def Delivery_method(self):      # specifys a method #

        if self.State == 1:
            method = 'Delivery man'
        else:
            method = 'Post'
        return method

    def Delivery_time(self):    # shows available times and takes one #

        print("\nChoose the suitable post delivery time \n\n1.morning ")
        if self.ds.iloc[1, 1] < 3:
            print("2.noon")
        if self.ds.iloc[2, 1] < 3:
            print("3.evening\n")
        self.o = eval(input("option : "))

        return [self.ds.iloc[self.o-1, 0], self.o-1]

    def Update(time_index: int):
        ds = pd.read_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv")      # uppdate the schedual chosen time #
        ds.iloc[time_index, 1] += 1
        ds.to_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv", index=False)
        pass
import pandas as pd
from random import randint


class Role():
    def role():
        o = input("Choose your Role\n1.customer\n2.manager\n")
        return o

    def manager():
        o = input("Choose the section\n1.warehouse\n2.Accounting\n")
        return o


class Warehouse:
    def __init__(self):

        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')

    def Option(self):
        print("***Warehouse managment***\n")
        o = input("1.update list of goods\n2.print list of goods\n")
        # if o == '1':
        #     self.Manualy_update()
        # elif o == '2':
        #     self.Output()
        return o

    def Update(name, number: int):
        d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')
        d.loc[(d['name'] == name), 'number'] = number
        d.to_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv", index=False)
        pass

    def Manualy_update(self):

        o = input(
            "Choose update method\n1.csv file address \n2.enter the code and number of goods\n")

        if o == '2':
            self.Update(eval(input("enter the code\n")),
                        eval(input("enter the new number\n")))
        elif o == '1':
            path = input("enter the path of csv file \n")
            d = pd.read_csv(path)
            for i in d.index:
                self.Update(d.iloc[i, 0], d.iloc[i, 1])
        else:
            print("not available option")

        pass

    def Output(self):
        d = self.d[['wh.code', 'code', 'number']]
        d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.csv", index=False)


class Store():

    def Order(wares: list):  # add the orders to the list
        d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')
        for i in d.index:
            if d.loc[i, 'number'] > 0:
                print(
                    f"{i+1}.({d.loc[i , 'number']}){d.loc[i , 'name']} {d.loc[i , 'price']}")
            else:
                print(f"{i+1}.{d.loc[i , 'name']}\t unavailable")

        o = eval(input("please choose the good you want: "))
        n = eval(input("please choose the number you want: "))
        if d.loc[o-1, 'number'] >= n:
            s = input("Wich size do you want?(M,L,XL) ")
            print("\nthe goods added to your cart successfuly\n")
            l = [d.loc[o-1, 'name'], d.loc[o-1, 'price'], n]
            wares.append(l)

        else:
            print("Oops! the number you want is not available")

        print("Choose an option")
        o = input("1.Back to store\n2.cart\n")
        if o == '1':
            Store.Order()
        return wares

    def cart(wares):
        print(wares)
        print("Choose an option to continue!")
        o = input("1.Back to store\n2.Payment\n")
        return o


class Logistic:
    def __init__(self):
        self.ds = pd.read_csv(   # ds : delivery schedual
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv")
        pass

    def get_address(self):      # gets and check the address #
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

    def Delivery_time(self):    # shows available times and take one #

        print("\nChoose the suitable post delivery time \n\n1.morning ")
        if self.ds.iloc[0, 1] > 0:
            print("2.noon")
        if self.ds.iloc[1, 1] > 0:
            print("3.evening\n")
        self.o = eval(input("option : "))
        return [self.ds.loc[self.o-1, 'time'], o-1]

    def Update(time):
        ds = pd.read_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv")      # uppdate the schedual chosen time #
        ds.loc[time, 1] -= 1
        ds.to_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv", index=False)
        pass


class Payment():
    def __init__(self, wares: list, buyer: list):
        self.wares = wares
        self.buyer = buyer

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

    def confirmation(self):

        f = open(
            f"C:/Users/LENOVO/Desktop/Ap/project 1/configration_{self.buyer[6]}.txt", mode="w")
        if len(self.card) == 16:
            f.write(f"Your purchase No.{self.buyer[6]} was successfull!")
        else:
            f.write(
                f"Sorry! Your purchase No.{self.buyer[6]} wasn't successfull!")
        f.write(
            f"Name :{self.buyer[0]} {self.buyer[1]} \n Card number :{self.card}")
        f.close()
        print(f"Your purchase No.{self.buyer[6]} conformation file  saved.")
        if len(self.card) != 16:
            print("your card number was unavailable ! \nThanks for visiting :)")
            return 0
        else:
            return 1

    def Invoice(self):

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


class Accounting():

    def Update(wares: list, buyer: list):
        d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/accounting.csv')
        number = 0
        price = 0
        for i in wares:
            number += i[2]
            price += eval(i[1])
        d.loc[len(d.index)] = [buyer[6], number, price, 30000, price*9.0/100]
        d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/accounting.csv", index=False)
        pass

    def Output():
        print("the accounting csv file saved !")
        pass


print("***Welcome***")

o = Role.role()
if o == '1':
    wares = []  # [[name , price , number]]
    wares = Store.Order(wares)
    o = Store.cart(wares)
    if o == '1':
        wares = Store.Order(wares)
    elif o == '2':
        buyer = []  # [first name, last name, phone number, [State, City, Details, PostCode], delivery method, [delivery time, index], purchase number]
        payment = Payment(wares, buyer)
        buyer = Payment.get_info(payment)
        if Payment.confirmation(payment) == 1:
            Payment.Invoice(payment)
            print("Purchase completed successfully.\n your invoice file saved")
            Logistic.Update(buyer[5][1])
            Warehouse.Update(wares[0], wares[2])
            Accounting.Update(wares,buyer)


elif o == '2':
    o = Role.manager()
    if o == '1':
        warehouse = Warehouse()
        if Warehouse.Option(warehouse) == '1':
            Warehouse.Manualy_update(warehouse)
        else:
            Warehouse.Output(warehouse)

    if o == '2':
        Accounting.Output()

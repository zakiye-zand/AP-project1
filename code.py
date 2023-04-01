import pandas as pd


def Role():
    # input the role and pass it to the class
    pass

# def Inventory():
    # needs data base ,to make list of good's code and number and price
    pass


def Store(warehouse):
    # show the list of available ware
    pass
# def Update(Inventory):
    # after each order need to update the list of goods
    pass


def Order(Store):
    # 1. take order name
    # 2. take order number and property for eachone
    pass


def Options():
    # show  and take options:
    #           1.store
    #           2.cart
    pass


def cart():
    # show orders
    # calcute the price
    # make sure with showing option:
    # 1. complete the purchase
    # 2. back to store
    # 3.delete good(unneeded)
    pass


def Delivery_time():
    # needs data base to calcute what time to show
    # show the time and take one
    pass


def Specification(Logistic):
    # use get address of logistic
    # fuul name , number , addres , delivery time
    # go to portal
    pass


def Portal():
    # this is a class:...
    # make  random purchase number 11digit
    # get card number 16 digit and check
    # print confirmation by the way as .txt
    # print Invoice if was ok
    pass


class Warehouse():
    def __init__(self):
        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')
        pass
    # update inventory after successfull purchase automaticly
    def Update(self, code: int, number: int):

        self.code = code
        self.number = number

        self.d.loc[(self.d['code'] == self.code), 'number'] = self.number
        print(self.d)
        
    def Manualy_update(self):

        o = input(
            "شیوه تغییر را انتخاب کنید\n1.ادرس فایل csv \n2.وارد کردن کد و موجودی\n")
        
        if o == '2':
            self.Update(eval(input("کد کالا را وارد کنید\n")),
                        eval(input("موجودی جدید را وارد کنید\n")))

        elif o == '1':
            path = input("مسیر فایل را وارد کنید\n")
            d = pd.read_csv(path)
            for i in d.index:
                self.Update(d.iloc[i, 0], d.iloc[i, 1])

        else:
            print("گزینه وارد شده موجود نمیباشد")

    def Output(self):
        d = self.d[['wh.code' , 'code','number']]
        d.to_csv("c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.csv" , index=False)


class Accounting():

    def Update():
        # update the data frame
        pass

    def Output():
        pass


class Logistic:
    def __init__(self) -> None:
        # need a data frame of number of orders by the time and method
        pass

    def get_address():
        # input the address and check them
        pass

    def Delivery_method():
        # alloacate a method by city
        pass

    def Delivery_time():
        # show available time by data frame of that
        # take a time from user
        pass

    def Update():
        # uppdate the data frame by method and chosen time
        pass


x = Warehouse()
x.Output()

import pandas as pd


def Role():
    print("***Welcome***")
    o = input("Choose your Role\n1.customer\n2.saler(manage goods)\n")
    if o == '1':
        Store()
    elif o == '2':
        temp = Warehouse()
        Warehouse.Option(temp)
    pass


class Warehouse:
    def __init__(self):
        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')

    def Option(self):
        print("***Warehouse managment***\n")
        o = input("1.update list of goods\n2.print list of goods\n")
        if o == '1':
            self.Manualy_update()
        elif o == '2':
            self.Output()

    def Update(self, code: int, number: int):

        self.code = code
        self.number = number

        self.d.loc[(self.d['code'] == self.code), 'number'] = self.number
        print(self.d)

    def Manualy_update(self):

        o = input(
            "Choose update method\n1.csv file address \n2.enter the code and number of goods\n")

        if o == '2':
            self.Update(eval(input("enter the code\n")),
                        eval(input("enter the new number\n")))

        elif o == '1':
            path = input("enter the path\n")
            d = pd.read_csv(path)
            for i in d.index:
                self.Update(d.iloc[i, 0], d.iloc[i, 1])

        else:
            print("not available option")

    def Output(self):
        d = self.d[['wh.code', 'code', 'number']]
        d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.csv", index=False)


class Store(Warehouse):
    def __init__(self):
        super().__init__()
        self.list = []
        self.Store()

    def Store(self):  # show the list of available ware
        print("***Store***\n")

        for i in self.d.index:
            if self.d.loc[i, 'number'] > 0:
                print(
                    f"{i+1}.({self.d.loc[i , 'number']}){self.d.loc[i , 'name']}")
        self.Order()

    def Order(self):  # add the orders to the list

        o = eval(input("please choose the good you want:"))
        n = eval(input("please choose the number you want: "))

        if self.d.loc[o-1, 'number'] >= n:
            s = input("Wich size do you want?(M,L,XL) ")
            print("the goods added to your cart successfuly")
            l = [self.d.loc[o-1, 'name'], self.d.loc[o-1, 'price'], n]
            self.list.append(l)
        else:
            print("Oops! the number you want is not available")

        self.Options()

    def Options(self):
        print("Choose an option\n")
        o = input("1.back to store\n2.cart\n")
        if o == '1':
            self.Store()
        elif o == '2':
            self.cart(self.list)

    def cart(self, list):
        wares = pd.DataFrame(list)
        wares.columns = ['name', 'price', 'number']
        print(wares)
        print("Choose an option to continue!\n")
        o = input("1.Back to store\n2.Cash\n")
        if o == '1':
            Store.Store()
        elif o == '2':
            Cash(wares)


class Cash:
    def __init__(self, wares):
        self.wares = wares
        self.buyer = []
        self.get_info()

    def get_info(self):

        first_name = input("enter your first name : ")
        last_name = input("enter your last name : ")
        number = input("enter your phine number : ")
        temp = Logistic()
        address = Logistic.get_address(temp)
        delivery_method = Logistic.Delivery_method(temp)
        delivery_time = Logistic.Delivery_time(temp)
        self.buyer.append(first_name, last_name, number,
                          address, delivery_method, delivery_time)
        print("Moving to payment portal...")
        # اینجااگه بشه چن ثانتیه صبر کنه بعد بره جالب میشه
        Portal()


class Portal():
    # this is a class:...
    # make  random purchase number 11digit
    # get card number 16 digit and check
    # print confirmation by the way as .txt
    # print Invoice if was ok
    pass


class Logistic:
    def __init__(self):
        self.ds = pd.read_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/Delivery schedual.csv")
        # ds : delivery schedual
        # باید بخونه و بشه تغییرش داد باید ببینم یه راه خاص داشت فک کنم

    def get_address(self):      # gets and check the address #

        buyer_address = []  # دو وایل باید زده بشه
        self.State = eval(
            input("Enter your state code (Tehran: 1, Isfahan: 2, Tabriz: 3): "))
        if self.State != 1 and self.State != 2 and self.State != 3:  # این باید بشه یجور بهتر زدش
            print("Wrong code!")
        City = eval(input("Enter your city code (1, 2): "))
        # اشتباهش هم باید چک شه
        Details = input("Enter the details if you want :")
        # باید دیجیتای این چک شه و وایل زده شه
        PostCode = eval(input("Enter your post code (must be 10 digits) :"))
        buyer_address.append(self.State, City, Details, PostCode)
        return buyer_address

    def Delivery_method(self):      # specifys a method #

        if self.State == 1:
            method = 'Peik'
        else:
            method = 'Post'
        return method

    def Delivery_time(self):    # shows available times and take one #

        print("\nChoose the suitable post delivery time \n\n1.morning ")
        if self.ds.iloc[0, 1] > 0:
            print("2.noon")
        if self.ds.iloc[1, 1] > 0:
            print("3.evening\n")
        o = eval(input("option : "))
        return o

    def Update():       # uppdate the schedual chosen time #
        # اینحا باید ریرایت شه...
        pass


class Accounting():

    def Update():
        # update the data frame
        pass

    def Output():
        pass


Role()

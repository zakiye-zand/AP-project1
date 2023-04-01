import pandas as pd


def Role():
    print("***خوش امدید***")
    o = input("نقش خود را انتخاب کنید\n1.بازدیدکننده\n2.فروشنده(مدیریت موجودی)\n")
    if o == '1':
        Store()
    elif o == '2':
        Warehouse.Option()
    pass


class Warehouse:
    def __init__(self):
        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')

    def Option(self):
        print("***مدیریت انبار***\nگزینه مورد نظر خود را انتخاب کنید\n")
        o = input("1.مدیریت دستی\n2.دریافت لیست موجودی\n")
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
        d = self.d[['wh.code', 'code', 'number']]
        d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.csv", index=False)


class Store(Warehouse):
    def __init__(self):
        super().__init__()
        self.list = []

    def Store(self):  # show the list of available ware
        print("***فروشگاه***\n")

        for i in self.d.index:
            if self.d.loc[i, 'number'] > 0:
                print(
                    f"{i+1}.({self.d.loc[i , 'number']}){self.d.loc[i , 'name']}")
        self.Order()

    def Order(self):
        
        o = eval(input("لطفا کالای مورد نظر خود را انتخاب کنید :"))
        n = eval(input("تعداد مورد نظر را وارد کنید: "))

        if self.d.loc[o-1,'number']>= n:
            s = input("سایز مورد نظر را وارد کنید(M,L,XL) ")
            print("کالای مورد نظر با موفقیت به سبد خرید اضافه شد")
            l = [self.d.loc[o-1,'name'] ,self.d.loc[o-1,'price'], n ]
            self.list.append(l)
        else:
            print("خطا! تعداد انتخابی بیشتر از موجودی میباشد")

        self.Option()    

    def Options(self):
        print("جهت ادامه یکی از گزینه ها را انتخاب کنید\n")
        o = input("1.بازگشت به فروشگاه\n2.سبد خرید\n")
        if o == '1' : self.Store()
        elif o =='2' : self.cart(self.list)

    def cart(self ,list):
        wares = pd.DataFrame(list)
        wares.columns = ['name' , 'price' , 'number']    
        print(wares)
        print("جهت ادامه یکی از گزینه ها را انتخاب کنید\n")
        o = input("1.بازگشت به فروشگاه\n2.تسویه حساب\n")
        if o == '1' : Store.Store()
        elif o =='2' : Cash(wares)


class Cash:
    def __init__(self , wares):
        self.wares = wares
    def get_name():
        pass
    def Specification(Logistic):
        # use get address of logistic
        # fuul name , number , addres , delivery time
        # go to portal
        pass
    def Delivery_time():
        # needs data base to calcute what time to show
        # show the time and take one
        pass


    def Portal():
        # this is a class:...
        # make  random purchase number 11digit
        # get card number 16 digit and check
        # print confirmation by the way as .txt
        # print Invoice if was ok
        pass


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


x = Store()
x.Store()

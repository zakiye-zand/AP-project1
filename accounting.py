import pandas as pd
class Accounting():         # updates accounting file after each successful purchase and saves it #

    def Update(wares: list, buyer: list):
        d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/accounting.csv')
        number = 0
        price = 0
        for i in wares:
            number += i[2]
            price += eval(i[1][:-1])*i[2]
        d.loc[len(d.index)] = [buyer[6], number, price, 30000, price*9.0/100]
        d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/accounting.csv", index=False)
        pass

    def Output():
        print("the accounting csv file saved !\n")
        pass